import random
import pickle
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LogisticRegression


class Agent(object):
    def __init__(self, agent_number, params={}):
        self.this_agent_number = agent_number  # index for this agent
        self.opponent_number = 1 - agent_number  # index for opponent
        self.n_items = params["n_items"]
        self.filename1 = 'agents/thethreemusketeers_files/user_model'
        self.user_model = pickle.load(open(self.filename1, 'rb'))
        self.filename2 = 'agents/thethreemusketeers_files/demand_model'
        self.demand_model = pickle.load(open(self.filename2, 'rb'))
        self.item0file = 'agents/thethreemusketeers_files/item0embedding'
        self.item0_embedding = pickle.load(open(self.item0file, 'rb'))
        self.item1file = 'agents/thethreemusketeers_files/item1embedding'
        self.item1_embedding = pickle.load(open(self.item1file, 'rb'))
        self.competition_outcome = []
        self.covariates = []

    def _process_last_sale(self, last_sale, profit_each_team):
        # print("last_sale: ", last_sale)
        # print("profit_each_team: ", profit_each_team)
        my_current_profit = profit_each_team[self.this_agent_number]
        opponent_current_profit = profit_each_team[self.opponent_number]

        my_last_prices = last_sale[2][self.this_agent_number]
        opponent_last_prices = last_sale[2][self.opponent_number]

        did_customer_buy_from_me = last_sale[1] == self.this_agent_number
        did_customer_buy_from_opponent = last_sale[1] == self.opponent_number

        which_item_customer_bought = last_sale[0]

        # print("My current profit: ", my_current_profit)
        # print("Opponent current profit: ", opponent_current_profit)
        # print("My last prices: ", my_last_prices)
        # print("Opponent last prices: ", opponent_last_prices)
        # print("Did customer buy from me: ", did_customer_buy_from_me)
        # print("Did customer buy from opponent: ",
        #       did_customer_buy_from_opponent)
        # print("Which item customer bought: ", which_item_customer_bought)

        if any(np.isnan(my_last_prices)):
            return None
        # new_entry = [my_last_prices[0], my_last_prices[1], opponent_last_prices[0], opponent_last_prices[1],
        #              did_customer_buy_from_me]
        new_entry = [my_last_prices[0], my_last_prices[1], did_customer_buy_from_me]
        self.competition_outcome.append(new_entry)
        # df_competition = pd.DataFrame(self.competition_outcome, columns=['my_0', 'my_1', 'op_0', 'op_1', 'win'])
        df_competition = pd.DataFrame(self.competition_outcome, columns=['my_0', 'my_1', 'win'])
        df_covariates = pd.DataFrame(self.covariates, columns=['1', '2', '3'])
        df_all = pd.concat([df_competition, df_covariates], axis=1)
        if len(df_all) < 200:
            return None
        elif len(df_all) < 1000:
            df_train = df_all.copy()
        else:
            df_train = df_all.sample(1000)

        rf = LogisticRegression().fit(df_train.drop(columns=['win']).values, df_train['win'].values)
        return rf


    # Given an observation which is #info for new buyer, information for last iteration, and current profit from each time
    # Covariates of the current buyer, and potentially embedding. Embedding may be None
    # Data from last iteration (which item customer purchased, who purchased from, prices for each agent for each item (2x2, where rows are agents and columns are items)))
    # Returns an action: a list of length n_items=2, indicating prices this agent is posting for each item.
    def action(self, obs):
        new_buyer_covariates, new_buyer_embedding, last_sale, profit_each_team = obs
        if not any(np.isnan(last_sale[2][self.this_agent_number])):
            self.covariates.append(new_buyer_covariates)
        competition_model = self._process_last_sale(last_sale, profit_each_team)

        if len(self.competition_outcome) < 200:
            return np.random.uniform(0, 3, 2)
        else:
            if new_buyer_embedding is None:
                new_buyer_embedding = self.user_model.predict(np.array(new_buyer_covariates).reshape(1, -1))[0]
            item_mat = np.array([self.item0_embedding, self.item1_embedding])
            user_ratings = np.matmul(new_buyer_embedding, item_mat.T)

            top_revenues = []
            top_prices = []
            max_revenue = 0
            optimal_price = [0, 0]
            for price_0 in np.arange(0, 6, 1):
                for price_1 in np.arange(0, 6, 1):
                    new_row = (price_0, price_1, new_buyer_covariates[0], new_buyer_covariates[1], new_buyer_covariates[2],
                               user_ratings[0], user_ratings[1])
                    demand = self.demand_model.predict_proba(np.array(new_row).reshape(1, -1))
                    revenue = demand[0][1] * price_0 + demand[0][2] * price_1
                    if revenue > max_revenue:
                        max_revenue = revenue
                        optimal_price[0] = price_0
                        optimal_price[1] = price_1

            for price_0 in np.arange(optimal_price[0] - 0.7, optimal_price[0] + 0.7, 0.1):
                for price_1 in np.arange(optimal_price[1] - 0.7, optimal_price[1] + 0.7, 0.1):
                    new_row = (price_0, price_1, new_buyer_covariates[0], new_buyer_covariates[1], new_buyer_covariates[2],
                               user_ratings[0], user_ratings[1])
                    demand = self.demand_model.predict_proba(np.array(new_row).reshape(1, -1))
                    revenue = demand[0][1] * price_0 + demand[0][2] * price_1
                    top_revenues.append(revenue)
                    top_prices.append([price_0, price_1])

            top20_prices = np.array(top_prices)[np.argsort(top_revenues)][::-1][:20]
            df_20prices = pd.DataFrame(top20_prices)
            covariate_tiled = pd.DataFrame(np.tile(new_buyer_covariates, (20, 1)))
            df_test = pd.concat([df_20prices, covariate_tiled], axis=1)
            my_sale_proba = competition_model.predict_proba(df_test)[:, 1]
            if not any(competition_model.predict(df_test)):
                return np.random.uniform(0, 3, 2)
            else:
                return top20_prices[np.argmax(my_sale_proba)]
