#!/usr/bin/python3
"""
Flask routes for handling City objects.
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def state_cities(state_id):
    """Retrieves the list of all City objects of a State"""
    if not state_id:
        abort(404)
    state = storage.get(State, state_id)
    cities = state.cities
    result = []
    for city in cities:
        result.append(city.to_dict())
    return jsonify(result), 200


@app_views.route('/cities/<city_id>/', methods=['GET'])
def get_city(city_id):
    """Retrieve City object by ID"""
    if not city_id:
        abort(404)
    city = storage.get(City, city_id)
    return jsonify(city.to_dict()), 200


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """Delete City object by ID"""
    if not city_id:
        abort(404)
    city = storage.get(City, city_id)
    city.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """Create City"""
    if not state_id:
        abort(400)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if not data.name:
        abort(400, 'Missing name')
    city = City(state_id=state_id, **data)
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Update City object by ID."""
    if not city_id:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    city = storage.get(City, city_id)
    dump = ['id', 'state_id', 'created_at', 'updated_at']
    for key, val in data.items():
        if key not in dump:
            setattr(city, key, val)
    city.save()
    return jsonify(city.to_dict()), 200
