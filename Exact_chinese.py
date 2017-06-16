import util

__author__ = 'pegah'

import numpy as np
ftype = np.float32

class exact:
    def __init__(self, _mdp, _states_list, _lambda, _discount= 1.0, _height= 63):
        self.mdp = _mdp
        self.d = self.mdp.d
        self.discount = _discount
        self.height = _height

        self.Lambda = np.zeros(len(_lambda), dtype=ftype)
        self.Lambda[:] = _lambda

        self.states = _states_list
        self.values = util.Counter(1) # A Counter is a dict with default [0, 0, .., 0]

        self.query_counter_ = 0

    # the exact value iteration goes here

    def computeQValueFromValues(self, state, action, reward):
        value = [0]
        transitionFunction = self.mdp.getTransitionStatesAndProbs(state,action)

        for nextState, probability in transitionFunction:
            rewards = (np.array(reward)).dot(self.Lambda)
            value += probability * (np.array(rewards) + (self.discount * np.array(self.values[nextState])))

        return value

    def exact_value_iteraion(self):

        states_list = self.states
        print 'states_list', states_list
        optimal_policy = {i:None for i in states_list}
        time = self.height

        while time > -1:
            print 'tour', time
            valuesCopy = self.values.copy()
            for state in (states_list):
                _V_best = [0]
                possible_actions = self.mdp.getPossibleActions(state)

                for action in possible_actions:
                    rewards_list = self.mdp.getQoS(state, action, time)

                    for reward_value in rewards_list[1]:
                        Q_d = self.computeQValueFromValues(state, action, reward_value)

                        if Q_d[0] > _V_best[0]:
                            _V_best = Q_d
                            optimal_policy[state] = action

                        valuesCopy[state] = _V_best

            print 'copy', valuesCopy
            print 'value', self.values

            self.values = valuesCopy
            time -= 1

        print 'optimal policy', optimal_policy
        print "query_counter_", self.query_counter_

        return self.values