#!/usr/bin/python3
"""Starting a flask web app. that listens on a host and port
   displays contents"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exc):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def hello_hbnb():
    """display content on net"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def hello_there(id):
    """display contents based on id on net"""
    states = storage.all(State).values()
    n = 0
    for state in states:
        if state.id == id:
            n = 1
    return render_template("9-states.html", states=states, id=id, n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
