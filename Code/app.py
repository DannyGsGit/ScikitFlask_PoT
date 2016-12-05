#~~~~~~~~~~~~~~~~~~~~~~~~
#### Import packages ####
#~~~~~~~~~~~~~~~~~~~~~~~~

## ML Dependencies
import numpy as np
import pandas as pd
import os
import pickle

## Webservice Dependencies
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Source perceptron class ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

exec(open("perceptron.py").read(), globals())


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Unpickle the models ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

iris_model = pickle.load(open(os.path.join('Models', 'iris_perceptron.pkl'), 'rb'))


#~~~~~~~~~~~~~~~~~~
#### App stuff ####
#~~~~~~~~~~~~~~~~~~

app = Flask(__name__)

## Define classify method to run the Iris Model on input
def classify(document):
    #label = {-1: 'Setosa', 1: 'Versicolor'}
    X = document
    X = str.split(X, ",")
    X = list(map(float, X))
    y = iris_model.predict(X)
    y = "setosa" if y > 0 else "versicolor"
    return y


#~~~~~~~~~~~~~~~~~~~~~
#### Flask Config ####
#~~~~~~~~~~~~~~~~~~~~~
class ModelInputForm(Form):
    flowerdimensions = TextAreaField('',
                                     [validators.DataRequired(),
                                     validators.length(min=3)])

@app.route('/')
def index():
    form = ModelInputForm(request.form)
    return render_template('flower_form.html', form = form)

@app.route('/results', methods = ['POST'])
def results():
    form = ModelInputForm(request.form)
    if request.method == 'POST' and form.validate():
        flower = request.form['flowerdimensions']
        y = classify(flower)
        return render_template('results.html',
                                content = flower,
                                prediction = y)
    return render_template('flower_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
