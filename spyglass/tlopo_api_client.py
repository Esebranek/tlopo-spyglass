import requests
from typing import List

from spyglass.models import Ocean


OCEAN_API = 'https://api.tlopo.com/shards'


# Get ocean information
def get_oceans() -> List[Ocean]:
    response = requests.get(OCEAN_API)
    # Handle bad response codes
    if response.status_code >= 300:
        pass
    data = response.json()
    # Return data mapped to Ocean objects
    return list(map(lambda o: Ocean(o['name'], o['available'], o['population'], o['created'], None, None), [data[key] for key in data.keys()]))