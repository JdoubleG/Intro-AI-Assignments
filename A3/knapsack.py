"""
        James Garijo-Garde
        3/26/2019

        Comp131 Homework 3

        Solves the knapsack problem using a genetic algorithm approach.
"""

import random
import copy

# an initial list of possible boxes
boxes = []
boxes.append((1, 20, 6))
boxes.append((2, 30, 5))
boxes.append((3, 60, 8))
boxes.append((4, 90, 7))
boxes.append((5, 50, 6))
boxes.append((6, 70, 9))
boxes.append((7, 30, 4))

# Sets up the initial population of possible combinations
def setup():
        population = []
        # sets up the solo items
        population.append([(1, 20, 6)])
        population.append([(2, 30, 5)])
        population.append([(3, 60, 8)])
        population.append([(4, 90, 7)])
        population.append([(5, 50, 6)])
        population.append([(6, 70, 9)])
        population.append([(7, 30, 4)])
        """  Intended for debugging
        # sets up the doubles
        population.append([(1, 20, 6), (2, 30, 5)])
        population.append([(1, 20, 6), (3, 60, 8)])
        population.append([(1, 20, 6), (4, 90, 7)])
        population.append([(1, 20, 6), (5, 50, 6)])
        population.append([(1, 20, 6), (6, 70, 9)])
        population.append([(1, 20, 6), (7, 30, 4)])
        population.append([(2, 30, 5), (3, 60, 8)])
        population.append([(2, 30, 5), (4, 90, 7)])
        population.append([(2, 30, 5), (5, 50, 6)])
        population.append([(2, 30, 5), (6, 70, 9)])
        population.append([(2, 30, 5), (7, 30, 4)])
        population.append([(3, 60, 8), (5, 50, 6)])
        population.append([(3, 60, 8), (7, 30, 4)])
        population.append([(4, 90, 7), (7, 30, 4)])
        population.append([(5, 50, 6), (6, 70, 9)])
        population.append([(5, 50, 6), (7, 30, 4)])
        population.append([(6, 70, 9), (7, 30, 4)])
        # sets up the tripples
        population.append([(1, 20, 6), (2, 30, 5), (3, 60, 8)])
        population.append([(1, 20, 6), (2, 30, 5), (6, 70, 9)])
        population.append([(1, 20, 6), (3, 60, 8), (7, 30, 4)])
        population.append([(1, 20, 6), (5, 50, 6), (7, 30, 4)])
        population.append([(1, 20, 6), (6, 70, 9), (7, 30, 4)])
        population.append([(2, 30, 5), (3, 60, 8), (7, 30, 4)])
        population.append([(2, 30, 5), (5, 50, 6), (7, 30, 4)])
        """
        print("Initial Population:\n")
        for i in population:
                print(i)
        print("\n")
        return population

# facilitates the solution of the knapsack problem
def solver(pop, count):
        # establishes a new population pop2
        pop2 = []
        pop_size = len(pop)
        # keeping best
        for i in range(pop_size - (pop_size/2)):
                bestIndex = 0
                bestScore = 0
                for j in range(len(pop)):
                        if score(pop[j]) > bestScore:
                                bestScore = score(pop[j])
                                bestIndex = j
                if count == 10:
                        print("10 TURN LIMIT REACHED! Returning current best...")
                        return pop[bestIndex]
                else:
                        pop2.append(pop[bestIndex])
                        del pop[bestIndex]
        print("1st Half New Population:")
        for i in pop2:
                print(i)
        print()
        # reproduction
        while len(pop2) < pop_size:
                a = 0
                b = 0
                while a == b:
                        a = random.randint(0, len(pop2)-1)
                        b = random.randint(0, len(pop2)-1)
                print("Crossing over " + str(pop2[a]) + " with " + str(pop2[b]) + " !")
                if len(pop2[a]) > 1 and len(pop2[b]) > 1:
                        c = crossover(copy.deepcopy(pop2[a]), copy.deepcopy(pop2[b]))
                else:
                        c = copy.deepcopy(pop2[a])
                print(str(c))
                # mutation
                rand_value = random.randint(1, 8)
                if rand_value == 1:
                        print("Mutating (add) " + str(c) + " ...")
                        c = mutate_add(c)
                        print("... to " + str(c) + " !")
                elif rand_value == 2:
                        print("Mutating (swap) " + str(c) + " ...")
                        c = mutate_swap(c)
                        print("... to " + str(c) + " !")
                # fitness check
                c.sort()
                if score(c) == 20:
                        print("SUCCESS\n")
                        print("OPTIMAL ANSWER FOUND")
                        return c
                unique = True
                for i in pop2:
                        if i == c:
                                unique = False
                                print("Crossover already exists in population! Trying again...")
                if unique == True:
                        print("SUCCESS\n")
                        pop2.append(c)
        # repeat if no elements in pop2 are totally fit
        print("New Population:")
        for i in pop2:
                print(i)
        print("\n")
        return solver(pop2, count+1)

