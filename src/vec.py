# A Vec is a 3-component vector

from __future__ import annotations

# The Decimal library will give us fixed-point arithmetic.
# This project will use the default 28-digits of decimal precision.
from decimal import Decimal

class Vector:
    def __init__(self, x: Decimal | float = 0, y: Decimal | float = 0, z: Decimal | float = 0):
        self.x: Decimal = Decimal(x)
        self.y: Decimal = Decimal(y)
        self.z: Decimal = Decimal(z)
    
    
    # Dunder methods for arithmetic operators
    def __add__(self, other: object) -> Vector:
        if not isinstance(other, Vector):
            raise ArithmeticError(f'Cannot add Vector to type {type(other)}')
        
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )
        
    def __sub__(self, other: object) -> Vector:
        if not isinstance(other, Vector):
            raise ArithmeticError(f'Cannot subtract Vector by type {type(other)}')
        
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )
        
    def __mul__(self, other: object) -> Vector:
        if not isinstance(other, (int, float, Decimal)):
            raise ArithmeticError(f'Cannot multiply Vector by non-scalar of type {type(other)}')
        
        return Vector(
            self.x * Decimal(other),
            self.y * Decimal(other),
            self.z * Decimal(other),
        )
    
    def __div__(self, other: object) -> Vector:
        if not isinstance(other, (int, float, Decimal)):
            raise ArithmeticError(f'Cannot divide Vector by non-scalar of type {type(other)}')
            
        return Vector(
            self.x / Decimal(other),
            self.y / Decimal(other),
            self.z / Decimal(other),
        )
        
    def __neg__(self) -> Vector:
        return Vector(
            -self.x,
            -self.y,
            -self.z,
        )
        
    # Vector operators
    def dot(self, other: Vector) -> Decimal:
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other: Vector) -> Vector:
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )
