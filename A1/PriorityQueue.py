"""
    James Garijo-Garde
    2/11/2019

    Comp131 Homework 1

    This code is based on code from GeeksforGeeks. I have modified it to store
    both a value and a cost and to return the item with the minimum cost when
    popping.
"""

class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty; returns True or False
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    # for inserting an element in the queue 
    def push(self, cost, data):
        element = (cost, data)
        self.queue.append(element) 
  
    # for popping an element based on Priority 
    def pop(self): 
        try: 
            min = 0
            for i in range(len(self.queue)): 
                if self.queue[i][0] < self.queue[min][0]: 
                    min = i
            item = self.queue[min] 
            del self.queue[min] 
            return item
        except IndexError: 
            print() 
            exit() 