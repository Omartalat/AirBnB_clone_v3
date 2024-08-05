#!/usr/bin/python3
"""
Flask routes for handling Amenity objects.
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities/', methods=['GET'])
def get_amenities():
    """Retrieves the list of all Amenity objects"""
    amenities = storage.all(Amenity)
    result = []
    for amenity in amenities.values():
        result.append(amenity.to_dict())
    return jsonify(result)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """Retrieve Amenity object by ID."""
    if not amenity_id:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', mehtods=['DELETE'])
def delete_amenity(amenity_id):
    """delete Amenity object by ID."""
    if not amenity_id:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    amenity.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities/', methods=['POST'])
def create_amenity():
    """create Amenity object"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if not data.get('name'):
        abort(400, 'Missing name')
    amenity = Amenity(**data)
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """update Amenity object by ID."""
    if not amenity_id:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    amenity = storage.get(Amenity, amenity_id)
    for key, val in data.items():
        setattr(amenity, key, val)
    amenity.save()
    return jsonify(amenity.to_dict()), 200 