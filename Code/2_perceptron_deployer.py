#~~~~~~~~~~~~~~~~~~~~~~~~
#### Import packages ####
#~~~~~~~~~~~~~~~~~~~~~~~~

import numpy as np
import matplotlib.pyplot as plt
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

iris_model.predict([6, 4])