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


