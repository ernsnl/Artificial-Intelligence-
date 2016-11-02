# Got it from https://github.com/aimacode/aima-python/blob/master/

# ______________________________________________________________________________
# Uninformed Search algorithms
from utils import (
    is_in, argmin, argmax, argmax_random_tie, probability,
    weighted_sample_with_replacement, memoize, print_table, DataFile, Stack,
    FIFOQueue, PriorityQueue, name
)
from node import Node
import time



def tree_search(problem, frontier):
    """Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Don't worry about repeated paths to a state. [Figure 3.7]"""
    frontier.append(Node(problem.initial))
    node_expanded = 0
    node_generated = 0
    while frontier:
        node = frontier.pop()
        node_generated += 1
        if problem.goal_test(node.state):
            print("Generated Node " + str(node_generated + len(frontier)) + " Node Expanded " + str(node_expanded))
            return node
        node_expanded += 1
        frontier.extend(node.expand(problem))
    return None


def breadth_first_tree_search(problem):
    "Search the shallowest nodes in the search tree first."
    return tree_search(problem, FIFOQueue())


def depth_first_tree_search(problem):
    "Search the deepest nodes in the search tree first."
    return tree_search(problem, Stack())
