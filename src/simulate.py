# Main simulation loop

from decimal import Decimal
from pynput import keyboard
import logging

from .body import Body
from .vector import Vector
from .constants import G
from .time import Times, Stopwatch


logger = logging.getLogger(__name__)

# Required to be a global for the asynchronous keyboard listener
running: bool = True


# Simulation loop.
#   t: the length of seconds in each simulation step
def simulate(t: Decimal, bodies: list[Body]) -> None:

    # How many steps have occured since the start of the simulation
    time: Times = Times(t)

    # Used to control when printouts occur
    printtimer: Stopwatch = Stopwatch(goal = 1 / 60)

    # How often to push simulation state into debug logs
    loggertimer: Stopwatch = Stopwatch(goal = 1)

    # Adds key listener to allow escaping simulation loop
    listener = keyboard.Listener(on_press = on_press)
    listener.start()

    logger.info(f'Starting simulation with {len(bodies)} bodies and time step {time.real.t} seconds per step...')

    # Simulation loop
    while running:

        # Performs a printout
        if printtimer():
            logger.debug(f'{time}' + ''.join([f'\n{body}' for body in bodies]))

        # Separate timer for file write to mitigate endless log file growth
        if loggertimer():
            logger.info(f'{time}' + ''.join([f'\n{body}' for body in bodies]))

        # Applies gravity
        gravity(bodies)

        # Moves bodies through spacetime
        for body in bodies:
            body.step(time.real.t)

        # Increments current step
        time.step()


    # Some logging before shutting down
    logger.info(f'Simulation ended after {time.real} ({time.real.steps} steps) at a mean rate of {time.real.steps / time.real.time:.2f} steps per second.')
    logger.info(f'Final state of the simulated universe:\n{time.simulation}' + ''.join([f'\n{body}' for body in bodies]))



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




# Keyboard listener to exit simulation loop when `esc` is pressed
def on_press(key) -> None:
    global running
    if key == keyboard.Key.esc:
        running = False
