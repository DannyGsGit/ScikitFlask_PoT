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
#### Define perceptron class ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Perceptron(object):
    
    #### Perceptron classifier ####
    # 
    # PARAMETERS:
    # eta- (float) learning rate
    # n_iter- (int) number of iterations to pass
    #
    # ATTRIBUTES:
    # w_- post-fit weights
    # errors_- fitting error per epoch
    
    def __init__(self, eta = 0.01, n_iter = 10):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        # Fits training data
        #
        # PARAMETERS:
        # X- the training data array of n-records in rows and n-features in columns
        # y- target labels, list
        #
        # RETURNS:
        # self- object
        
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
   
    
    def net_input(self, X):
        # Calculate net input
        return np.dot(X, self.w_[1:]) + self.w_[0]
  
    def predict(self, X):
        # Return class label after unit step
        return np.where(self.net_input(X) >= 0.0, 1, -1)


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



