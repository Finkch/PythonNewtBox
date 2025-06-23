# Main simulation loop

from decimal import Decimal

from .body import Body
from .vector import Vector
from .constants import G

# Simulation loop.
#   t: the length of seconds in each simulation step
def simulate(t: Decimal, bodies: list[Body]) -> None:
    
    # How many steps have occured since the start of the simulation
    step: int = 0
    
    # Simulation loop
    while True:
        
        # Applies gravity
        gravity(bodies)
        
        # Moves bodies through spacetime
        for body in bodies:
            body.step(t)
            
        printout(step, t, bodies)
        
        # Increments current step
        step += 1



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
            fg: Vector = r * G * a.mass * b.mass / r.magnitude() ** 3
            
            # Applies the force onto each body
            a.force(fg)
            b.force(-fg)

def printout(s: int, t: Decimal, bodies: list[Body]) -> None:
    print(f'\nTime elapsed: {s * t:.0f}s ({s} steps)')
    for body in bodies:
        print(f'{body}')
