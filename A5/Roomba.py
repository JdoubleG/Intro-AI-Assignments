"""
        James Garijo-Garde
        4/30/2019

        Comp131 Homework 5

        Simulates a Roomba using behavior trees.
"""

import random
import copy
from HoN_BTree import HoN_BTree

# builds and returns the behavior tree
def buildTree():
        sc = HoN_BTree("Conditional", None, spotConditional)
        cw = HoN_BTree("Task", None, cleanSpot20)
        ds = HoN_BTree("Task", None, doneSpot)
        c9 = HoN_BTree("Composite", "Sequence", None)
        c9.addChildren(sc)
        c9.addChildren(cw)
        c9.addChildren(ds)
        
        ch = HoN_BTree("Conditional", None, cleanSpot35)
        us = HoN_BTree("Task", None, dustySpot)
        c8 = HoN_BTree("Composite", "Sequence", None)
        c8.addChildren(us)
        c8.addChildren(ch)

        gc = HoN_BTree("Task", None, clean)
        c7 = HoN_BTree("Composite", "Selection", None)
        c7.addChildren(c8)
        c7.addChildren(gc)

        nb = HoN_BTree("Conditional", None, notLowBattery)
        c6 = HoN_BTree("Composite", "Sequence", None)
        c6.addChildren(nb)
        c6.addChildren(c7)

        fl = HoN_BTree("Decorator", "Until Fail", None)
        fl.addChildren(c6)

        dg = HoN_BTree("Task", None, doneGeneral)
        c5 = HoN_BTree("Composite", "Selection", None)
        c5.addChildren(fl)
        c5.addChildren(dg)

        cg = HoN_BTree("Conditional", None, conditionalGeneral)
        c4 = HoN_BTree("Composite", "Sequence", None)
        c4.addChildren(cg)
        c4.addChildren(c5)

        c3 = HoN_BTree("Composite", "Selection", None)
        c3.addChildren(c9)
        c3.addChildren(c4)

        lb = HoN_BTree("Conditional", None, lowBattery)
        fh = HoN_BTree("Task", None, findHome)
        gh = HoN_BTree("Task", None, goHome)
        dk = HoN_BTree("Task", None, dock)
        c2 = HoN_BTree("Composite", "Sequence", None)
        c2.addChildren(lb)
        c2.addChildren(fh)
        c2.addChildren(gh)
        c2.addChildren(dk)
        
        dn = HoN_BTree("Task", None, doNothing)
        c1 = HoN_BTree("Composite", "Priority", None)
        c1.addChildren(c2)
        c1.addChildren(c3)
        c1.addChildren(dn)

        return c1

# sets up the initial blackboard
def setupBlackboard():
        board = {"BATTERY_LEVEL": 100, "SPOT": False, "GENERAL": False,
                 "DUSTY_SPOT": False, "HOME_PATH": "Initial Home Path"}
        return board

# changes the state of the environment and updates the black board accordingly
def updateState(blackboard):
        # change the battery level
        blackboard["BATTERY_LEVEL"] = blackboard["BATTERY_LEVEL"] - random.randint(1, 2)
        # randomly activate DUSTY_SPOT
        dusty = random.randint(1, 5)
        if dusty == 1:
                blackboard["DUSTY_SPOT"] = True
        # randomly activate GENERAL
        general = random.randint(1, 2)
        if general == 1:
                blackboard["GENERAL"] = True
        # randomly activate SPOT
        spot = random.randint(1, 3)
        if spot == 1:
                blackboard["SPOT"] = True
        # etc.
        return blackboard

# evaluate the tree given the current status of the blackboard and time
def evaluateTree(tree, blackboard, time):
        result = tree.act(blackboard, time, None)

# Functions used by the behavior tree nodes:
def spotConditional(blackboard, a, b):
        if blackboard["SPOT"] == True:
                return ["SPOT", "Success"]
        else:
                return ["SPOT", "Fail"]

def cleanSpot20(blackboard, time, b):
        start = copy.deepcopy(time)
        while time - start < 20:
                print("CLEAN SPOT is Running")
                time = time + 1
                blackboard["BATTERY_LEVEL"] = blackboard["BATTERY_LEVEL"] - \
                    random.randint(1, 2)
        blackboard["SPOT"] = False
        return ["CLEAN SPOT", "Success"]

def doneSpot(blackboard, a, b):
        blackboard["SPOT"] = False
        return ["DONE SPOT", "Success"]

def cleanSpot35(blackboard, time, b):
        start = copy.deepcopy(time)
        while time - start < 35:
                print("CLEAN SPOT is Running")
                time = time + 1
                blackboard["BATTERY_LEVEL"] = blackboard["BATTERY_LEVEL"] - \
                    random.randint(1, 2)
        blackboard["DUSTY_SPOT"] = False
        return ["CLEAN SPOT", "Success"]

def dustySpot(blackboard, a, b):
        if blackboard["DUSTY_SPOT"] == True:
                return ["DUSTY SPOT", "Success"]
        else:
                return ["DUSTY SPOT", "Fail"]

def clean(blackboard, a, b):
        blackboard["BATTERY_LEVEL"] = blackboard["BATTERY_LEVEL"] - \
            random.randint(1, 2)
        return ["CLEAN", "Running"]

def notLowBattery(blackboard, a, b):
        if blackboard["BATTERY_LEVEL"] < 30:
                return ["BATTERY > 30%", "Fail"]
        else:
                return ["BATTERY > 30%", "Success"]

def doneGeneral(blackboard, a, b):
        blackboard["GENERAL"] = False
        return ["DONE GENERAL", "Success"]

def conditionalGeneral(blackboard, a, b):
        if blackboard["GENERAL"] == True:
                return ["GENERAL", "Success"]
        else:
                return ["GENERAL", "Fail"]

def lowBattery(blackboard, a, b):
        if blackboard["BATTERY_LEVEL"] < 30:
                return ["BATTERY < 30%", "Success"]
        else:
                return ["BATTERY < 30%", "Fail"]

def findHome(blackboard, time, b):
        blackboard["HOME_PATH"] = "Home path at " + str(time)
        return ["FIND HOME", "Success"]

def goHome(blackboard, a, b):
        return ["GO HOME", "Success"]

def dock(blackboard, a, b):
        blackboard["BATTERY_LEVEL"] = 100
        return ["DOCK", "Success"]

def doNothing(blackboard, a, b):
        return ["DO NOTHING", "Success"]


####  MAIN  #####
if __name__ == '__main__':
        tree = buildTree()
        blackboard = setupBlackboard()
        time = 0
        # Roomba opperates for 100 iterations (seconds)
        while time < 100:
                evaluateTree(tree, updateState(blackboard), time)
                time = time + 1
