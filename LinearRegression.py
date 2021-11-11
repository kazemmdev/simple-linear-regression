import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils.gradientDescent import gradient

dataset = pd.read_csv("dataset/test.csv")

array = dataset.values

X = array[:, 0]
y = array[:, 1]

# plt.plot(X,y, ".")
# plt.show()

gradient(X, y, 0.001)
