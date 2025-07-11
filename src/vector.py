# A Vec is a 3-component vector

from __future__ import annotations

from decimal import Decimal


# A 3-component vector with vector arithmetic
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
    
    def __rmul__(self, other: object) -> Vector:
        return self * other
    
    def __truediv__(self, other: object) -> Vector:
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
        
    # Other useful methods
    
    # Returns the absolute size of the vector
    def magnitude(self) -> Decimal:
        return (self.x ** Decimal(2) + self.y ** Decimal(2) + self.z ** Decimal(2)) ** Decimal('0.5')
    
    # Gets the unit-length normal vector
    def normal(self) -> Vector:
        return self / self.magnitude()

    # To string
    def __str__(self) -> str:
        return f'{self.x:.4e}, {self.y:.4e}, {self.z:.4e}'
