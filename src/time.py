# A wrapper for Decimal time

from decimal import Decimal

from time import time

class Time:
    def __init__(self, t: int | float | Decimal = 1):
        
        # Sets t, the seconds per step
        self.change(t)
        
        # The current step
        self.steps: int = 0
        
        # Total time elapsed
        self.time: Decimal = Decimal(0)
        
    # Comparison operators
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, (int, float, Decimal, Time)):
            raise TypeError(f'Cannot compare Time with non-Time or non-scalar value of type {type(other)}')
        
        if isinstance(other, Time):
            return self.time < other.time
        return self.time < other
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (int, float, Decimal, Time)):
            raise TypeError(f'Cannot compare Time with non-Time or non-scalar value of type {type(other)}')
        
        if isinstance(other, Time):
            return self.time == other.time
        elif isinstance(other, Decimal):
            return self.time == other
        else:
            return self.time == Decimal(other)
            
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
    def step(self, t: int | float | Decimal | None = None) -> None:
        if t:
            self.change(t)
        
        self.steps += 1
        self.time += self.t
    
    # To string
    def __str__(self) -> str:
        seconds: int    = int(self.time)
        minutes: int    = int(seconds // 60)
        hours: int      = int(minutes // 60)
        days: int       = int(hours // 24)
        years: int      = int(days // 365)
        
        return f'{years}y, {days % 365:03}d, {hours % 24:02}:{minutes % 60:02}:{seconds % 60:02}'


# A Stopwatch is used to track timestamps and their deltas
class Stopwatch:
    def __init__(self, goal: float | None = None, max_length: int = 2):
    
        self.timestamps: list[float] = [time()]
        
        # Aims for self.since() to return value close to this.
        # If goal == None, goal will never be met.
        # If goal <= 0, goal will always be met.
        self.goal: float | None = goal
        
        # The max number of timestamps
        self.max_length: int = max_length
        
    # If time since last stamp is greater/equal to 
    # goal, return true and push the timestamp
    def __call__(self) -> bool:
        if self.goal == None:
            return False
        
        if self.since() >= self.goal:
            self.push()
            return True
        return False
        
    # Pushes a value onto the timestamps pile
    def push(self, timestamp: float | None = None) -> None:
        if not timestamp:
            timestamp = time()
        self.timestamps.append(timestamp)
        
        if len(self.timestamps) > self.max_length:
            self.timestamps = self.timestamps[1:]
        
    # Returns the most recent timestamp
    def peek(self) -> float:
        return self.timestamps[-1]
        
    # Returns the difference between the two most recent timestamps
    def delta(self) -> float:
        if len(self.timestamps) < 2:
            return 0
        return self.timestamps[-1] - self.timestamps[-2]  
      
    # Returns elapsed time since last timestamp
    def since(self) -> float:
        return time() - self.peek()



# A stopwatch tracks both real time and simulation time
class Times:
    def __init__(self, t: int | float | Decimal = 1):
        self.simulation: Time = Time(t)
        self.real: Time = Time(0)
        
        self.stopwatch: Stopwatch = Stopwatch()
        
    def step(self) -> None:
        self.simulation.step()
        
        self.stopwatch.push()
        self.real.step(self.stopwatch.delta())
        
    def __str__(self) -> str:
        return f'Simulation time: {self.simulation} ({self.simulation.steps} steps)\nReal time:\t {self.real} ({1 / self.stopwatch.delta():.1f} steps per second)'
