#!/usr/bin/python3
"""
This module contains the routes for the index view of the API.
"""

from api.v1.views import app_views


@app_views.route('/status')
def statuscode():
    """
    Returns a JSON response with the status code.
    """
    return '''{
    "status": "OK"
}'''
