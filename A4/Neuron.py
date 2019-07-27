"""
        James Garijo-Garde
        4/18/2019

        Comp131 Homework 4

        This class is a neuron for the ANN needed for Assignment 4. Each neuron
        takes two inputs and uses a sigmoid activation to determine its output.
"""

import math

class Neuron:

        # Initializes each Neuron with two weights for two inputs.
        def __init__(self, w1, w2):
                self.weight1 = w1
                self.weight2 = w2
        
        # Calculates the net potential.
        def potential(self, x1, x2):
                potential = (x1 * self.weight1) + (x2 * self.weight2)
                return potential
        
        # Output function for the Neuron class. Takes in total potential and
        # returns the output value.
        def O(self, p):
                output = 1 / (1 + math.exp(-p))
                return output
        
        # Derivative of the output function. Takes in total potential and
        # returns an output value.
        def Oprime(self, p):
                o = self.O(p)
                output = o * (1 - o)
                return output

        # Fire function that takes in input and runs activation function
        def fire(self, x1, x2):
                p = self.potential(x1, x2)
                return self.O(p)
        
        # Calculates the error of the neuron
        def error(self, x1, x2, expected):
                p = self.potential(x1, x2)
                err = self.Oprime(p) * (expected - self.O(p))
                return err


# Main for testing
if __name__ == '__main__':
        print("TEST OF NEURON CLASS\n")
        n1 = Neuron(0.5, 0.25)
        print("Weights:")
        print(n1.get_weight1)
        print(n1.get_weight2)
        print("Potential on 2, 4 input:")
        print(n1.potential(2, 4))
        print("Output on 2, 4 input:")
        print(n1.fire(2, 4))
        print("Output Error when expected value is 3:")
        print(n1.error(2, 4, 3))
