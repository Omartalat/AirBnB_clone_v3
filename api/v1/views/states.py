#!/usr/bin/python3
"""
Flask routes for handling State objects.
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states/', methods=['GET'])
def get_states():
    """
    Retrieves the list of all State objects.
    """
    print("Retrieving states")
    states_list = []
    states = storage.all(State)
    for state in states.values():
        state_dict = state.to_dict()
        states_list.append(state_dict)
    return jsonify(states_list), 200


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Retrieves a State object by ID."""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    state_dict = state.to_dict()
    return jsonify(state_dict), 200


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Delete a State object by ID."""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'])
def create_state():
    """Create a State"""
    request_body = request.get_json()
    if not request_body:
        abort(400, "Not a JSON")
    if not request_body['name']:
        abort(400, 'Missing name')
    state = State(**request_body)
    state.save()
    state_dict = state.to_dict()
    return jsonify(state_dict), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Update a State object by ID"""
    if not state_id:
        abort(404)
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    dump = ['id', 'created_at', 'updated_at']
    for key, val in data.items():
        if key not in dump:
            setattr(state, key, val)
    state.save()
    state_dict = state.to_dict()
    return jsonify(state_dict), 200
