import numpy as np
import matplotlib.pyplot as plt


class BaseAlgorithm:
    population = 100
    iterations = 100
    boundaries = []
    verbose = False
    best_index = 0
    worst_index = 0
    error_func = None
    error_func_args = None
    fitness_func = None
    fitness_func_args = None
    epochs = 1
    epoch_fitness = list()
    epoch_error = list()

    def __init__(self, population=100, iterations=100, boundaries=[], epochs=1):
        self.population = population
        self.iterations = iterations
        self.boundaries = np.array(boundaries)
        self.epochs = epochs

    def get_individual_length(self):
        return len(self.boundaries)

    def initialization(self):
        self.individuals = np.random.uniform(
            self.boundaries[:, 0], self.boundaries[:, 1], size=(self.population, len(self.boundaries)))
        self.reevaluate_population()

    def after_initialization(self):
        # do anything here
        return

    def regenerate_individual(self, index):
        self.individuals[index] = np.random.uniform(
            self.boundaries[:, 0], self.boundaries[:, 1], size=(1, len(self.boundaries)))
        self.fitness[index] = self.call_fitness_func(self.individuals[index])

    def set_fitness_function(self, fitness, arguments=None):
        self.fitness_func = fitness
        self.fitness_func_args = arguments

    def call_fitness_func(self, individual):
        if self.fitness_func_args == None:
            return self.fitness_func(individual)
        else:
            return self.fitness_func(individual, self.fitness_func_args)

    def set_error_function(self, error, arguments=None):
        self.error_func = error
        self.error_func_args = arguments

    def call_error_func(self, individual):
        if self.error_func_args == None:
            return self.error_func(individual)
        else:
            return self.error_func(individual, self.error_func_args)

    def update(self, iteration):
        for i in range(0, len(self.individuals)):
            self.individuals[i] = self.update_individual(self.individuals[i])
            self.fitness[i] = self.call_fitness_func(self.individuals[i])
        self.reevaluate_population()

    def update_individual(self, individual):
        return individual

    def run_epoch(self):
        self.initialization()
        self.after_initialization()
        for iteration in range(0, self.iterations):
            self.before_update(iteration)
            self.update(iteration)
            self.after_update(iteration)
            if self.verbose:
                print("At iteration #{} \n *best individual: {} \n *worst individual{}"
                      .format(iteration, np.min(self.fitness), np.max(self.fitness)))
        return self.best_index

    def run(self, verbose=False):
        self.verbose = verbose
        for epoch in range(0, self.epochs):
            print("========\nEpoch #{}:  \n========\n".format(epoch))
            best_idx = self.run_epoch()
            self.epoch_fitness.append(self.get_fitness(best_idx))
            if not self.error_func == None:
                self.epoch_error.append(self.call_error_func(
                    self.get_individual(best_idx)))
            print("Best fitness is {}\nWorst fitness is {}\n".format(
                self.get_fitness(self.best_index), self.get_fitness(self.worst_index)))
        print("\n========================\n")
        return self.statistics()

    def before_update(self, iteration):
        # do anything here
        pass

    def after_update(self, iteration):
        # do anything here
        pass

    def reevaluate_population(self):
        self.fitness = np.array([self.call_fitness_func(x)
                                for x in self.individuals])
        self.best_index = np.argmin(self.fitness)
        self.worst_index = np.argmax(self.fitness)

    def best_individual(self):
        return self.individuals[self.best_index]

    def worst_individual(self):
        return self.individuals[self.worst_index]

    def get_fitness(self, index=None):
        if index == None:
            return self.fitness
        else:
            return self.fitness[index]

    def get_individual(self, index=None):
        if index == None:
            return self.individuals
        else:
            return self.individuals[index]

    def set_individual(self, index, new_individual):
        self.individuals[index] = new_individual

    def statistics(self):
        return {
            'best': np.min(self.epoch_fitness),
            'avg': np.mean(self.epoch_fitness),
            'worst': np.max(self.epoch_fitness),
            'std': np.std(self.epoch_fitness),
            'error': np.min(self.epoch_error) if len(self.epoch_error) > 0 else None,
        }

    def show_error_plot(self):
        if len(self.epoch_error) > 0:
            values = np.array(self.epoch_error)
            plt.plot(values, 'r')
            plt.title("Errors")
            plt.ylabel('Error')
            plt.xlabel('Epoch')
            plt.grid(True)
            plt.show()

    def show_fitness_plot(self):
        if len(self.epoch_fitness) > 0:
            values = np.array(self.epoch_fitness)
            plt.plot(values, 'g')
            plt.title("Fitnesses")
            plt.ylabel('Fitness')
            plt.xlabel('Epoch')
            plt.grid(True)
            plt.show()
