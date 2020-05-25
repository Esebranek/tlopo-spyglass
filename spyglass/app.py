from flask import Flask, Response, make_response
from flask_cors import CORS
from flask_socketio import SocketIO
from gevent import monkey; monkey.patch_socket()
from json import dumps
from typing import List
from apscheduler.schedulers.gevent import GeventScheduler
from apscheduler.triggers.interval import IntervalTrigger
from logging.config import dictConfig
import logging

import spyglass.tlopo_api_client as api
from spyglass.response_models import StatusResponse, VersionResponse, OceansResponse
from spyglass.models import Version, Ocean


# Application Versioning - I should move this
APP_VERSION='0.1.0'


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


# Applicaiton setup
application = Flask(__name__)
CORS(application)
socketio = SocketIO(application, cors_allowed_origins=["localhost"])
socketio.logger=application.logger

# Scheduler for socketio broadcast
scheduler = GeventScheduler()
trigger = IntervalTrigger(seconds=15)
scheduler.start()


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
def get_oceans() -> Response:
    oceans: List[Ocean] = api.get_oceans()
    response: OceansResponse = OceansResponse(oceans)
    return make_response(response.get_json(), 200)


# =============================================================================
#
# SocketIO
#
# =============================================================================

# New connection
@socketio.on('connect')
def handle_new_connection():
    application.logger.info('New socketio connection')


# Broadcast Cceans
@scheduler.scheduled_job(trigger)
def broadcast_oceans() -> None:
    oceans: List[Ocean] = api.get_oceans()
    socketio.emit('oceans_status', [ocean.get_dict() for ocean in oceans])


if __name__ == '__main__':
    socketio.run(application, port=int(os.environ.get('PORT', '8000')))
