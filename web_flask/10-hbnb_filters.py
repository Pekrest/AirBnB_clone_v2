#!/usr/bin/python3
"""Starts a Flask web application.

"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/hbnb_filters")
def hbnb_filters():
    """
    Displays the main HBnB filters HTML page.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
