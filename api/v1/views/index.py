#!/usr/bin/python3
"""
This module contains route
to check status of API
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=["GET"])
def status():
    """
        API status
    """
    return jsonify({"status": "OK"})