# A wrapper for Decimal time

from decimal import Decimal

class Time:
    def __init__(self, t: int | float | Decimal = 1):
        
        # Sets t, the seconds per step
        self.change(t)
        
        # The current step
        self.steps: int = 0
        
        # Total time elapsed
        self.total: Decimal = Decimal(0)
        
    # Comparison operators
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, (int, float, Decimal, Time)):
            raise TypeError(f'Cannot compare Time with non-Time or non-scalar value of type {type(other)}')
        
        if isinstance(other, Time):
            return self.total < other.total
        return self.total < other
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (int, float, Decimal, Time)):
            raise TypeError(f'Cannot compare Time with non-Time or non-scalar value of type {type(other)}')
        
        if isinstance(other, Time):
            return self.total == other.total
        elif isinstance(other, Decimal):
            return self.total == other
        else:
            return self.total == Decimal(other)
            
    def __le__(self, other: object) -> bool:
        return self < other or self == other
        
    def __gt__(self, other: object) -> bool:
        return not self <= other
    
    def __ge__(self, other: object) -> bool:
        return not self < other
    
    
        
    # Changes the seconds per step
    def change(self, t: int | float | Decimal) -> None:
        if not isinstance(t, Decimal):
            t = Decimal(t)
            
        # Seconds per step
        self.t: Decimal = t
        
    # Steps forward one
    def step(self) -> None:
        self.steps += 1
        self.total += self.t
    
    # To string
    def __str__(self) -> str:
        seconds: int    = int(self.total)
        minutes: int    = int(seconds // 60)
        hours: int      = int(minutes // 60)
        days: int       = int(hours // 24)
        years: int      = int(days // 365)
        
        return f'{years}y, {days % 365:03}d, {hours % 24:02}:{minutes % 60:02}:{seconds % 60:02} ({self.steps} steps)'
