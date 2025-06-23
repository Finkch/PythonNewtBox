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
        
        # Since acceleration is reset at the end of every step, we track
        # a fake acceleration for ease of logging
        self.fake_acc: Vector = Vector()

    # Applies a force onto the body
    def force(self, newtons: Vector) -> None:
        self.acc += newtons / self.mass

    # Performs one step in the simulation
    def step(self, t: Decimal) -> None:
        self.vel += self.acc * t
        self.pos += self.vel * t
        
        # Reset acceleration
        self.fake_acc = self.acc
        self.acc = Vector()
        
    # To string
    def __str__(self) -> str:
        return f'''{self.name} ({self.mass:.2e} kg):
    * Position:\t\t{self.pos}
    * Velocity:\t\t{self.vel}
    * Acceleration:\t{self.fake_acc}'''
