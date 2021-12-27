"""
From here mostly: https://github.com/openai/multiagent-particle-envs/blob/master/make_env.py
"""
from settings import *


import algopricing_opy.MultiAgentEnv_algopricing as MultiAgentEnv_algopricing
from algopricing_opy.MultiAgentEnv_algopricing import MultiAgentEnv_algopricing


def make_env_agents(agentnames, params=default_params, first_file=None, second_file=None, third_file=None):
    import agents

    agents = [
        agents.load(name + ".py").Agent(en, params)
        for en, name in enumerate(agentnames)
    ]
    env = MultiAgentEnv_algopricing(
        params, agentnames, len(
            agentnames), first_file, second_file, third_file
    )
    return env, agents
