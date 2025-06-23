# Main simulation loop

from decimal import Decimal

from .body import Body
from .vector import Vector
from .constants import G

# Simulation loop.
#   t: the length of time in each simulation step
def simulate(t: Decimal, bodies: list[Body]) -> None:
    pass



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
