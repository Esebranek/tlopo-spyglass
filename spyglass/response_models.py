import re
from json import dumps
from typing import List

from spyglass.models import Version, Ocean


class StatusResponse:
    def __init__(self, status: str = None):
        if status:
            self.set_status(status)
        else:
            self.set_status('ok')

    def get_status(self) -> str:
        return self._status

    def set_status(self, status: str) -> None:
        self._status = status

    def get_json(self):
        return dumps({
            'status': self.get_status()
        })


class VersionResponse:
    def __init__(self, version: Version):
        self._version = version.get_version()

    def get_json(self):
        return dumps({
            'status': 'ok',
            'version': self._version
        })




class OceansResponse:
    def __init__(self, oceans: List[Ocean] = None):
        self._oceans = oceans

    def get_oceans(self):
        return self._oceans

    def get_json(self):
        oceans = list(map(lambda o: o.get_dict(), self.get_oceans()))
        return dumps({
            'status': 'ok',
            'oceans': sorted(oceans, key = lambda o: o['name'])
        })