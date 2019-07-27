"""
        James Garijo-Garde
        2/11/2019

        Comp131 Homework 1

        This is an implementation of the A* search algorithm to solve the
        pancake problem.
"""

from PriorityQueue import PriorityQueue

# Implementation of the A* search. This implementation uses 4 possible flips at
# 4 different points on the pancake stack. 
def a_star(stack):
        # Checks that the initial stack of pancakes is not already solved
        if goaltest(stack):
                        return stack
        frontier = PriorityQueue()
        visited = []
        flipped = 0     # This is the backwards cost
        # Possible Flip 1:
        flip1 = [stack[1], stack[0], stack[2], stack[3], stack[4]]
        frontier.push(heuristic(flip1), flip1)
        # Possible Flip 2:
        flip2 = [stack[2], stack[1], stack[0], stack[3], stack[4]]
        frontier.push(heuristic(flip2), flip2)
        # Possible Flip 3:
        flip3 = [stack[3], stack[2], stack[1], stack[0], stack[4]]
        frontier.push(heuristic(flip3), flip3)
        # Possible Flip 4:
        flip4 = [stack[4], stack[3], stack[2], stack[1], stack[0]]
        frontier.push(heuristic(flip4), flip4)
        while True:
                if frontier.isEmpty():
                        print("ERROR! Pancakes could not be processed!")
                        exit()
                node = frontier.pop()
                # Checks that node has not already been visited
                for i in range(len(visited)-1):
                        if node[1] == visited[i][1]:
                                if frontier.isEmpty():
                                        print("ERROR! Pancakes could not be processed!")
                                        exit()
                                node = frontier.pop()
                visited.append(node)
                # recalculates backwards cost
                flipped = 1 + node[0] - heuristic(node[1])
                ### FOR DEBUGGING ###
                # print("FLIPS: " + str(flipped) + " " + str(node[1]))
                # Checks if the node is the goal state
                if goaltest(node[1]):
                        return node[1]
                # Possible Flip 1:
                flip1 = [node[1][1], node[1][0], node[1][2], node[1][3], node[1][4]]
                costCompare(frontier, flip1, visited, flipped)
                # Possible Flip 2:
                flip2 = [node[1][2], node[1][1], node[1][0], node[1][3], node[1][4]]
                costCompare(frontier, flip2, visited, flipped)
                # Possible Flip 3:
                flip3 = [node[1][3], node[1][2], node[1][1], node[1][0], node[1][4]]
                costCompare(frontier, flip3, visited, flipped)
                # Possible Flip 4:
                flip4 = [node[1][4], node[1][3], node[1][2], node[1][1], node[1][0]]
                costCompare(frontier, flip4, visited, flipped)

# Checks the pancake stack to see if it has been solved.
def goaltest(stack):
        goalstate = True
        stack.append(6)
        for i in range(len(stack)-1):
                if stack[i] > stack[i+1]:
                        goalstate = False
                        break
        stack.remove(6)
        return goalstate

# My implementation of the Gap Heuristic.
def heuristic(stack):
        stack.append(6)
        gaps = 0
        for i in range(len(stack)-1):
                if abs(stack[i+1] - stack[i]) > 1:
                        gaps = gaps + 1
        stack.remove(6)
        return gaps

# Ensures the costs in the priority queue are optimal.
def costCompare(frontier, flip, visited, backwards):
        cost = backwards + heuristic(flip)
        add = True
        for i in range(len(visited)-1):
                if flip == visited[i][1]:
                        add = False
                        if visited[i][0] > cost:
                                del visited[i]
                                add = True
                        break
        if add:
                frontier.push(cost, flip)

# Runs the program if it is invoked in standalone.
if __name__ == '__main__': 
        print("The Pancake Problem:\n")
        ### FOR DEBUGGING ###
        input = [2, 4, 3, 5, 1] # manipulate this to control what is input into A*
        print("Input Order: " + str(input))
        print("Output Order: " + str(a_star(input)))