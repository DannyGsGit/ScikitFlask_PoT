
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Import Dependencies ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators



#~~~~~~~~~~~~~~~~~~~~~~~~~
#### Initialize Flask ####
#~~~~~~~~~~~~~~~~~~~~~~~~~

app = Flask(__name__)  # Initializes a Flask instance with argument __name__

class HelloForm(Form):
    sayhello = TextAreaField('',[validators.DataRequired()])

#~~~~~~~~~~~~~~~~~~~~~~~~~
#### Define App ####
#~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('IrisModelApp.html', form=form)

@app.route('/result', methods = ['POST'])  # Specify the URL that executes the index function
def hello():
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['sayhello']
        return render_template('result.html', name = name)
    return render_template('IrisModelApp.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
