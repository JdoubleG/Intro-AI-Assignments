"""
        James Garijo-Garde
        4/18/2019

        Comp131 Homework 4

        The Artificial Neural Network used to sort the iris flowers.
"""

import math
import random
import copy
from Neuron import Neuron

# acceptable error threshold
threshold = 2

# training set
training_set = []
training_set.append((5.1, 3.5, 1.4, 0.2, "Iris-setosa"))
training_set.append((4.9, 3.0, 1.4, 0.2, "Iris-setosa"))
training_set.append((4.7, 3.2, 1.3, 0.2, "Iris-setosa"))
training_set.append((4.6, 3.1, 1.5, 0.2, "Iris-setosa"))
training_set.append((5.4, 3.9, 1.7, 0.4, "Iris-setosa"))
training_set.append((4.6, 3.4, 1.4, 0.3, "Iris-setosa"))
training_set.append((5.0, 3.4, 1.5, 0.2, "Iris-setosa"))
training_set.append((4.4, 2.9, 1.4, 0.2, "Iris-setosa"))
training_set.append((5.4, 3.7, 1.5, 0.2, "Iris-setosa"))
training_set.append((4.8, 3.4, 1.6, 0.2, "Iris-setosa"))
training_set.append((4.3, 3.0, 1.1, 0.1, "Iris-setosa"))
training_set.append((5.8, 4.0, 1.2, 0.2, "Iris-setosa"))
training_set.append((5.4, 3.9, 1.3, 0.4, "Iris-setosa"))
training_set.append((5.7, 3.8, 1.7, 0.3, "Iris-setosa"))
training_set.append((5.1, 3.8, 1.5, 0.3, "Iris-setosa"))
training_set.append((5.1, 3.7, 1.5, 0.4, "Iris-setosa"))
training_set.append((4.8, 3.4, 1.9, 0.2, "Iris-setosa"))
training_set.append((5.2, 3.5, 1.5, 0.2, "Iris-setosa"))
training_set.append((4.8, 3.1, 1.6, 0.2, "Iris-setosa"))
training_set.append((5.4, 3.4, 1.5, 0.4, "Iris-setosa"))
training_set.append((4.9, 3.1, 1.5, 0.1, "Iris-setosa"))
training_set.append((4.9, 3.1, 1.5, 0.1, "Iris-setosa"))
training_set.append((4.4, 3.0, 1.3, 0.2, "Iris-setosa"))
training_set.append((5.1, 3.4, 1.5, 0.2, "Iris-setosa"))
training_set.append((4.4, 3.2, 1.3, 0.2, "Iris-setosa"))
training_set.append((5.0, 3.5, 1.6, 0.6, "Iris-setosa"))
training_set.append((4.8, 3.0, 1.4, 0.3, "Iris-setosa"))
training_set.append((5.1, 3.8, 1.6, 0.2, "Iris-setosa"))
training_set.append((4.6, 3.2, 1.4, 0.2, "Iris-setosa"))
training_set.append((5.3, 3.7, 1.5, 0.2, "Iris-setosa"))
training_set.append((7.0, 3.2, 4.7, 1.4, "Iris-versicolor"))
training_set.append((6.4, 3.2, 4.5, 1.5, "Iris-versicolor"))
training_set.append((6.9, 3.1, 4.9, 1.5, "Iris-versicolor"))
training_set.append((5.5, 2.3, 4.0, 1.3, "Iris-versicolor"))
training_set.append((5.7, 2.8, 4.5, 1.3, "Iris-versicolor"))
training_set.append((6.3, 3.3, 4.7, 1.6, "Iris-versicolor"))
training_set.append((4.9, 2.4, 3.3, 1.0, "Iris-versicolor"))
training_set.append((6.6, 2.9, 4.6, 1.3, "Iris-versicolor"))
training_set.append((5.0, 2.0, 3.5, 1.0, "Iris-versicolor"))
training_set.append((5.9, 3.0, 4.2, 1.5, "Iris-versicolor"))
training_set.append((6.1, 2.9, 4.7, 1.4, "Iris-versicolor"))
training_set.append((5.6, 3.0, 4.5, 1.5, "Iris-versicolor"))
training_set.append((6.2, 2.2, 4.5, 1.5, "Iris-versicolor"))
training_set.append((5.6, 2.5, 3.9, 1.1, "Iris-versicolor"))
training_set.append((6.1, 2.8, 4.0, 1.3, "Iris-versicolor"))
training_set.append((6.4, 2.9, 4.3, 1.3, "Iris-versicolor"))
training_set.append((6.8, 2.8, 4.8, 1.4, "Iris-versicolor"))
training_set.append((6.7, 3.0, 5.0, 1.7, "Iris-versicolor"))
training_set.append((5.5, 2.4, 3.8, 1.1, "Iris-versicolor"))
training_set.append((5.5, 2.4, 3.7, 1.0, "Iris-versicolor"))
training_set.append((5.4, 3.0, 4.5, 1.5, "Iris-versicolor"))
training_set.append((6.3, 2.3, 4.4, 1.3, "Iris-versicolor"))
training_set.append((5.6, 3.0, 4.1, 1.3, "Iris-versicolor"))
training_set.append((5.5, 2.5, 4.0, 1.3, "Iris-versicolor"))
training_set.append((6.1, 3.0, 4.6, 1.4, "Iris-versicolor"))
training_set.append((5.8, 2.6, 4.0, 1.2, "Iris-versicolor"))
training_set.append((5.7, 3.0, 4.2, 1.2, "Iris-versicolor"))
training_set.append((5.7, 2.9, 4.2, 1.3, "Iris-versicolor"))
training_set.append((6.2, 2.9, 4.3, 1.3, "Iris-versicolor"))
training_set.append((5.1, 2.5, 3.0, 1.1, "Iris-versicolor"))
training_set.append((6.3, 3.3, 6.0, 2.5, "Iris-virginica"))
training_set.append((5.8, 2.7, 5.1, 1.9, "Iris-virginica"))
training_set.append((7.1, 3.0, 5.9, 2.1, "Iris-virginica"))
training_set.append((6.3, 2.9, 5.6, 1.8, "Iris-virginica"))
training_set.append((7.6, 3.0, 6.6, 2.1, "Iris-virginica"))
training_set.append((4.9, 2.5, 4.5, 1.7, "Iris-virginica"))
training_set.append((7.3, 2.9, 6.3, 1.8, "Iris-virginica"))
training_set.append((6.7, 2.5, 5.8, 1.8, "Iris-virginica"))
training_set.append((6.5, 3.2, 5.1, 2.0, "Iris-virginica"))
training_set.append((6.4, 2.7, 5.3, 1.9, "Iris-virginica"))
training_set.append((5.7, 2.5, 5.0, 2.0, "Iris-virginica"))
training_set.append((6.5, 3.0, 5.5, 1.8, "Iris-virginica"))
training_set.append((7.7, 2.6, 6.9, 2.3, "Iris-virginica"))
training_set.append((6.0, 2.2, 5.0, 1.5, "Iris-virginica"))
training_set.append((5.6, 2.8, 4.9, 2.0, "Iris-virginica"))
training_set.append((6.7, 3.3, 5.7, 2.1, "Iris-virginica"))
training_set.append((6.2, 2.8, 4.8, 1.8, "Iris-virginica"))
training_set.append((6.1, 3.0, 4.9, 1.8, "Iris-virginica"))
training_set.append((7.4, 2.8, 6.1, 1.9, "Iris-virginica"))
training_set.append((7.9, 3.8, 6.4, 2.0, "Iris-virginica"))
training_set.append((6.1, 2.6, 5.6, 1.4, "Iris-virginica"))
training_set.append((6.4, 3.1, 5.5, 1.8, "Iris-virginica"))
training_set.append((6.0, 3.0, 4.8, 1.8, "Iris-virginica"))
training_set.append((6.9, 3.1, 5.4, 2.1, "Iris-virginica"))
training_set.append((5.8, 2.7, 5.1, 1.9, "Iris-virginica"))
training_set.append((6.8, 3.2, 5.9, 2.3, "Iris-virginica"))
training_set.append((6.7, 3.0, 5.2, 2.3, "Iris-virginica"))
training_set.append((6.3, 2.5, 5.0, 1.9, "Iris-virginica"))
training_set.append((6.5, 3.0, 5.2, 2.0, "Iris-virginica"))
training_set.append((6.2, 3.4, 5.4, 2.3, "Iris-virginica"))

# validation set
validation_set = []
validation_set.append((4.9, 3.1, 1.5, 0.1, "Iris-setosa"))
validation_set.append((5.2, 2.7, 3.9, 1.4, "Iris-versicolor"))
validation_set.append((7.2, 3.6, 6.1, 2.5, "Iris-virginica"))
validation_set.append((4.8, 3.0, 1.4, 0.1, "Iris-setosa"))
validation_set.append((6.0, 2.2, 4.0, 1.0, "Iris-versicolor"))
validation_set.append((6.8, 3.0, 5.5, 2.1, "Iris-virginica"))
validation_set.append((5.2, 4.1, 1.5, 0.1, "Iris-setosa"))
validation_set.append((5.8, 2.7, 3.9, 1.2, "Iris-versicolor"))
validation_set.append((6.4, 2.8, 5.6, 2.2, "Iris-virginica"))
validation_set.append((4.6, 3.6, 1.0, 0.2, "Iris-setosa"))
validation_set.append((6.3, 2.5, 4.9, 1.5, "Iris-versicolor"))
validation_set.append((7.7, 2.8, 6.7, 2.0, "Iris-virginica"))
validation_set.append((5.1, 3.3, 1.7, 0.5, "Iris-setosa"))
validation_set.append((6.1, 2.8, 4.7, 1.2, "Iris-versicolor"))
validation_set.append((6.3, 2.7, 4.9, 1.8, "Iris-virginica"))
validation_set.append((4.5, 2.3, 1.3, 0.3, "Iris-setosa"))
validation_set.append((5.0, 2.3, 3.3, 1.0, "Iris-versicolor"))
validation_set.append((6.9, 3.1, 5.1, 2.3, "Iris-virginica"))
validation_set.append((5.5, 4.2, 1.4, 0.2, "Iris-setosa"))
validation_set.append((6.0, 2.7, 5.1, 1.6, "Iris-versicolor"))
validation_set.append((6.3, 2.8, 5.1, 1.5, "Iris-virginica"))
validation_set.append((5.0, 3.3, 1.4, 0.2, "Iris-setosa"))
validation_set.append((5.7, 2.8, 4.1, 1.3, "Iris-versicolor"))
validation_set.append((5.9, 3.0, 5.1, 1.8, "Iris-virginica"))
validation_set.append((5.0, 3.6, 1.4, 0.2, "Iris-setosa"))
validation_set.append((5.6, 2.9, 3.6, 1.3, "Iris-versicolor"))
validation_set.append((5.8, 2.8, 5.1, 2.4, "Iris-virginica"))
validation_set.append((5.2, 3.4, 1.4, 0.2, "Iris-setosa"))
validation_set.append((6.0, 2.9, 4.5, 1.5, "Iris-versicolor"))
validation_set.append((6.4, 2.8, 5.6, 2.1, "Iris-virginica"))

# testing set
testing_set = []
testing_set.append((5.5, 3.5, 1.3, 0.2, "Iris-setosa"))
testing_set.append((6.7, 3.1, 4.7, 1.5, "Iris-versicolor"))
testing_set.append((6.3, 3.4, 5.6, 2.4, "Iris-virginica"))
testing_set.append((5.0, 3.2, 1.2, 0.2, "Iris-setosa"))
testing_set.append((6.0, 3.4, 4.5, 1.6, "Iris-versicolor"))
testing_set.append((7.7, 3.0, 6.1, 2.3, "Iris-virginica"))
testing_set.append((5.1, 3.5, 1.4, 0.3, "Iris-setosa"))
testing_set.append((5.8, 2.7, 4.1, 1.0, "Iris-versicolor"))
testing_set.append((7.7, 3.8, 6.7, 2.2, "Iris-virginica"))
testing_set.append((5.1, 3.8, 1.9, 0.4, "Iris-setosa"))
testing_set.append((5.6, 2.7, 4.2, 1.3, "Iris-versicolor"))
testing_set.append((6.7, 3.3, 5.7, 2.5, "Iris-virginica"))
testing_set.append((5.0, 3.0, 1.6, 0.2, "Iris-setosa"))
testing_set.append((6.6, 3.0, 4.4, 1.4, "Iris-versicolor"))
testing_set.append((7.2, 3.2, 6.0, 1.8, "Iris-virginica"))
testing_set.append((4.7, 3.2, 1.6, 0.2, "Iris-setosa"))
testing_set.append((5.7, 2.6, 3.5, 1.0, "Iris-versicolor"))
testing_set.append((7.2, 3.0, 5.8, 1.6, "Iris-virginica"))
testing_set.append((5.4, 3.4, 1.7, 0.2, "Iris-setosa"))
testing_set.append((5.9, 3.2, 4.8, 1.8, "Iris-versicolor"))
testing_set.append((6.9, 3.2, 5.7, 2.3, "Iris-virginica"))
testing_set.append((5.0, 3.5, 1.3, 0.3, "Iris-setosa"))
testing_set.append((5.5, 2.6, 4.4, 1.2, "Iris-versicolor"))
testing_set.append((6.7, 3.1, 5.6, 2.4, "Iris-virginica"))
testing_set.append((5.7, 4.4, 1.5, 0.4, "Iris-setosa"))
testing_set.append((6.7, 3.1, 4.4, 1.4, "Iris-versicolor"))
testing_set.append((6.4, 3.2, 5.3, 2.3, "Iris-virginica"))
testing_set.append((5.0, 3.4, 1.6, 0.4, "Iris-setosa"))
testing_set.append((6.5, 2.8, 4.6, 1.5, "Iris-versicolor"))
testing_set.append((6.5, 3.0, 5.8, 2.2, "Iris-virginica"))


# Creates a list of the neurons in the neural network
def build_network():
        neurons = []
        w01 = random.uniform(-1/8, 1/8)
        w02 = random.uniform(-1/8, 1/8)
        n0 = Neuron(w01, w02)
        neurons.append(n0)
        w11 = random.uniform(-1/8, 1/8)
        w12 = random.uniform(-1/8, 1/8)
        n1 = Neuron(w11, w12)
        neurons.append(n1)
        w21 = random.uniform(-1/8, 1/8)
        w22 = random.uniform(-1/8, 1/8)
        n2 = Neuron(w21, w22)
        neurons.append(n2)
        return neurons

# Normalizes the Sepal Length to +/- 6
def normSepalL(x):
        return ((2 * (x - 4.3)) / (7.9 - 4.3)) - 1

# Normalizes the Sepal Width to +/- 6
def normSepalW(x):
        return ((2 * (x - 2.0)) / (4.4 - 2.0)) - 1

# Normalizes the Petal Length to +/- 6
def normPetalL(x):
        return ((2 * (x - 1.0)) / (6.9 - 1.0)) - 1

# Normalizes the Petal Length to +/- 6
def normPetalW(x):
        return ((2 * (x - 0.1)) / (2.5 - 0.1)) - 1

# trains the ANN on the training set
def train(network):
        print("Training:")
        expected = 0
        setosa = 0
        versicolor = 0
        virginica = 0
        E = 0  # overall error
        for i in training_set:
                # forward propigate
                print("Forward Propigating...")
                o0 = network[0].fire(normSepalL(i[0]), normSepalW(i[1]))
                o1 = network[1].fire(normPetalL(i[2]), normPetalW(i[3]))
                o2 = network[2].fire(o0, o1)
                # backward propigate
                print("Backward Propigating...")
                n = 0.1  # learning rate
                # Iris Setosa is assigned the ID 0
                if i[4] == "Iris-setosa":
                        expected = 0
                        setosa = setosa + 1
                # Iris Versicolor is assigned the ID 1
                elif i[4] == "Iris-versicolor":
                        expected = 1
                        versicolor = versicolor + 1
                # Iris Virginica is assigned the ID 2
                elif i[4] == "Iris-virginica":
                        expected = 2
                        virginica = virginica + 1
                else:
                        print("\nERROR Incorrect Flower Type\n")
                        exit()
                e2 = network[2].error(o0, o1, expected)
                e0 = network[2].weight1 * e2  # contribution to error by n0
                e1 = network[2].weight2 * e2  # error by n1
                network[2].weight1 = network[2].weight1 + n * o0 * e2
                network[2].weight2 = network[2].weight2 + n * o1 * e2
                network[1].weight1 = network[1].weight1 + n * normPetalL(i[2]) * e1
                network[1].weight2 = network[1].weight2 + n * normPetalW(i[3]) * e1
                network[0].weight1 = network[0].weight1 + n * normSepalL(i[0]) * e0
                network[0].weight2 = network[0].weight2 + n * normSepalW(i[1]) * e0
                e = math.pow(expected - o2, 2)
                print("Expected: " + str(expected) + "  Recorded:  " + str(o2) + "  Error: " + str(e))
                E = E + e
        # calculate and return overall error
        E = 0.1 * E
        print("Training completed on " + str(setosa) + " Iris setosas, " + str(versicolor) + " Iris versicolors and " + str(virginica) + " Iris virginicas.")
        print("Overall Training Error:  " + str(E))
        return E

