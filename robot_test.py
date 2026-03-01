import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as CirclePatch

robot_name = "monkey"
battery_level = 100.0
position = np.array([0.0, 0.0])
velocity = np.array([1.0, 1.5])
obstacle_pos = np.array([4.5, 4.5])
obstacle_size = 1.0

test = position + velocity
print(test)
is_running = True

def move(current_position, speed):
    noise = [random.uniform(-0.1, 0.1),random.uniform(-0.1, 0.1)]

    real_distance = speed + noise

    new_position = current_position + real_distance
    return new_position

def obstacle(robot_pos, obs_pos,obs_size):
    distance = np.linalg.norm(robot_pos - obs_pos)
    if distance < obs_size:
        return True
    else:
        return False

print(f"[{robot_name}] System Start...")

fig = plt.figure()
plt.ion()




while is_running:
    if battery_level < 20:
        print("Warning: Low Battery!")
        is_running = False
        break

    position = move(position, velocity)
    if obstacle(position, obstacle_pos, obstacle_size):
        print("Warning: Obstacle!")
        is_running = False
        break

    battery_level -= 5.0

    print(f"Status: Moving | Pos: [{position[0]:5.2f}m, {position[1]:5.2f}m | Battery Level: {battery_level}%" )
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 30)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    ax.plot(position[0], position[1], 'ro')
    draw_circle = plt.Circle((obstacle_pos[0],obstacle_pos[1]), radius=obstacle_size)
    ax.set_aspect(1)
    ax.add_artist(draw_circle)
    plt.pause(0.5)
 #   time.sleep(0.5)

plt.ioff()
plt.show()
print("System Shutdown.")
