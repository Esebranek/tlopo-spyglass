from flask import Flask, Response, make_response
from json import dumps
from typing import List

import spyglass.tlopo_api_client as api
from spyglass.response_models import StatusResponse, VersionResponse, OceansResponse
from spyglass.models import Version, Ocean


APP_VERSION='0.0.2'


application = Flask(__name__)



@application.route('/up')
def get_status() -> Response:
    response: StatusResponse = StatusResponse()
    return make_response(response.get_json(), 200)


@application.route('/version')
def get_version() -> Response:
    version: Version = Version(APP_VERSION)
    response: VersionResponse = VersionResponse(version)
    return make_response(response.get_json(), 200)


@application.route('/oceans')
def get_oceans() -> Response:
    oceans: List[Ocean] = api.get_oceans()
    response: OceansResponse = OceansResponse(oceans)
    return make_response(response.get_json(), 200)
