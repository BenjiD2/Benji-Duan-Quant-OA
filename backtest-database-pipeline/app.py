from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from fetchData import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

Bootstrap(app)

class DateForm(FlaskForm):
    # Creates requirements for Form
    name = StringField('What date would you like?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    # Displays intial page with form, reads in form results and redirects to the correct response
    form = DateForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        return redirect(url_for('data', id=name)) 
    return render_template('index.html', form=form, message=message)

@app.route('/data/<id>')
def data(id):
    # Displays results page with stock data, uses form results and fetchResult function to display result
    name = fetchResult(id)
    if name == "Unknown":
        return render_template('404.html'), 404
    else:
        return render_template('results.html', name = name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)