# validates the ANN on the validation set
def validate(network):
        print("Validating:")
        expected = 0
        E = 0  # overall error
        correct = 0
        for i in validation_set:
                # forward propigate
                o0 = network[0].fire(normSepalL(i[0]), normSepalW(i[1]))
                o1 = network[1].fire(normPetalL(i[2]), normPetalW(i[3]))
                o2 = network[2].fire(o0, o1)
                # backward propigate
                n = 0.1  # learning rate
                # Iris Setosa is assigned the ID 0
                if i[4] == "Iris-setosa":
                        expected = 0
                        if round(o2, 1) <= 0.6:
                                print("Iris setosa correctly identified!")
                                correct = correct + 1
                        else:
                                print("Iris setosa incorrectly not identified!")
                # Iris Versicolor is assigned the ID 1
                elif i[4] == "Iris-versicolor":
                        expected = 1
                        if round(o2, 1) >= .6 and round(o2, 2) <= 0.79:
                                print("Iris versicolor correctly identified!")
                                correct = correct + 1
                        else:
                                print("Iris versicolor incorrectly not identified!")
                # Iris Virginica is assigned the ID 2
                elif i[4] == "Iris-virginica":
                        expected = 2
                        if round(o2) >= 1:
                                print("Iris virginica correctly identified!")
                                correct = correct + 1
                        else:
                                print("Iris virginica incorrectly not identified!")
                else:
                        print("\nERROR Incorrect Flower Type\n")
                        exit()
                e2 = network[2].error(o0, o1, expected)
                e0 = network[2].weight1 * e2  # contribution to error by n0
                e1 = network[2].weight2 * e2  # error by n1
                network[2].weight1 = network[2].weight1 + n * o0 * e2
                network[2].weight2 = network[2].weight2 + n * o1 * e2
                network[1].weight1 = network[1].weight1 + n * normPetalL(i[2]) * e1
                network[1].weight2 = network[1].weight2 + n * normPetalW(i[3]) * e1
                network[0].weight1 = network[0].weight1 + n * normSepalL(i[0]) * e0
                network[0].weight2 = network[0].weight2 + n * normSepalW(i[1]) * e0
                E = E + math.pow(expected - o2, 2)
        # calculate and return overall error
        E = 0.1 * E
        print("Validation Error:  " + str(E))
        print("Number Correct:  " + str(correct) + "/30")
        return E

