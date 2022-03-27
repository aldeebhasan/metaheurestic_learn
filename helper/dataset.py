import os
import numpy as np

cwd = os.getcwd()


def readIris():
    file = "iris"
    converters = {
        b'Iris-setosa': 0,
        b'Iris-versicolor': 1,
        b'Iris-virginica': 2,
    }

    def convert(s):
        return converters[s]

    data = np.genfromtxt(
        open("datasets/" + file + ".csv", "rb"),
        dtype=float, delimiter=",",
        skip_header=1,
        converters={4: convert}
    )

    data, label = convertAndReturn(data)

    ranges = list()
    for i in range(data.shape[1]):
        ranges.append([np.floor(min(data[:, i])), np.ceil(max(data[:, i]))])

    return data, label, ranges


def readCMC():
    file = "cmc"

    data = np.genfromtxt(
        open("datasets/" + file + ".csv", "rb"),
        dtype=float, delimiter=",",
        skip_header=1,
    )
    data, label = convertAndReturn(data)

    ranges = list()
    for i in range(data.shape[1]):
        ranges.append([np.floor(min(data[:, i])-1),
                      np.ceil(max(data[:, i])+1)])

    return data, label,ranges


def readGlass():
    file = "glass"

    data = np.genfromtxt(
        open("datasets/" + file + ".csv", "rb"),
        dtype=float, delimiter=",",
        skip_header=1,
    )
    data, label = convertAndReturn(data)

    ranges = list()
    for i in range(data.shape[1]):
        ranges.append([np.floor(min(data[:, i])-1),
                      np.ceil(max(data[:, i])+1)])

    return data, label, ranges


def readCancer():
    file = "cancer"

    data = np.genfromtxt(
        open("datasets/" + file + ".csv", "rb"),
        dtype=float, delimiter=",",
        skip_header=1,
    )

    data, label = convertAndReturn(data)

    ranges = list()
    for i in range(data.shape[1]):
        ranges.append([np.floor(min(data[:, i])), np.ceil(max(data[:, i]))])

    return data,label, ranges


def readWine():
    file = "wine"

    data = np.genfromtxt(
        open("datasets/" + file + ".csv", "rb"),
        dtype=float, delimiter=",",
        skip_header=1,
    )
    data, label = convertAndReturn(data)

    ranges = list()
    for i in range(data.shape[1]):
        ranges.append([np.floor(min(data[:, i])-1),
                      np.ceil(max(data[:, i])+1)])

    return data,label,ranges


def convertAndReturn(data):
    c_data = []
    for i in range(data.shape[0]):
        c_data.append(list(j for j in data[i]))

    return split(np.array(c_data))


def split(data):
    return data[:, :-1], data[:, -1]
