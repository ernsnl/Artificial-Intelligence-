# Got it from https://github.com/aimacode/aima-python/blob/master/

from utils import (
    is_in, argmin, argmax, argmax_random_tie, probability,
    weighted_sample_with_replacement, memoize, print_table, DataFile, Stack,
    FIFOQueue, PriorityQueue, name
)

from node import Node
from grid import distance

from collections import defaultdict
import math
import random
import sys
import bisect



def best_first_graph_search(problem, f):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    node_expanded = 0
    node_generated = 0
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue(min, f)
    frontier.append(node)
    explored = list()
    while frontier:
        node = frontier.pop()
        node_generated += 1
        if problem.goal_test(node.state):
            print("Generated Node " + str(node_generated + len(frontier)) + " Node Expanded " + str(node_expanded))
            return node
        explored.append(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
                node_expanded += 1
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)

    return None

# ______________________________________________________________________________
# Informed (Heuristic) Search


def astar_search(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))

# ______________________________________________________________________________
