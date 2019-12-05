import numpy as np
from matplotlib import pyplot as plt
# 进度条
from tqdm import tqdm
# 统计时间
import time

time.perf_counter()
start = time.time()

# set parameters
n_samples = 10000
n_step = 10000
# 在（0，0）生成黑洞
# 在以（0，0）为圆心，r=sqrt(n_samples)的圆盘内生成均匀的点

# genarte data

# initial condition
r = np.random.uniform(0, n_samples**0.5, n_samples)
theta = np.random.uniform(0, 2*np.pi, n_samples)
x = r*np.cos(theta)
y = r*np.sin(theta)
vx = np.random.normal(size=n_samples)
vy = np.random.normal(size=n_samples)

# random walk
x_rand = []
y_rand = []
print("Genarating data>>>")
for i in tqdm(range(n_step)):
    x_rand.append(np.random.random(n_samples) *
                  np.cos(np.random.uniform(0, 2*np.pi, 10000)))
    y_rand.append(np.random.random(n_samples) *
                  np.sin(np.random.uniform(0, 2*np.pi, 10000)))

# caculate
print("Caculating>>>")
n = 0
for step in tqdm(range(n_step)):
    r2 = x**2 + y**2
    F = 10 / r2**1.5
    ax = -F * x
    ay = -F * y
    vx += ax
    vy += ay
    x += x_rand[step] + vx
    y += y_rand[step] + vy

    # save figure
    '''
    if (step % 100 == 0):
        plt.plot(x, y, 'bo', markersize=3, alpha=0.2)
        plt.xlim(-n_samples*5, n_samples*5)
        plt.ylim(-n_samples * 5, n_samples * 5)
        plt.savefig('./fig/%d.png' % n)
        plt.cla()
        n = n+1
    '''


end = time.time()
elapse = end - start
print('total time: ' + str(elapse))


plt.figure(figsize=(10, 10))
grid = plt.GridSpec(4, 4, wspace=0.5, hspace=0.5)

main_ax = plt.subplot(grid[1:4, 0:3])
plt.plot(x, y, 'bo', markersize=3, alpha=0.2)
plt.xlim(-n_samples*5, n_samples*5)
plt.ylim(-n_samples*5, n_samples*5)

y_hist = plt.subplot(grid[1:4, 3], xticklabels=[], sharey=main_ax)
plt.hist(y, 30, range=(-40000, 40000), orientation='horizontal', color='blue')

x_hist = plt.subplot(grid[0, 0:3], xticklabels=[], sharex=main_ax)
plt.hist(x, 30, range=(-40000, 40000), orientation='vertical', color='blue')

plt.show()
