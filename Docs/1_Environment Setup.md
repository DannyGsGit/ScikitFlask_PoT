# Setting Up a Python Environment
Getting up &amp; running with a Python-Flask environment

## 1. Python Installation

Python can be downloaded from https://www.python.org/. This writeup assumes the use of Python 3.5 on Windows 10.

## 2. Package Installation in Virtualenv

Though not strictly required, virtual environments ensure the stability, repeatability and reproducibility of Data Science projects by quarantining and documenting package dependencies.

The following instructions install Flask in a virtual environment in Python 3.4+ (pyvenv environment) on Windows 10.

### 2.1 Creating the virtual environment

* Create a folder that will contain your Python assets (environments, package downloads, etc.). In this document, we will use *C:\Python35*
* In your Python folder, add an Environments folder (*C:\Python35\Environments*)
* Open a Windows CMD prompt **as an administrator**.
* Navigate to your newly created *Environments* directory: </br>
`$ cd C:\Python35\Environments`
> Do not type in the '$', this is only included to indicate we are typing into the CMD prompt.

* Create a new virtual environment called *scikit_flask_env* using the following command: </br>
`$ python -m venv scikit_flask_env`
* You should now see a new directory at *C:\Python35\Environments\scikit_flask_env* containing multiple sub-directories and files. This is your virtual environment.

### 2.2 Activating the Virtual Environments

To work in a virtual environment, we will *activate* the environment.

* Navigate to the environment's *Scripts* subdirectory: </br>
`$ cd C:\Python35\Environments\scikit_flask_env\Scripts`
* Use the activate.bat script to *activate* the environment: </br>
`$ activate`
> Any commands executed in the ~\Scripts subdirectory of an environment are executed in the environment, regardless of whether the environment is active.

* When working in an active environment, your command prompt format will change to show the environment name in parentheses at the beginning of the line:
</br> [[[[PROMPT SCREENSHOT]]]]
> When you are done working in an environment, you can leave it by *deactivating*:
```
$ cd C:\Python35\Environments\scikit_flask_env\Scripts
$ deactivate
```
When deactivated, the parenthetical environment name should disappear from the CMD prompt line.

### 2.3 Adding environment assets

* We must first run an update on pip before proceeding with environment configuration: </br>
`$ python -m pip install --upgrade pip`
* (Optional) We can view the currently installed packages in the environment with the pip freeze command: </br>
`$ pip freeze`
> Tip 1: In a new environment, pip freeze should return nothing. Compare this to a pip freeze outside of the environment to see packages installed on the base system. </br>
> Tip 2: Pip freeze can write to a file as a simple way to document package dependencies:
`$ pip freeze > package_version_requirements.txt`

* Next, we will install some packages including Flask (webservice framework), Numpy & Scipy (array manipulation), Scikit-learn (machine learning) and pandas (data frame objects):
```
$ cd C:\Python35\Environments\scikit_flask_env\Scripts
$ pip install flask
$ pip install numpy
$ pip install scipy
$ pip install scikit-learn
$ pip install matplotlib
$ pip install pandas
```
> Scipy, in particular, is dependent on C++ and Fortran compilers to install. This can significantly complicate installation on Windows. One option is to install the Numpy+MKL package (http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy) instead of plain Numpy. After downloading the wheel, install using `pip install {filepath}`. </br>
After installing Numpy+MKL, download the scipy wheel (http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy) and install from local as above.

* We now have a virtual environment containing the package dependencies for this project, in isolation from the system-level Python installation. We can view the environment packages using a pip freeze command: </br>
`$ pip freeze`

> Note: Some IDEs, like Yhat Rodeo, need to be installed from within an environment to work inside. Pay careful attention to which environment your IDE is working against when coding!

### 2.4 Adding project assets

We will want to add our project files as a subdirectory of our environment. The purpose of this heirarchy is to limit the scope of our source control scheme to only include code we've generated- the environment we just created, with no custom code yet, is already 450MB in size.

For this demo, we can simply create a project folder at *C:\Python35\Environments\scikit_flask_env\ScikitFlask_PoT* as the target for a Git repository. This will ensure that Git only synchronizes our custom code and not the full environment.

To ensure that the specifics of the environment are captured with the project code in our Git repository, we can use `$ pip freeze > package_versions.txt` to generate a text file containing all environment dependencies.

## 3. Addendum: Re-creating an environment

One benefit of creating a package version file with pip freeze is the ability to re-build an *identical* version of the environment (same packages and versions) using the file. For example, rebuilding using our *package_versions.txt* file is executed with the following command: </br>
`$ pip install -r package_versions.txt`
