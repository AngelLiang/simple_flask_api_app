# coding=utf-8
# flake8: noqa

from flask import Blueprint
from flask_cors import CORS

api_v1_bp = Blueprint("api_v1", __name__)

CORS(api_v1_bp)

from app.apis.v1 import auth
from app.apis.v1 import user
