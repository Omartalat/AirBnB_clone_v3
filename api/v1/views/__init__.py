#!/usr/bin/python3
"""
This module initializes the views package for the AirBnB clone v3 API.

It creates a Blueprint object named 'app_views' that serves as a blueprint for all the API routes.
The Blueprint is registered with the Flask application and has a URL prefix of '/api/v1'.

The views package contains the API routes for different resources such as users, places, reviews, etc.
"""

from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