# Tests the ANN on the testing set
def test(network):
        print("Testing...")
        expected = 0
        E = 0  # overall error
        correct = 0
        for i in validation_set:
                # forward propigate
                o0 = network[0].fire(normSepalL(i[0]), normSepalW(i[1]))
                o1 = network[1].fire(normPetalL(i[2]), normPetalW(i[3]))
                o2 = network[2].fire(o0, o1)
                # checks error
                # Iris Setosa is assigned the ID 0
                if i[4] == "Iris-setosa":
                        expected = 0.6
                        if round(o2, 1) <= 0.6:
                                print("Iris setosa correctly identified!")
                                correct = correct + 1
                        else:
                                print("Iris setosa incorrectly not identified!")
                # Iris Versicolor is assigned the ID 1
                elif i[4] == "Iris-versicolor":
                        expected = 1
                        if round(o2, 1) >= .6 and round(o2, 2) <= 0.79:
                                print("Iris versicolor correctly identified!")
                                correct = correct + 1
                        else:
                                print("Iris versicolor incorrectly not identified!")
                # Iris Virginica is assigned the ID 2
                elif i[4] == "Iris-virginica":
                        expected = 2
                        # if round(o2, 2) >= .70:
                        if round(o2) >= 1:
                                print("Iris virginica correctly identified!")
                                correct = correct + 1
                        else:
                                print("Iris virginica incorrectly not identified!")
                else:
                        print("\nERROR Incorrect Flower Type\n")
                        exit()
                E = E + math.pow(expected - o2, 2)
        # calculate error
        E = 0.5 * E
        print("Test Error:  " + str(E))
        print("Number Correct:  " + str(correct) + "/30")
        return E

# Runs the ANN on a user's input
def run(network):
        cont = 'y'
        print("Please enter the following information:")
        while cont == 'y' or cont == 'Y':
                sepL = input("Sepal length: ")
                sepW = input("Sepal width:  ")
                petL = input("Petal length: ")
                petW = input("Petal width:  ")
                flower = classify((float(sepL), float(sepW),
                                   float(petL), float(petW)), network)
                print("The flower has been identified as " + flower + ".")
                loop = True
                cont = input("Would you like to classify another flower? y/n")
                if cont == 'n' or cont == 'N':
                        exit()

# Classifies a flower using the ANN
def classify(flower, network):
        o0 = network[0].fire(normSepalL(flower[0]), normSepalW(flower[1]))
        o1 = network[1].fire(normPetalL(flower[2]), normPetalW(flower[3]))
        o2 = network[2].fire(o0, o1)
        if round(o2, 1) <= 0.6:
                return "Iris setosa"
        elif round(o2, 1) >= .6 and round(o2, 2) <= .79:
                return "Iris versicolor"
        else:
                return "Iris virginica"

# sets up the ANN and facilitates training, validation, and testing.
def setup():
        cycle = 0
        build = True
        network = build_network()
        terror = 9999999999999999
        verror = 9999999999999999
        prevT = 0
        prevV = 0
        while build == True and cycle < 201:
                # train
                prevT = copy.deepcopy(terror)
                terror = train(network)
                # validate
                prevV = copy.deepcopy(verror)
                verror = validate(network)
                # check if done
                if terror > prevT or verror > prevV:
                         print("Training error has increased! Ending training...")
                         build = False
                if terror <= threshold or verror <= threshold:
                         print("Validation error has increased! Ending training...")
                         build = False
                cycle = cycle + 1
        test(network)
        cont = input("\nWould you like to run the ANN on custom input? y/n")
        while True:
                if cont == 'y' or cont == 'Y':
                        run(network)
                elif cont == 'n' or cont == 'N':
                        exit()
                else:
                        cont = input("\nWould you like to run the ANN on custom input? y/n")


# Main
if __name__ == '__main__':
        setup()
