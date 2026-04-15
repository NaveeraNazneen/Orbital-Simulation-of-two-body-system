import numpy as np
import matplotlib.pyplot as plt

# Conatants
G = 0.9999999# Simplified Gravitation constant ,closer to 1, but not exactly 1, to show the unique shape of planetary motion, when a variable is changed, for mos tcases it is kept 1. 

#Planet class
class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)

def compute_force(body1, body2):
    r = body2.position - body1.position
    distance = np.linalg.norm(r)
    force = G * body1.mass * body2.mass * r / distance**3
    return force

# Creating planetary and star (sum) bodies
sun = Body(1000, [0, 0], [0, 0])
planet = Body(1, [10, 0], [0, 3])

bodies = [sun, planet]

# Simulation
dt = 0.01
steps = 5000

positions = []

for _ in range(steps):
    forces = []

    for body in bodies:
        total_force = np.array([0.0, 0.0])
        for other in bodies:
            if body != other:
                total_force += compute_force(body, other)
        forces.append(total_force)

    for i, body in enumerate(bodies):
        acceleration = forces[i] / body.mass
        body.velocity += acceleration * dt
        body.position += body.velocity * dt

    positions.append(planet.position.copy())

# Ploting
positions = np.array(positions)
plt.plot(positions[:,0], positions[:,1])
plt.scatter(0, 0, color='orange', label='Sun')
plt.title("Planet Orbit Simulation")
plt.legend()
plt.show()
