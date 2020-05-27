from os import getenv
from flask import Flask, Response, make_response
from flask_cors import CORS
from flask_caching import Cache
from json import dumps
from typing import List
from logging.config import dictConfig
import logging

import spyglass.tlopo_api_client as api
from spyglass.response_models import StatusResponse, VersionResponse, OceansResponse
from spyglass.models import Version, Ocean


# Application Versioning - I should move this
APP_VERSION='0.2.0'


# Logging Configuration
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

cache_config = {
    "DEBUG": False,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 60
}


# Applicaiton setup
application = Flask(__name__)
CORS(application)
application.config.from_mapping(cache_config)
cache = Cache(application)


# =============================================================================
#
# RESTful
#
# =============================================================================

# Handle 404 errors
@application.errorhandler(404)
def handle_not_found(e) -> Response:
    response: StatusResponse = StatusResponse('not_found')
    return make_response(response.get_json(), 404)


# Status Endpoint
@application.route('/up')
def get_status() -> Response:
    response: StatusResponse = StatusResponse()
    return make_response(response.get_json(), 200)


# Version Endpoint
@application.route('/version')
def get_version() -> Response:
    version: Version = Version(APP_VERSION)
    response: VersionResponse = VersionResponse(version)
    return make_response(response.get_json(), 200)


# List Oceans Endpoint
@application.route('/oceans')
@cache.cached(timeout=15)
def get_oceans() -> Response:
    oceans: List[Ocean] = api.get_oceans()
    response: OceansResponse = OceansResponse(oceans)
    return make_response(response.get_json(), 200)
