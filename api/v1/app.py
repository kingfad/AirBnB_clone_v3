#!/usr/bin/python3

"""
Module that starts an API for AirBnB_Clone
Running on host: HBNB_API_HOST:HBNB_API_PORT
Or 0.0.0.0:5000 if below env's is not define
"""

from flask import Flask,Blueprint
from models import storage
from api.v1.views import app_views
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(error):
    """ Close Storage """
    storage.close()


if __name__ == "__main__":
    """
        Main Function
    """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)