#!/usr/bin/python3
"""
Starts a Flask web application listening on 0.0.0.0, port 5000
and routes /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display "C" + text (replaces underscores with spaces)
    /python/(<text>): display "Python" + text (default is 'is cool')
    /number/<int:n>: display "n is a number" only if n is an integer
    /number_template/<int:n>: display HTML page only if n is an integer
    /number_odd_or_even/<int:n>: display HTML page only if n is an integer
    /state_list: display HTML page with list of all State objects
    /cities_by_states: display HTML page with list of all City objects
    /states/<id>: display HTML page with list of all City objects
    /states: display HTML page with list of all State objects
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Display hello message

    Returns:
        str: hello message
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Display HBNB

    Returns:
        str: HBNB
    """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Display text

    Args:
        text (str): text to display

    Returns:
        str: text
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Display other text

    Args:
        text (str, optional): Other text to display. Defaults to "is cool".

    Returns:
        str: text
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """Display number

    Args:
        n (int): number to display

    Returns:
        str: text with number
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def html_if_int(n):
    """Display HTML template

    Args:
        n (int): number to check

    Returns:
        str: HTML template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def html_odd_or_even(n):
    """Check if number is odd or even

    Args:
        n (int): number to check

    Returns:
        str: HTML template
    """
    odd_or_even = "even" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_or_even=odd_or_even)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the db connection

    Args:
        exception (str): exception to close
    """
    storage.close()


@app.route('/states')
@app.route('/states_list')
def states_list():
    """
    Display a HTML page with list of all State objects

    Returns:
        HTML: HTML page with list of all State objects
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """
    Display a HTML page with list of all City objects linked to the State

    Returns:
        HTML: HTML page with list of all City objects
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>')
def states_id(id):
    """
    Display a HTML page with list of all City objects linked to the State

    Args:
        id (str): state id

    Returns:
        HTML: HTML page with list of all City objects
    """
    state = storage.get(State, id)
    if state is not None:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
