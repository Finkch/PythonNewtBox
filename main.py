
# The Decimal library will give us fixed-point arithmetic.
# This project will use the default 28-digits of decimal precision.
from decimal import Decimal

from src.logging import logs_setup
import logging
logger = logging.getLogger(__name__)

from src.solarsystems import SolarSystemFactory
from src.simulate import simulate


# TODO:
# * Add visuals
# * Add tests
# * Added dynamic rates


if __name__ == '__main__':

    # Sets up the logger.
    # There are two places the output is streamed: to a file and to console
    logs_setup(file_level = logging.INFO, stream_level = logging.DEBUG)


    # Used to initialise the solar system
    factory: SolarSystemFactory = SolarSystemFactory()




    #   –– Add celestial bodies here ––
    factory.create('default') # Loads all planets, moons, and the sun as stored in bodies.json
    # factory.create('simple') # Sun, earth, moon

    # factory.add('Sun')
    # factory.add('Earth')



    # Creates the solar system
    bodies = factory.spawn()

    simulate(Decimal(1 * 60 * 60), bodies)
