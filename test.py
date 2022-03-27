import numpy as np
import helper.dataset as dataset
from algorithms.blackhole_algorithm import BlackHole
from algorithms.genetic_algorithm import GeneticAlgorithm

# in this test example we are using the implemeted
# metaheurestic algorithns to perform data clustering.
# the dataset helper will allow us to upload the targeted dataset
# then the algorithm will try to find the best clusters' centers. 
# the fitness function is the: 
# `intra cluster sum distance`: the sum of  distance between the input data sample and the closest cluster center
################

#read the input data samples
X, Y,  ranges = dataset.readGlass()
#each lable will be attached to a cluster, so we need k cluster
K = len(set(Y))
ranges = ranges * K

def euclids_distance(items, centers):
    return np.array([np.sqrt(np.sum((items - center) ** 2, axis=1)) for center in centers])


def fitness(individual):
    centers = individual.reshape((K, -1))
    distance = euclids_distance(X, centers)
    return sum(np.min(distance, axis=0))



def error(individual):
    correct_tr = np.random.randint(1,len(X))
    return ((len(X) - correct_tr) / len(X)) * 100



optimizer = BlackHole(population=100, iterations=150,
                      boundaries=ranges, epochs=2)
# optimizer = GeneticAlgorithm(population=100, iterations=150,
#                              boundaries=ranges, epochs=2)
optimizer.set_fitness_function(fitness)
optimizer.set_error_function(error)
statistics = optimizer.run(verbose=True)
optimizer.show_fitness_plot()
optimizer.show_error_plot()
print("Best is: ",statistics['best'])
print("Worst is: ",statistics['worst'])
print("Average is: ",statistics['avg'])
print("Error is: ",statistics['error'])
