#!/usr/bin/python3
<<<<<<< HEAD
"""
This module contains route
to check status of API
"""
import models
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """Endpoint to check the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def count_by_class():
    """Endpoint that retrieves the number of each objects by type"""
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    count_by_class = {}

    for key, value in classes.items():
        count = models.storage.count(value)
        count_by_class[key] = count
    return count_by_class


if __name__ == "__main__":
    pass
=======
"""Index module"""
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status', strict_slashes=False)
def index():
    """index page"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Count the number of instances for every classes"""
    return jsonify({'amenities': storage.count(Amenity),
                    'cities': storage.count(City),
                    'places': storage.count(Place),
                    'reviews': storage.count(Review),
                    'states': storage.count(State),
                    'users': storage.count(User)})
>>>>>>> 3ea81942a4d2a6d6f1885268a6a61619f36b27ae
