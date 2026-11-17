import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm

from fitting_functions import *

data=np.loadtxt("tips.csv", delimiter=",", dtype=str)

x=data[1:,0].astype(np.float32)
y=data[1:,1].astype(np.float32)

print(x)
print(y)

fig=plt.figure()
plt.scatter(x_data, y_data)
plt.xlim(xmax = 12.0, xmin = 0)
plt.xlabel("t (s)")
plt.ylabel("speed (m/s)")
fig.savefig('plot_tips.png')
