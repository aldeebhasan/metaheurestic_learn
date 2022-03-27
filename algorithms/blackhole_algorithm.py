
from core.base_algorithm import BaseAlgorithm
import numpy as np
from helper.distance import Distance


class BlackHole(BaseAlgorithm):

    blackhole_radius = 0

    def after_initialization(self):
        self.setRadius()

    def update_individual(self, individual):
        current_best = self.best_individual()
        if np.array_equal(individual, current_best):
            return individual
        rand = np.random.rand()
        individual += rand * (current_best - individual)
        return individual

    def before_update(self,iteration):
        self.blackhole = self.best_individual()
        for index, item in enumerate(self.get_individual()):
            if np.array_equal(self.blackhole, item):
                continue
            distance = Distance.euclidian_distance(item, self.blackhole)
            if (distance <= self.blackhole_radius):
                self.regenerate_individual(index)

    def after_update(self,iteration):
        current_best = self.best_individual()
        if not np.array_equal(self.blackhole, current_best):
            self.blackhole = current_best
            self.setRadius()

    #--------------------------
    #Algorithm custom functions
    #--------------------------
    def setRadius(self):
        fbh = np.max(self.get_fitness())
        f = np.sum(self.get_fitness())
        self.blackhole_radius = fbh / f
    

