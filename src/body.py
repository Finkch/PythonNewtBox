# A Body is a planet, a star, or other actor with mass

from decimal import Decimal

from .vector import Vector

class Body:
    def __init__(self, name: str, mass: Decimal | float, **kwargs):
        self.name: str = name
        self.mass: Decimal = Decimal(mass)
        
        self.pos: Vector = Vector() if 'pos' not in kwargs else kwargs['pos']
        self.vel: Vector = Vector() if 'vel' not in kwargs else kwargs['vel']
        self.acc: Vector = Vector() if 'acc' not in kwargs else kwargs['acc']
