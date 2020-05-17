from typing import List

from spyglass.models import Ocean, Fleet, Invasion


class ApiResponseMapper:
    def oceans_factory(self, response_blob: dict) -> List[Ocean]:
        entries = [response_blob[key] for key in response_blob.keys()]
        return list(map(lambda entry: self._ocean_from_blob(entry), entries))

    def _ocean_from_blob(self, ocean_blob: dict) -> Ocean:
        return Ocean(
            ocean_blob.get('name', 'Unknown'),
            ocean_blob.get('available', False),
            ocean_blob.get('population', 0),
            ocean_blob.get('created', 0),  # Probably safe to assume something went wrong if we've defaulted the time to 1970
            self._fleet_from_blob(ocean_blob.get('fleet', {})),
            self._invasion_from_blob(ocean_blob.get('invasion', {}))
        )

    def _fleet_from_blob(self, fleet_blob: dict) -> Fleet:
        if len(fleet_blob.keys()) < 1:
            return Fleet()
        return Fleet(
            fleet_blob.get('type', None),
            fleet_blob.get('state', None),
            fleet_blob.get('shipsRemaining', None),
            fleet_blob.get('started', None)
        )

    def _invasion_from_blob(self, invasion_blob: dict) -> Invasion:
        if len(invasion_blob.keys()) < 1:
            return Invasion()
        return Invasion(
            invasion_blob.get('location', None),
            invasion_blob.get('state', None),
            invasion_blob.get('phase', None),
            invasion_blob.get('num_players', None),
            invasion_blob.get('started', None)
        )

