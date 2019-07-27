"""
        James Garijo-Garde
        4/30/2019

        Comp131 Homework 5

        Heirarchy of nodes implementation of the Roomba behavior tree.
"""

class HoN_BTree:

        # Initializes behavior tree
        def __init__(self, elem, flavor, func):
                self.element = elem
                self.subtype = flavor
                self.action = func
                self.children = []
        
        # populates the children array with the Behavior tree's children nodes
        def addChildren(self, child):
                self.children.append(child)

        # performs a node's specific action.
        def act(self, blackboard, a, b):
                if self.element == "Composite":
                        if self.subtype == "Priority":
                                result = self.priority(blackboard, a, b)
                                print(result[0] + " is " + result[1])
                                return result
                        elif self.subtype == "Sequence":
                                result = self.sequence(blackboard, a, b)
                                print(result[0] + " is " + result[1])
                                return result
                        else:
                                result = self.selection(blackboard, a, b)
                                print(result[0] + " is " + result[1])
                                return result
                elif self.element == "Decorator":
                        if self.subtype == "Until Fail":
                                result = self.sequence(blackboard, a, b)
                                while result[1] != "Fail":
                                        result = self.sequence(blackboard, a, b)
                                return result
                else:
                        result = self.action(blackboard, a, b)
                        print(result[0] + " is " + result[1])
                        return result
        
        # complete by priority; fails if all children fail; children must be
        # loaded by priority
        def priority(self, blackboard, a, b):
                result = ["PRIORITY", "Fail"]
                for i in self.children:
                        temp = i.act(blackboard, a, b)
                        if temp[1] == "Running":
                                result = ["PRIORITY", "Running"]
                        elif result[1] != "Running" and temp[1] == "Success":
                                result = ["PRIORITY", "Success"]
                return result

        # complete left to right; fails if one child fails
        def sequence(self, blackboard, a, b):
                result = ["SEQUENCE", "Success"]
                for i in self.children:
                        temp = i.act(blackboard, a, b)
                        if temp[1] == "Fail":
                                return ["SEQUENCE", "Fail"]
                        elif temp[1] == "Running":
                                result = ["SEQUENCE", "Running"]
                return result

        # complete left to right; fails if all children fail
        def selection(self, blackboard, a, b):
                result = ["SELECTION", "Fail"]
                for i in self.children:
                        temp = i.act(blackboard, a, b)
                        if temp[1] == "Running":
                                result = ["SELECTION", "Running"]
                        elif result[1] != "Running" and temp[1] == "Success":
                                result = ["SELECTION", "Success"]
                return result


# Functions for testing
def testing_function1(b, c, d):
        return "Fail"

def testing_function2(b, c, d):
        return "Running"

def testing_function3(b, c, d):
        return "Success"

        
# Main for testing
if __name__ == '__main__':
        tester1 = HoN_BTree("Composite", "Priority", None)
        tester2 = HoN_BTree("Task", None, testing_function3)
        tester1.addChildren(tester2)
        tester3 = HoN_BTree("Task", None, testing_function3)
        tester1.addChildren(tester3)
        tester4 = HoN_BTree("Task", None, testing_function3)
        tester1.addChildren(tester4)
        print(tester1.act(None, None, None))
