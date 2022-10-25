#!/usr/bin/python3
"""
This module contains route
to check status of API
"""

from models import storage
from api.v1.views import app_views
from flask import jsonify
from models import state
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place

@app_views.route('/status', methods=["GET"])
def status():
    """
        API status
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=["GET"])
def stats():
    """
        API stats
    """
    stats = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(stats)