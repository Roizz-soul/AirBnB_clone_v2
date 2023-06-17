#!/usr/bin/python3
"""Starting a flask web app. that listens on a host and port
   displays contents"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display content on net"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display sontent on net"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """display some edited content"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_pyth(text="is cool"):
    """display some content with default value if no text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """display integer only"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
