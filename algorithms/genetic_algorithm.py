
import random
from core.base_algorithm import BaseAlgorithm
import numpy as np


class GeneticAlgorithm(BaseAlgorithm):

    crossover_rate = 0.8
    mutation_rate = 0.2
    tournement_size = 4

    def __init__(self, population=100, iterations=100, boundaries=[], epochs=1, crossover_rate=0.8, mutation_rate=0.2):
        super().__init__(population, iterations, boundaries, epochs)
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def update_individual(self, individual):
        if (np.random.rand() < self.crossover_rate and
                not np.array_equal(self.best_individual(), individual)):
            individual = self.mate()
        return individual

    #--------------------------
    #Algorithm custom functions
    #--------------------------
    def tournement_selection(self):
        best_fitness = self.get_fitness(self.worst_index)
        best_individual = self.worst_individual()
        for _ in range(self.tournement_size):
            rand = np.random.randint(0, self.population)
            if self.get_fitness(rand) < best_fitness:
                best_fitness = self.get_fitness(rand)
                best_individual = self.get_individual(rand)

        return best_individual

    def crossover(self, parent_a, parent_b):
        crossover_point = np.random.randint(2 * self.get_individual_length())
        if crossover_point >= self.get_individual_length():
            crossover_point -= self.get_individual_length()
            parent_a, parent_b = parent_b, parent_a

        return np.concatenate([parent_a[0:crossover_point], parent_b[crossover_point:]])

    def mutation(self, item):
        for i in range(len(item)):
            if np.random.rand() < self.mutation_rate:
                item[i] = np.random.uniform(
                    self.boundaries[i][0], self.boundaries[i][1]
                )
        return item

    def mate(self):
        parent_a = self.tournement_selection()
        parent_b = self.tournement_selection()
        new_chromosome = self.crossover(parent_a, parent_b)
        return self.mutation(new_chromosome)


