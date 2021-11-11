import numpy as np


def computeGradient(X, y, theta):

    m = len(y)

    return  np.dot(np.transpose(X), np.dot(X, theta) - y) / m
