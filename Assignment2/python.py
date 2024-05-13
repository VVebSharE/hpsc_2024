# python script that takes n files as input and output an animation for the particles
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Particle:
    def __init__(self,filePath):
        self.fileData = None

        with open(filePath) as f:
            lines = f.readlines()
            self.fileData = np.array([[float(x) for x in line.split(" ")] for line in lines])

    def position(self,i):
        '''
            returns the position of the particle at the ith time step
            returns a tuple of the x and y coordinates of the particle at the ith time step
        '''
        return [self.fileData[i][1],self.fileData[i][2]]
    
    def velocity(self,i):
        '''
            returns the velocity of the particle at the ith time step
            returns a tuple of the x and y components of the velocity of the particle at the ith time step
        '''
        return [self.fileData[i][3],self.fileData[i][4]]


parser = argparse.ArgumentParser(description='Process command line args')

# for the folder containing the .txt files
parser.add_argument("--r","--root",default="./particles", type=str, help="Root directory of the .txt files each for a particle")


##-----------things for animation using FuncAnimation------------

def init():
    particle.set_data([], [])
    return (particle,)


def animate(frame):
    global position, ani, num_steps

    if frame >= num_steps:
        # Stop the animation when the desired output duration is reached
        ani.event_source.stop()
        return (particle,)


    position0 = [Particles[i].position(frame)[0] for i in range(n)]
    position1 = [Particles[i].position(frame)[1] for i in range(n)]

    # print("Position",position0,position1)

    particle.set_data(position0, position1)

    return particle,


##---------------------------------------------------------------

n=None
num_steps = None
radius = 0.05

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Initialize empty particle plot
particle, = ax.plot([], [], "bo", markersize=radius * 400)


if __name__ == "__main__":
    args = parser.parse_args()

    # root = args.r
    root = "C:\\Users\\Vaibhav\Desktop\\vaibhav programming\\Mtech_sem2\\HPSC"


    # all txt files in the root directory
    PFiles = [name for name in os.listdir(root) if name.endswith(".txt")]

    n = len(PFiles)


    Particles = [Particle(os.path.join(root, i)) for i in PFiles]

    num_steps = len(Particles[0].fileData)

    ani = FuncAnimation(
        fig, animate, frames=num_steps + 1, init_func=init, blit=True, interval=10
    )

    plt.show()

    plt.close()
