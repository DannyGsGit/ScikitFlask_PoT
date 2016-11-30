# PTN_Demo
Getting up &amp; running with a Python-Flask environment

## 1. Python Installation

Python can be downloaded from https://www.python.org/. This writeup assumes the use of Python 3.5 on Windows 10.

## 2. Package Installation

The following instructions install Flask in a virtual environment in Python 3.4+ (pyvenv environment) on Windows 10.

* Open a command prompt as an administrator.
* Navigate to your project folder and enter the following command to create a virtual environment called *PTNEnv*: </br>
`$ python -m venv PTNEnv`</br>
This will create a virtual environment with it's own dependencies quarantined from the system-level Python installation, protecting against package clutter and collisions. After running this command, you should see a *PTNEnv* folder appear in your project folder.
> Environments may be activated/deactivated, but this writeup will simply invoke the interpreter in the PTVEnv folder- this is functionally the same as activating the environment.

* To ensure that our environment is using the latest pip installer, update pip: </br>
```
$ PTNEnv\Scripts\python -m pip install --upgrade pip
```
* Next, we will install some packages including Flask (webservice framework), Numpy & Scipy (array manipulation), Scikit-learn (machine learning) and pandas (data frame objects):
```
$ PTNEnv\Scripts\pip install flask
$ PTNEnv\Scripts\pip install numpy
$ PTNEnv\Scripts\pip install scipy
$ PTNEnv\Scripts\pip install scikit-learn
$ PTNEnv\Scripts\pip install matplotlib
$ PTNEnv\Scripts\pip install pandas
```
> Scipy, in particular, is dependent on C++ and Fortran compilers to install. This can significantly complicate installation on Windows. One option is to install the Numpy+MKL package (http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy) instead of plain Numpy. After downloading the wheel, install using `pip install {filepath}`. </br>
After installing Numpy+MKL, download the scipy wheel (http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy) and install from local as above.

* We now have a virtual environment containing the package dependencies for this project, in isolation from the system-level Python installation.
