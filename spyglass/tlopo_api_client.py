import requests
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
    data = response.json()
    # Return data mapped to Ocean objects
    return response_mapper.oceans_factory(data)