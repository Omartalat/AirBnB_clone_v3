#!/usr/bin/python3
"""
This module contains the routes for the index view of the API.
"""
from api.v1.views import app_views
from flask import jsonify



@app_views.route('/status', methods=['GET'])
def status():
    ''' routes to status page '''
    return jsonify({'status': 'OK'})
