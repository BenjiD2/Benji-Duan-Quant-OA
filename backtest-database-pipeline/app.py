# import main Flask class and request object
from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from fetchData import *

# create the Flask app
app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')
# def hello():
#     return 'Hello, World!'
# def index():
#     return render_template('index.html')

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

class DateForm(FlaskForm):
    name = StringField('What date would you like?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = DateForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        # empty the form field
        form.name.data = ""
        return redirect(url_for('data', id=name))
        # redirect the browser to another route and template     
    return render_template('index.html', form=form, message=message)

@app.route('/data/<id>')
def data(id):
    # run function to get actor data based on the id in the path
    name = fetchResults(id)
    if name == "Unknown":
        # redirect the browser to the error template
        return render_template('404.html'), 404
    else:
        # pass all the data for the selected actor to the template
        return render_template('results.html', name = name)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)