# PythonNewtBox
An N-body orbital simulator written in Python. Created in 2025 by Skyler Alderson. This project was completed within a single day (June 23rd).

My series of "NewtBox" (or Newton Sandbox) simulations are Newtonian N-body orbital simulators I use to learn a new language. I find reimplementing a familar project is a good way to get a grasp on an unfamiliar language.

This is an exception; rather, it is a portfolio piece. A problem of using a project like this to learn a new language is that one has yet to understand the intent behind the languages choices. As such, my NewtBoxes are rough around the edges since at their creation I had yet to master their languages. Now that I have learned much about Python, I want to showcase some better practices.

To run this project, get a local instance (git clone ...), navigate into its directy, and run `python main.py`. If you do not have the required libraries, run `pip install -r requirements.txt` while in the project directory. This project requires Python3.10+.

To end a simulation, hit the `escape` key.


## Running a Simulation
To run a simulation, enter the command `python main.py` while in the project directory. To adjust the parameters, change the variables found within `main.py`.


### Simulation Parameters
To adjust the seconds simulated per step, change the `t` variable (`t: Decimal = ...`). Valid values include: `SECOND`, `MINUTE`, `HOUR`, `DAY`, and `YEAR`. Alternatively, enter any Decimal value (e.g. `t: Decimal = Decimal('3.14')).

To change the set of planets simulated, there are two options. The first option is one can use a present (currently just `'default'` and `'simple'`) in the line `factory.create(...)`. `'default`' is all celestial bodies currelty listed in `data/bodies.json`; `'simple'` is the sun-earth-moon system. The second option is manually adding a set of bodies. This involves calling `factory.add(x)` where `x` is the string name of the body (a complete list can be found in `data/bodies.json`) or a Body object (see: `body.py`).

Finally to supress prints to either the console or to file, change the level parameters in `logs_setup(...)` to `logging.warning`.


## src
### body.py
A body is a celestial object. It has a name, mass, as well as a position, velocity, and acceleration vector.

A custom Body object can be created through `Body()`, which much be supplide with the following arguments: `name`, and `mass`. Optional key-word arguments are: `pos` to set the initial position, `vel` to set initial velocity, and `acc` to set initial acceleration.


### constants.py
This file stores several constants such as G, the gravitational parameter.


### logging.py
This is responsible for setting up the logger. This project uses the default `logging` library for this ends. By default, only the five most recent logs are kept.

When calling `logs_setup(...)`, the logging level can be changed to supress output: use `logging.warning` to do so.


### simulate.py
The primary simulation loop is in this file. It tracks the time from the simulation's start both from the perspective of our time and the simulation's time. In addition, the loop applies gravity between all unique pairs of bodies in every simulation step as well as updating each body each step.

This file also listens for the user pressing the `escape` key. If it is pressed, the simulation ends.


### solarsytem.py
This file contains a factory object which creates solar systems for the simulation. It contains a list of current bodies. New bodies can be added to the list by calling `SolarSystemFactory.add(x)` where `x` is the string name of the body (for a complete list, see `data/bodies.json`) or a Body object (see: `body.py`). Then, by calling `SolarSystemFactory.spawn()`, the factory will create and return the list.

When a body is added via the `.add()` method and a string name is supplied, if the body has a parent it's position will automatically be added onto the position vector of its parent body. In effect, this places the child body relative to its parent. Additionally by adding a body in the way `.add()`, the velocity is automatically set by using the planet's semi-major axis, assuming the orbit has e = 0 (i.e. a circular orbit).

If a body is instead added via `.add()` and supplying a Body object, no adjustments are made and the body is added as is.


### time.py
This file is responsible for class that keep track of time. It includes: `Time`, `Times`, and `Stopwatch`.

The `Time` class has three parameters: `t`, the seconds per step; `steps`, the total simulation steps elapsed; and, `time`, the total time elapsed. The point of this object is to bunlde that information together with a nice to-string.

`Stopwatch` is used to track the time elapsed since a particular event. It is used to enfore timed events; namely, for this project, logging events use a stopwatch to ensure not too much time is wasted writing to output. In addition, `Stopwatch` is used to track the time between simulation steps, ensuring the real time clock remains accurate.

The (poorly named) `Times` class is a wrapper for two `Time` objects and a `Stopwatch`. It tracks real world time and universe time.


# vector.py
The `Vector` class is a three component vector. It used the `Decimal` data type from the `decimal` library to store its components. `Decimals` are fixed-point numbers, preventing drift that would otherwise be introduced when using floats. This project uses the default 28 digits of precision since this is meant to be a showcase more than a hyper-accurate simulation.

The `Vector` class mostly contains arithmetic operations, such as add, multiply, dot- and cross-product, and so on. It also contains a method to find the magnitude of the vector and its normal vector.


## Other directories
### data
The `data` directory contains data for celestial objects. At the moment, it contains major planetary bodies, several notable moons, Ceres and Pluto, as well as the sun.

Each entry consists of a name, its parent body if it has one, a mass in kilograms, a semi-major axis measured in kilometres, and a period measured in days. This file was created using generative AI to search and compile the data; this was the only use of AI in this project.


### logs
The log files are kept in the `logs` directory. Only the five more recent logs are kept.
