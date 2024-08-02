#!/usr/bin/python3
"""
This module contains the routes for the index view of the API.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def status():
    """routes to status page"""
    res = {'status': 'OK'}
    return jsonify(res)


@app_views.route('/stats', methods=['GET'])
def stats():
    """routes to stats"""
    classes = {"amenities": Amenity, "cities": City,
               "places": Place, "reviews": Review,
               "states": State, "users": User}
    stats_dict = {}
    for key, val in classes.items():
        num = storage.count(val)
        stats_dict[key] = num
    return jsonify(stats_dict)
