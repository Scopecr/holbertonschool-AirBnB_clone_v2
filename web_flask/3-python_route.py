#!/usr/bin/python3
"""
starts a Flask application
"""

from flask import Flask
app = flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """return Hello HBNB!"""
    return  'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slahes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C' + text.replace('_',' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<test>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display "Pyython", followed by the calue of the text variable"""
    return 'Pyython' + text.replace('_',' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
