import numpy as np


class Distance:

    @staticmethod
    def euclidian_distance(item_1, item_2):
        return np.sqrt(np.sum((item_1 - item_2) ** 2))

    @staticmethod
    def hamming_distance(item_1, item_2):
        return np.sum(np.abs(item_1 - item_2))/len(item_1)

    @staticmethod
    def manhattan_distance(item_1, item_2):
        return np.sum(np.abs(item_1 - item_2))

    @staticmethod
    def minkowski_distance(item_1, item_2, p):
        return np.sum((item_1 - item_2) ** p)**(1/p)
