# This file is responsible for creating solar systems and the celestial bodies therein

from json import load
from decimal import Decimal
import logging
logger = logging.getLogger(__name__)

from .constants import G
from .body import Body
from .vector import Vector


# Creates a solar system
class SolarSystemFactory:
    def __init__(self, celestial_filepath: str = 'data/bodies.json'):
        self.data = self.load(celestial_filepath)

        self.solarsystem: dict[str, Body] = {}

    # Spawns new solar system and resets
    def spawn(self) -> list[Body]:
        out: list[Body] = [body for body in self.solarsystem.values()]
        self.solarsystem = {}
        return out

    # Adds a body to the current system
    def add(self, body: str | Body) -> None:
        if isinstance(body, str):
            body = self._create(body)

        self.solarsystem[body.name] = body



    # Creates a body from data
    def _create(self, body: str) -> Body:
        if body not in self.data:
            raise KeyError(f'No template data for body "{body}"')

        return Body(
            name = body,
            mass = self.data[body]['mass'],
            pos = self._get_pos(body),
            vel = self._get_vel(body),
        )

    # Gets the position vector of the body, setting it relative to itsparent if relevant
    def _get_pos(self, body) -> Vector:
        pos: Vector = Vector(self.data[body]['a'])

        if self.data[body]['parent'] and self.data[body]['parent'] in self.solarsystem:
            pos += self.solarsystem[self.data[body]['parent']]

        return pos

    # Uses the vis-viva equation to obtain body's initial velocity
    # v^2 = G M (2 / r - 1 / a). Here, r = a => v = (G M / a) ^ 0.5
    def _get_vel(self, body) -> Vector:
        return Vector(
            y = (G * self.data[body]['mass'] / self.data['body']['a']) ** Decimal('0.5')
        )



    # Loads celestial body data
    def load(self, filepath: str = 'data/bodies.json') -> dict[str, dict]:

        # Loads celestial data from a JSON file
        data: list[dict[str, str]]
        with open(filepath, 'r') as file:
            data = load(file)

        # Converts to a more useful format and unit
        bodies: dict[str, dict] = {}
        for entry in data:
            bodies[entry['name']] = {
                'mass': Decimal(entry['mass_kg']),
                'parent': entry['parent'] if entry['parent'] else None,
                'a': Decimal(entry['semi_major_axis_km']) * 1000,       # a: semi-major axis
                'P': Decimal(entry['period_days']) * 86400,             # P: period
            }

        return bodies



    # Some predefined solar systems
    def create(self, name: str) -> None:
        match name:

            # All celestial bodies stored in the data file
            case 'default':
                for body in self.data:
                    self.add(body)

            # A simple three body system
            case 'simple':
                self.add('Sun')
                self.add('Earth')
                self.add('Moon')
