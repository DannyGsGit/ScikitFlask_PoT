
# Train an Iris classifier


from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

import pickle, json, requests


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Step 1: Build the model      ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import the Iris dataset
data = datasets.load_iris()
print(data.DESCR)

# Define features and target
X = data.data
y = data.target

# Split data for train and test splits
X_train, X_test, Y_train, Y_test = train_test_split(X, y)

# Train random forest
iris_rf_model = RandomForestClassifier(n_estimators = 100, n_jobs = 2)
iris_rf_model.fit(X_train, Y_train)





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Step 2: Inspect   model      ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print(classification_report(Y_test, iris_rf_model.predict(X_test)))




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Step 3: Export  model      ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dest = os.path.join('Code', 'Models')
if not os.path.exists(dest):
    os.makedirs(dest)

pickle.dump(iris_rf_model, open(os.path.join(dest, "iris_rf_model.pkl"), "wb"))
