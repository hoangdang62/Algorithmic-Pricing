import random


class Agent(object):
    def __init__(self, agent_number, params={}):
        self.this_agent_number = agent_number  # index for this agent
        self.n_items = params["n_items"]

    def _process_last_sale(self, last_sale):
        pass

    # Given an observation which is #info for new buyer, information for last iteration, and current profit from each time
    # Covariates of the current buyer
    # Data from last iteration (which item customer purchased, who purchased from, prices for each agent for each item (2x2, where rows are agents and columns are items)))
    # Returns an action: a list of length n_items=2, indicating price this agent is posting for each item.
    def action(self, obs):
        new_buyer_covariates, new_buyer_embedding, last_sale, state = obs
        self._process_last_sale(last_sale)
        # prices that I determined were pretty good if doing fixed prices for each item, i.e. not using embeddings or covariates
        return [0.97498204, 4.19529964]
