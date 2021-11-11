import numpy as np


def makePolinominal(X, d=1, AddBias=False):

    if(AddBias):
        m, = np.shape(X)
        pX = np.c_[np.ones(m), X]
    else:
        pX = X

    if(d == 1):
        return pX

    for i in range(2, d+1):
        pX = np.c_[pX, np.power(X, i)]

    return pX
