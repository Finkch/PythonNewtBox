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
        
        return f'{years}y, {days % 365:03}d, {hours % 24:02}h, {minutes % 60:02}m, {seconds % 60:02}s ({self.steps} steps)'
