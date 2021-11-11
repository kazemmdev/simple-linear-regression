import numpy as np
from utils.computeCost import computeCost
from utils.computeGradient import computeGradient
from utils.computePoly import makePolinominal
from utils.computeFeatureScale import featureScale
from utils.plotData import plot


def gradient(X, y, degree=1, alpha=0.01, loop=1000, hasReport=True, hasPlot=True, ):

    XX = getReadyData(X, degree)

    theta = np.zeros(degree + 1)

    j_histories = np.zeros(loop)

    for i in range(loop):

        theta = theta - alpha * computeGradient(XX, y, theta)

        j_histories[i] = computeCost(XX, y, theta)

        if (hasReport & i % 200 == 0):
            print("cost = " + str(j_histories[i]))

    if(hasPlot):
        plot(X, y, theta)

    return theta


def getReadyData(X, d):

    m, = np.shape(X)

    data = makePolinominal(X, d)

    data = featureScale(data)

    return np.c_[np.ones(m), data]
