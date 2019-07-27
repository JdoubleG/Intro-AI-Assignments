James Garijo-Garde
4/30/2019

Comp131 Homework 5

This is a behavior tree modeled after the behavior of a Roomba cleaning robot.
It uses the extra credit hierarchy of nodes implementation.

Details:
  * Each node of the behavior tree is an instance of the HoN_BTree class.
        * Nodes have a type (Task, Conditional, Decorator, or Composite), a
          subtype (if applicable), an associated action passed in as a function
          (if applicable), and a collection of children nodes.
  * The blackboard is a Python dict with the keys and values as described by the
    assignment.
        * The ambiguous HOME_PATH element is represented as a string "Home path at
          [time find home was called]".
  * The overall algorithm of Roomba.py is a while loop that runs the
    updateState() and evaluateTree(tree, blackboard, time) functions while also
    increasing time.
        * updateState activates different flags at random: DUSTY_SPOT is
          activated 1/5 times, GENERAL is activated 1/2 times, and SPOT is
          activated 1/3 times.
        * updateState also decreases battery by either 1 or 2 (randomly decided
          with 1:1 odds) each turn.

How to Run:
Type "python3 Roomba.py" into your command line. Be sure HoN_BTree.py is in the
same directory. The program will run the Roomba behavior tree for at least 100
"minutes" (iterations of the while loop) and display output indicating the
results of each step.

Additional Notes:
I changed the sequence above the sequence with the "Until Fail" decorator and
the DONE GENERAL node to a selection because the DONE GENERAL node would
otherwise never be reached since the "Until Fail" sequence always does its
children until a "Fail" signal is sent, which causes the above sequence to
evaluate to "Fail" without ever considering the value of DONE GENERAL. Please
don't take off points for this :)