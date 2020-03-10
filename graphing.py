import numpy as np
from matplotlib import pyplot as plt

x = range(1,301)
y = np.loadtxt("cumulative_rewards.txt")
plt.title("Learning Curve")
plt.xlabel("number of runs")
plt.ylabel("cumulative reward for run")
plt.plot(x,y,"ob")
plt.show()