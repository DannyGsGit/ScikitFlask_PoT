#~~~~~~~~~~~~~~~~~~~~~~~~
#### Import packages ####
#~~~~~~~~~~~~~~~~~~~~~~~~

import numpy as np
import pandas as pd
import os
import pickle


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Source perceptron class ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

exec(open("./Code/perceptron.py").read(), globals())




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Unpickle the models ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

iris_model = pickle.load(open(os.path.join('Code', 'Models', 'iris_perceptron.pkl'), 'rb'))




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Run a prediction ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

document = "5,1"
X = str.split(document, ",")
X = list(map(float, X))
y = iris_model.predict(X)