# genetic algorithm mutation function; adds an additional box
def mutate_add(x):
        y = copy.deepcopy(x)
        contents = set()
        for i in x:
                contents.add(i[0]-1)
        while True:
                mutation = random.randint(0, 6)
                while mutation in contents:
                        mutation = random.randint(0, 6)
                x.append(boxes[mutation])
                if weight_check(x):
                        return x
                else:
                        x = copy.deepcopy(y)
                        contents.add(mutation)
                        if contents & {0, 1, 2, 3, 4, 5, 6} == {0, 1, 2, 3, 4, 5, 6}:
                                return x

# genetic algorithm mutation function; swaps a box
def mutate_swap(x):
        y = copy.deepcopy(x)
        contents = set()
        attempts = set()
        for i in x:
                contents.add(i[0]-1)
        while True:
                mutation = random.randint(0, 6)
                while mutation in contents or mutation in attempts:
                        mutation = random.randint(0, 6)
                toSwap = random.randint(0, len(x)-1)
                x[toSwap] = boxes[mutation]
                if weight_check(x):
                        return x
                else:
                        x = copy.deepcopy(y)
                        attempts.add(mutation)
                        if (contents | attempts) & {0, 1, 2, 3, 4, 5, 6} == {0, 1, 2, 3, 4, 5, 6}:
                                return x

# genetic algorithm reproduction function; swaps a box in one for another
def crossover(x, y):
        z = copy.deepcopy(x)
        contentsX = set()
        contentsY = set()
        attempts = set()
        for i in x:
                contentsX.add(i[0]-1)
        for i in y:
                contentsY.add(i[0]-1)
        while True:
                mutation = random.randint(0, 6)
                while mutation in contentsX or mutation in attempts:
                        mutation = random.randint(0, 6)
                toSwap = random.randint(0, len(x)-1)
                # print("toSwap: " + str(toSwap) + " ;  mutation: " + str(mutation) + str(boxes))
                x[toSwap] = boxes[mutation]
                if weight_check(x):
                        return x
                else:
                        x = copy.deepcopy(z)
                        attempts.add(mutation)
                        if (contentsX | attempts) & {0, 1, 2, 3, 4, 5, 6} == {0, 1, 2, 3, 4, 5, 6}:
                                survivor = random.randint(1, 3)
                                if survivor == 1:
                                        return x
                                else:
                                        return y

# calculates the score of the combination
def score(x):
        score = 0
        for i in x:
                score = score + i[2]
        return score

# checks to make sure the weight constraint of 120 is satisfied
def weight_check(x):
        weight = 0
        for i in x:
                weight = weight + i[1]
        if weight <= 120:
                return True
        else:
                return False


# Runs the program if it is invoked in standalone.
if __name__ == '__main__':
        print("Knapsack Problem: Solved with Genetic Algorithm\n\n")
        answer = solver(setup(), 0)
        print("\n\nSolution: ")
        # parses answer to list only numbers
        # for i in answer:
        #         print(str(i[0]) + " ")
        print(str(answer))
