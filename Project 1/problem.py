"""Base code was orginally created by https://github.com/aimacode/aima-python/blob/master/search.py
Problem is adjusted the sliding block problem for project purposes."""

import numpy as np
import time

grid_size = 6


class Problem(object):

    """The abstract class for a formal problem.  You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        list_actions = []
        movement_matrix = self.get_movement_matrix(state)
        for block in state:
            _iter = 1
            block_splt = block.split(" ")
            row = int(block_splt[0])
            column = int(block_splt[1])
            length = int(block_splt[2])
            direction = block_splt[3]
            if(direction == "h"):
                _iter = 1
                while(column + length + _iter - 1 <= grid_size):  # Check for right
                    if(int(movement_matrix[row - 1][column + length + _iter - 2]) == 0):
                        list_actions.append(block + " +x" + str(_iter))
                        _iter += 1
                    else:
                        break

                _iter = 1
                while(column - _iter - 1 > 0):  # Check for the left
                    if(int(movement_matrix[row - 1][column - _iter - 1]) == 0):
                        list_actions.append(block + " -x" + str(_iter))
                        _iter += 1
                    else:
                        break

            if(direction == "v"):
                _iter = 1
                while(row - length - _iter + 1 > 0):  # Check for the up
                    if(int(movement_matrix[row - length - _iter][column - 1]) == 0):
                        list_actions.append(block + " +y" + str(_iter))
                        _iter += 1
                    else:
                        break

                _iter = 1
                while(row + _iter - 1 < grid_size):  # Check for down
                    if(int(movement_matrix[row - 1 + _iter][column - 1]) == 0):
                        list_actions.append(block + " -y" + str(_iter))
                        _iter += 1
                    else:
                        break
        return list_actions

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        action_splt = action.split(" ")

        return_state = []
        for block in state:
            block_splt = block.split(" ")
            if(block_splt[0] == action_splt[0]
               and block_splt[1] == action_splt[1]):
                movement_amount = int(action_splt[4][-1])
                if("+y" in action_splt[4]):
                    block = str(int(block_splt[0]) - movement_amount)
                    block += " " + block_splt[1]
                    block += " " + block_splt[2]
                    block += " " + block_splt[3]
                elif("-y" in action_splt[4]):
                    block = str(int(block_splt[0]) + movement_amount)
                    block += " " + block_splt[1]
                    block += " " + block_splt[2]
                    block += " " + block_splt[3]
                elif("+x" in action_splt[4]):
                    block = block_splt[0]
                    block += " " + str(int(block_splt[1]) + movement_amount)
                    block += " " + block_splt[2]
                    block += " " + block_splt[3]
                else:
                    block = block_splt[0]
                    block += " " + str(int(block_splt[1]) - movement_amount)
                    block += " " + block_splt[2]
                    block += " " + block_splt[3]
            return_state.append(block)
        return return_state

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        return self.goal == state[0]

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError

    def get_movement_matrix(self, state):
        matrix = np.zeros((6, 6))
        for block in state:
            block_st = block.split(" ")
            if(block_st[3] == 'h'):
                for _ in range(0, int(block_st[2])):
                    matrix[int(block_st[0]) - 1][int(block_st[1]) - 1 + _] = 1
            if(block_st[3] == 'v'):
                for _ in range(0, int(block_st[2])):
                    matrix[int(block_st[0]) - 1 - _][int(block_st[1]) - 1] = 1
        return matrix
# ______________________________________________________________________________
