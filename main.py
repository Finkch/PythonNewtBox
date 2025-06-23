
# The Decimal library will give us fixed-point arithmetic.
# This project will use the default 28-digits of decimal precision.
from decimal import Decimal

from src.logging import logs_setup
import logging

from src.body import Body
from src.vector import Vector
from src.simulate import simulate

logger = logging.getLogger(__name__)


# TODO:
# * Add visuals
# * Add tests


if __name__ == '__main__':
    
    # Sets up the logger
    logs_setup(file_level = logging.INFO, stream_level = logging.DEBUG)
    
    sol: Body   = Body('Sol', 1.989e30)
    terra: Body = Body(
        'Terra',
        5.9722e24, 
        pos = Vector(x = 1.496e11),
        vel = Vector(y = 2.978e4),
    )
    bodies = [sol, terra]
    
    simulate(Decimal(1 * 60), bodies)
