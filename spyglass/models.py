import re

# Application Version
class Version:
    def __init__(self, version):
        # TODO: Build this into the app instead
        self._version = version
    
    def get_version(self):
        return self._version


class Fleet:
    def __init__(self, fleet_type: str = None, state: str = None, ships_remaining: int = None, started: int = None):
        self._fleet_type = fleet_type
        self._state = state
        self._ships_remaining = ships_remaining
        self._started = started

    def get_type(self):
        return self._fleet_type

    def get_state(self):
        return self._state

    def get_ships_remaining(self):
        return self._ships_remaining

    def get_started(self):
        return self._started

    def get_dict(self) -> dict:
        if not self.get_type():
            return None
        return {
            'type': self.get_type(),
            'state': self.get_state(),
            'ships_remaining': self.get_ships_remaining(),
            'started': self.get_started()
        }


class Invasion:
    def __init__(self, location: str = None, state: str = None, phase: str = None, num_players: int = None, started: int = None):
        self._location = location
        self._state = state
        self._phase = phase
        self._num_players = num_players
        self._started = started

    def get_location(self):
        return self._location

    def get_state(self):
        return self._state

    def get_phase(self):
        return self._phase

    def get_num_players(self):
        return self._num_players

    def get_started(self):
        return self._started

    def get_dict(self) -> dict:
        if not self.get_location():
            return None
        return {
            'location': self.get_location(),
            'state': self.get_state(),
            'phase': self.get_phase(),
            'num_players': self.get_num_players(),
            'started': self.get_started()
        }


# Ocean object returned by TLOPO API
class Ocean:
    def __init__(self, name: str = 'unknown', available: bool = False, population: int = None, created: int = None, fleet: Fleet = None, invasion: Invasion = None):
        self._name = name
        self._available = available
        self._population = population
        self._created = created
        self._fleet = fleet
        self._invasion = invasion


    def get_name(self):
        return self._name


    def get_available(self):
        return self._available


    def get_population(self):
        return self._population


    def get_created(self):
        return self._created


    def get_fleet(self):
        return self._fleet


    def get_invasion(self):
        return self._invasion


    def get_dict(self):
        return {
            'name': self.get_name(),
            'available': self.get_available(),
            'population': self.get_population(),
            'created': self.get_created(),
            'fleet': self.get_fleet().get_dict(),
            'invasion': self.get_invasion().get_dict()
        }
