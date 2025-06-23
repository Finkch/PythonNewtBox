# Main simulation loop

from decimal import Decimal

from .body import Body
from .vector import Vector
from .constants import G
from .time import Stopwatch

# Simulation loop.
#   t: the length of seconds in each simulation step
def simulate(t: Decimal, bodies: list[Body]) -> None:
    
    # How many steps have occured since the start of the simulation
    time: Stopwatch = Stopwatch(t)
    
    # Simulation loop
    while time.simulation < 3.154e+7:
        
        # Applies gravity
        gravity(bodies)
        
        # Moves bodies through spacetime
        for body in bodies:
            body.step(time.real.t)
            
        printout(time, bodies)
        
        # Increments current step
        time.step()



# Applies gravity between all pairs of bodies
def gravity(bodies: list[Body]) -> None:
    
    # Considers each pair only once
    #   a, b:   celestial bodies
    #   r:      displacement vector
    #   fg:     f_G, force of gravity
    for (i, a) in enumerate(bodies[:-1]):
        for b in bodies[i + 1:]:
            
            # Displacement between bodies
            r: Vector = b.pos - a.pos
            
            # Gravitational force between bodies
            # fg = G m1 m2 r_bold / |r|^3
            fg: Vector = G * a.mass * b.mass * r / r.magnitude() ** 3
            
            # Applies the force onto each body
            a.force(fg)
            b.force(-fg)

def printout(time: Stopwatch, bodies: list[Body]) -> None:
    print(f'{time}')
    for body in bodies:
        print(f'{body}')
