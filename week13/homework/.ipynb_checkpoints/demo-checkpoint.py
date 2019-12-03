from tqdm import tqdm
import numpy as np
from matplotlib import pyplot as plt
 

def F(pos):
    r = (pos[0]**2+pos[1]**2)**0.5
    if r==0:
        r = 0.1
    if pos[0] != 0:
        if pos[0] > 0:
            theta = np.arctan(pos[1]/pos[0])+np.pi
        else:
            theta = np.arctan(pos[1]/pos[0])
    elif pos[1] > 0:
        theta = np.pi/2
    elif pos[1] < 0:
        theta = -np.pi/2
    else:
        theta = np.random.random()*2*np.pi
    return np.array([0.5/r*np.cos(theta), 0.5/r*np.sin(theta)])


class Singledot():

    def __init__(self, pos0=[0,0]):
        self.pos = pos0
        
    def walk(self, pos, n=1):
        for i in xrange(n):
            step = np.random.random()
            theta = np.random.random()*2*np.pi
            dx =  F(pos)[0] + np.cos(theta)*step
            dy =  F(pos)[1] + np.sin(theta)*step
            temp = np.array([dx,dy])


plt.figure(figsize=(8,8))
for i in tqdm(range(100)):
    point = Singledot([np.random.randint(-5,5), np.random.randint(-5,5)])
    point.walk(point.pos, 10000)
    plt.scatter(point.pos[0], point.pos[1])
plt.show()