import numpy as np


def computeCost(X, y, theta):

    m = len(y)

    return sum((np.dot(X, theta) - y) ** 2) / (2 * m)
