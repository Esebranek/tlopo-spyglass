import requests
from flask import current_app
from json.decoder import JSONDecodeError
from typing import List

from spyglass.models import Ocean
from spyglass.model_factory import ApiResponseMapper


OCEAN_API = 'https://api.tlopo.com/shards'


response_mapper = ApiResponseMapper()


# Get ocean information
def get_oceans() -> List[Ocean]:
    response = requests.get(OCEAN_API)
    # Handle bad response codes
    if response.status_code >= 300:
        pass
    try:
        data = response.json()
    except JSONDecodeError as jde:
        current_app.logger.warn(jde)
        return response_mapper.oceans_factory({})
    # Return data mapped to Ocean objects
    return response_mapper.oceans_factory(data)