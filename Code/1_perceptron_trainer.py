#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Sample Perceptron algorithm ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Uses code from Raschka, S. "Python Machine Learning" Packt Publishing. 2015.



#~~~~~~~~~~~~~~~~~~~~~~~~
#### Import packages ####
#~~~~~~~~~~~~~~~~~~~~~~~~

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Source perceptron class ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

exec(open("./Code/perceptron.py").read(), globals())



#~~~~~~~~~~~~~~~~~~~~~~
#### Get iris data ####
#~~~~~~~~~~~~~~~~~~~~~~

# Get iris dataset from USI repo
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header = None)
# Inspect the result
df.head()


# Extract 100 class labels (training split) and discretize the labels into 1, -1
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0, 2]].values

# Plot features for training set
plt.scatter(X[:50, 0], X[:50, 1], color = 'red', label = 'setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color = 'blue', label = 'versicolor')
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.legend(loc = 'upper left')
plt.show()




#~~~~~~~~~~~~~~~~~~~~~~~~~
#### Train Perceptron ####
#~~~~~~~~~~~~~~~~~~~~~~~~~

# Initiate the perceptron
ppn = Perceptron(eta = 0.1, n_iter = 10)

# Fit the perceptron to training data
ppn.fit(X, y)

# Plot training error by epoch
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker = 'o')
plt.xlabel('Epochs')
plt.ylabel('Error')
plt.show()




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Pickle Out Perceptron ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pickle
import os

# Define the model path and create the directory if it doesn't exist
dest = os.path.join('Code', 'Models')
if not os.path.exists(dest):
    os.makedirs(dest)

pickle.dump(ppn,
            open(os.path.join(dest, 'iris_perceptron.pkl'), 'wb'),
            protocol = 4)


