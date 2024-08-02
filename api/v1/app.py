#!/usr/bin/python3
"""
This module contains the Flask application for the AirBnB clone API.

It creates a Flask app, registers the blueprint for the API views,
and defines a teardown function to close the storage.

The app can be run with the specified host and port, or with default
values if not provided.
"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown."""
    storage.close()


host = getenv("HBNB_API_HOST")
port = getenv("HBNB_API_PORT")

if __name__ == '__main__':
    if host and port:
        app.run(host=host, port=port)
    else:
        app.run(host="0.0.0.0", port=5000)
