#~~~~~~~~~~~~~~~~~~~~~~~~
#### Import packages ####
#~~~~~~~~~~~~~~~~~~~~~~~~

## ML Dependencies
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle, os

# Web service dependencies
from flask import Flask, request, abort, jsonify




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Unpickle the models ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
my_random_forest = pickle.load(open(os.path.join('Models', 'iris_rf_model.pkl'), 'rb'))





#~~~~~~~~~~~~~~~~~~~~~~~~~
#### Define Flask API ####
#~~~~~~~~~~~~~~~~~~~~~~~~~

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(port = 9000, debug = True)


#~~~~~~~~~~~~~~~~~~
#### Citations ####
#~~~~~~~~~~~~~~~~~~
# https://github.com/mbernico/CS570/blob/master/module_4/flask_demo.py
