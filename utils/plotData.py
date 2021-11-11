import numpy as np
import matplotlib.pyplot as plt
from utils.computePoly import makePolinominal
from utils.computeFeatureScale import featureScale


def plot(X, y, theta):
    fpx = featureScale(X)
    fpx_min = np.min(fpx)
    fpx_max = np.max(fpx)


    i = np.linspace(fpx_min, fpx_max, 100)
    pi = makePolinominal(i, len(theta) - 1, True)
  
    plt.plot(fpx, y, ".")
    plt.plot(i, np.dot(pi, theta))
    plt.show()
