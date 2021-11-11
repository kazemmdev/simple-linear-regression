import numpy as np
from numpy.lib.function_base import average


def featureScale(X):
    average = calAverage(X)
    variance = calVariance(X)
    return (X - average) / np.where(variance != 0, variance, 1)


def calAverage(X):
    m = np.shape(X)[0]
    return sum(X) / m


def calVariance(X):
    m = np.shape(X)[0]
    return np.sqrt(sum((X - calAverage(X))**2) / m)


def maxmin(X):
    return np.max(X) - np.min(X)
