#!/usr/bin/python3
"""Handles all RESTful API actions for `Amenity`"""
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import jsonify, abort, make_response, request


@app_views.route("/amenities", strict_slashes=False)
def amenities():
    """Retrieve list of all `Amenity` objects

    Returns:
        `flask.Response`: List of all the amenities
    """
    all_amenities = storage.all(Amenity).values()
    list_amenities = []
    for amenity in all_amenities:
        list_amenities.append(amenity.to_dict())
    return jsonify(list_amenities)


@app_views.route("/amenities/<amenity_id>", strict_slashes=False)
def amenity(amenity_id):
    """Retrieve one `Amenity`

    Args:
        amenity_id (str): Amenity identifier

    Returns:
        flask.Response: An amenity in json
    """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route("/amenities/<amenity_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """Delete an amenity.

    Args:
        amenity_id (str): The ID of the amenity.

    Returns:
        dict: An empty JSON.

    Raises:
        404: If the specified amenity_id does not exist.
    """
    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    storage.delete(amenity)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route("/amenities", methods=["POST"], strict_slashes=False)
def create_amenity():
    """Create an amenity

    Returns:
        dict: New amenity in JSON

    Raises:
        400: If request body is not a valid JSON
        400: If the payload does not contain the key `name`
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Amenity(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route("/amenities/<amenity_id>", methods=["PUT"],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """Update Amenity object by ID."""
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(amenity, key, value)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 200)
