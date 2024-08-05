#!/usr/bin/python3
"""
This module initializes the views package for the AirBnB clone v3 API.

It creates a Blueprint object named 'app_views'
that serves as a blueprint for all the API routes.

The Blueprint is registered with the Flask application and has
a URL prefix of '/api/v1'.

The views package contains the API routes for different resources such as
users, places, reviews, etc.
"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
# from api.v1.views.users import *
# from api.v1.views.places import *
# from api.v1.views.places_reviews import *
