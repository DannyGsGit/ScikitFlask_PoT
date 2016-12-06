# Deploying a Flask Webservice

In this section, we deploy a trained machine learning model as a webservice using the Flask microframework. The `~/Code` directory contains a directory tree for a sample application including the following assets:
* `~/Code/1_train_model.py` A Python script to train a random forest classifier for Iris flower species
* `~/Code/2_test_api.py` A Python script to test the API created by *app_api.py*
* `~/Code/app_api.py` Our API definition executing the iris random forest pickle
* `~/Code/Models/iris_rf_model.pkl` The pickled random forest classifier for iris species


## 1. Operationalizing a Model

In order to operationalize a model, we do not want to train the model before each prediction- the desired workflow is to train a model and save the trained object as a file to be re-used. In Python, this is called *serialization* or *pickling*.

Please refer to `~/Code/1_train_model.py` for an example in which we train a model, then pickle the trained model using `pickle.dump()`.

Subsequently, a pickle can be brought into a new session using `pickle.load()`. Note that depending on the object that was pickled, the class definition of the object may also need to be imported to establish methods like *predict*.


## 2. Flask API

Our goal is to wrap an API around the Iris classification model we pickled in `~/Code/1_train_model.py`. The API is scoped in the `~/Code/app_api.py` script, where we define a Flask service.

After importing all required dependencies and unpickling the classification model, we define the scope of the API with the following code chunks.

First, we create an instance of the Flask class called *app*
```
app = Flask(__name__)
```

Next, we use the *route()* decorator to build the URLs triggering API functionality. This means we might have multiple routes defined in an API- for example, we may include a */predict* route for predictions and a */log* route to extract a log of prior predictions. In this case, we define a single route called */api* along with it's prediction function. After accepting a *POST* request, */api* will get new data as a JSON object, run a prediction from the unpickled model and returns the prediction result.
```
@app.route('/api', methods=['POST'])
def make_predict():
    #all kinds of error checking should go here
    data = request.get_json(force=True)
    #convert our json to a numpy array
    predict_request = [data['sl'],data['sw'],data['pl'], data['pw']]
    predict_request = np.array(predict_request).reshape(1,-1)
    #np array goes into random forest, prediction comes out
    y_hat = my_random_forest.predict(predict_request)
    #return our prediction
    output = {'y_hat': int(y_hat[0])}
    print(output)
    return jsonify(results=output)
```
Finally, we assert the webservice. The port is manually set to 9000 here (default = 5000) and debug is set to True for the sample application.
```
if __name__ == '__main__':
    app.run(port = 9000, debug = True)
```
> Note: NEVER set `debug = True` on a production server!!!

## 3. Start the service

To start the service, simply navigate to the folder where you've placed the API script and run it with Python. Note that this is run within our virtual environment to ensure all dependencies are visible.

```
(scikit_flask_env)$ cd C:\Code\Environments\scikit_flask_env\ScikitFlask_PoT\Code
(scikit_flask_env)$ python app_api.py
```

The Python interpreter will confirm the successful startup of the service and list the port on which the application is available.

## 4. Testing the API

Use the `~/Code/2_test_api.py` script to test the API. The script simply connects to the endpoint we defined in our API (*/api* on port 9000 of localhost) and passes in a JSON object containing new flower dimensions. The API processes the request and sends back a prediction.

### Sources
Bernico, Mike. https://github.com/mbernico/CS570/tree/master/module_4
