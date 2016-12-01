# Setting Up a Python Environment

This section describes how to setup an IDE (Yhat Rodeo) to run inside a virtual environment.

## 1 Rodeo IDE Configuration

* We will use Yhat Rodeo for this exercise, available here:
https://www.yhat.com/products/rodeo
* Before running the installer, we need to add a couple of package dependencies for Rodeo. Open a windows command prompt and navigate to the scripts folder of your venv, activate the venv, and install Jupyter and IPython: </br>
```
$ cd C:\Python35\Environments\scikit_flask_env\scripts
$ activate
(scikit_flask_env)$ pip install jupyter_client ipykernel
```
* Then start Python and use the following commands to get the Python path for the virtual environment (it should be in the ~/Scripts folder): </br>
```
(scikit_flask_env)$ python
>>> import os
>>> import sys
>>> os.path.dirname(sys.executable)
```
* Make note of the Python path, and start the Yhat Rodeo installation.
* After Rodeo is installed, open the application.
> If Jupyter, IPython, Numpy, Pandas and Matplotlib were not installed in your system Python installation, Rodeo may present an error at startup. Simply click "Skip Startup" to open the program and access the settings.

* In Rodeo, navigate to *Rodeo > Preferences* and browse to the Python preferences tab
[[[[PREFERENCES SCREENSHOT]]]]
* In the Python preferences pane, update the *Python Command* field to the virtual environment Python path.
[[[[SCREENSHOT PYTHON PATH]]]]
* Rodeo will now work from within your virtual environment. 
