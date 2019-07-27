James Garijo-Garde
2/11/2019

Comp131 Homework 1

Definition of the Problem as a searching problem:

        The pancake problem can easily be defined as a searching problem. Here
        are elements of a search problem specific to the pancake problem:

        1) Initial State: the starting arrangement of the pancakes on the plate.
           In my implementation, the pancake stack is represented as an array of
           numeric values representing the widths of the pancakes.
        2) Possible Actions: a flip. Example: [2, 1, 3, 4, 5] can be flipped
           between the 2 and the 3 to yield [1, 2, 3, 4, 5].
        3) Successor Function: executes a flip based on the best next state in
           the priority queue.
        4) Goal Test: I have implemented the goal test to ensure all of the
           pancakes on the stack have a width greater than the one immediately
           below. This is a viable test because each pancake width occurs only
           once per stack.
        5) Path Cost Function: the path cost is set equal to the number of flips
           needed to reach the current state.


Cost Functions:
        Backwards Cost: number of flips
        Forward Cost: Gap Heuristic, as defined in the article provided


Running my Implementation of the A* search algorithm:
        python3 Flipper.py