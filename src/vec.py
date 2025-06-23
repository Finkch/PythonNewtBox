# A Vec is a 3-component vector

from decimal import Decimal

class Vec:
    def __init__(self, x: Decimal | float = 0, y: Decimal | float = 0, z: Decimal | float = 0):
        self.x: Decimal = Decimal(x)
        self.y: Decimal = Decimal(y)
        self.z: Decimal = Decimal(z)
