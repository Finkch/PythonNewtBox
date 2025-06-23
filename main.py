
from decimal import Decimal

from src.body import Body
from src.vector import Vector
from src.simulate import simulate

if __name__ == '__main__':
    
    sol: Body   = Body('Sol', 1.989e30)
    terra: Body = Body(
        'Terra',
        5.9722e24, 
        pos = Vector(x = 1.496e11),
        vel = Vector(y = 2.978e4),
    )
    
    simulate(Decimal(1), [sol, terra])
