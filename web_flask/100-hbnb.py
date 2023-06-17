#!/usr/bin/python3
"""Starting a flask web app. that listens on a host and port
   displays contents"""

from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exc):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """display content on net"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    return render_template("100-hbnb.html",
                           states=states,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
