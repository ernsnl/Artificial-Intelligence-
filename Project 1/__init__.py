# Şinasi Eren Şenel
# Python 3.5.x
# Run __init__
import sl_draw
from problem import Problem
import uninformed_tree as _t
import a_star as _a
import a_star
import time
import timeit



given_problem = ["3 2 2 h", "4 1 2 v", "6 1 2 v",
                 "5 2 2 v", "6 3 2 h", "3 4 3 v", "3 5 2 v"] # Given Problem
altered_problem = ["3 2 2 h", "4 1 2 v", "6 1 2 v", "5 2 2 v", "6 3 2 h",
                   "3 4 3 v", "3 5 2 v", "4 6 2 v"]  # Altered Problem
goal = "3 5 2 h"

def heuristic_1(node): # Distance Between the goal object and the goal
    node_goal_piece = node.state[0].split(" ")
    goal_row = int(goal.split(" ")[0])
    goal_column = int(goal.split(" ")[1])
    return int(node_goal_piece[0]) - goal_row + int(node_goal_piece[1]) - goal_column

def heuristic_2(node):
    temp = Problem("aa")
    node_goal_piece = node.state[0].split(" ")
    node_movement_matrix = temp.get_movement_matrix(node.state)

    goal_row = int(goal.split(" ")[0])
    goal_column = int(goal.split(" ")[1])
    goal_distance = int(node_goal_piece[0]) - goal_row + int(node_goal_piece[1]) - goal_column

    heuristic = 0
    for _ in range(0, goal_distance):
        if(int(movement_matrix[goal_row - 1][goal_column - 2 + _]) == 1):
            heuristic += 1
    return heuristic

def draw_solution(initial, solution):
    temp = Problem(initial)
    for step in solution:
        sl_draw.draw_sliding_block(initial)
        initial = temp.result(initial, step)

pm = Problem(given_problem, goal)

start = timeit.default_timer()
#solution = _t.breadth_first_tree_search(pm).solution() # breadth-first
#solution = _t.depth_first_tree_search(pm).solution() # depth-first
solution = _a.astar_search(pm,heuristic_2).solution() # heuristic
stop = timeit.default_timer()
print(stop-start)

draw_solution(pm.initial, solution)
