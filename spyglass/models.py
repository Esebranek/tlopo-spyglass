import re

# Application Version
class Version:
    def __init__(self, version):
        # TODO: Build this into the app instead
        self._version = version
    
    def get_version(self):
        return self._version


class Fleet:
    def __init__(self):
        pass


class Invasion:
    def __init__(self):
        pass


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
            'fleet': self.get_fleet(),
            'invasion': self.get_invasion()
        }
