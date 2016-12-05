# Deploying a Flask Webservice

In this section, we deploy a trained machine learning model as a webservice using the Flask microframework.

## 1. Operationalizing a Model

*Describe pickling/unpickling process...*

## 2. Flask Framework

This section will build a simple web application to execute our Iris model. To begin, the following directory items are added to the project:
* `~/Code/3_perceptron_service.py` Contains Python code executing the model
* `~/Code/templates/IrisModelApp.html` The HTML front end for the application
* `~/Code/templates/_formhelpers.html` Input form elements
* `~/Code/templates/prediction.html` Page for returning result
* `~/Code/static/style.css` Stylesheet for HTML content

This application will include form inputs, for which we will include the following packages:
* `$ cd C:\Python35\Environments\Scripts`
* `$ activate`
* `(scikit_flask_env)$ pip install wtforms`
