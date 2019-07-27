James Garijo-Garde
3/26/2019

Comp131 Homework 3

This is a solver of the knapsack problem using a genetic algorithm.

Problem Genome: list of boxes in the backpack.

Initial Genome: lists consisting of only one of each of the boxes.

Population size: 7

Maximum number of generations: 10

Fringe Operations:
        Crossover: swaps a randomly selected box in genome x with a randomly
                   selected box in genome y.
        Add Mutation: adds a random box to the list of boxes in the backpack.
        Swap Mutation: changes a random box in the genome to a different box.
        Fitness Check: if a genome has the best possible score (20), the program
                       will return that genome.

Additional notes: the best half of the population is kept each time while the
                  bottom half is swapped for new genomes generated using the
                  above fringe operations. Duplicates are not accepted and
                  overweight (above 120) genomes are automatically rejected.

How to run: type "python knapsack.py" into your command line. No user input is
            required: starting population is defined. The program will
            automatically return the current best after 10 generations if the
            best possible score is not found before then (this is the time
            limit).