import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm

from fitting_functions import *

data=np.loadtxt("tips.csv", delimiter=",", dtype=str)

x=data[1:,0].astype(np.float32)
y=data[1:,1].astype(np.float32)
pct_tip=data[1:,6].astype(np.float32)

x_units= "dollars"
y_units="dollars"

bill_ends=np.array([x.min(), x.max()])

tip_params, tip_cov =scipy.optimize.curve_fit(linear, x, y)
tip_slope=tip_params[0]
tip_intercept=tip_params[1]

fig = plt.figure()
plt.scatter(x, y)
plt.plot(bill_ends, linear(bill_ends, tip_slope, tip_intercept), color="red")
plt.xlabel("Bill (dollars)")
plt.ylabel("Tip (dollars)")
fig.savefig("plot_tips.png")

print(print_equation(tip_slope, tip_intercept, x_units, y_units))

pct_params, pct_cov=scipy.optimize.curve_fit(linear, x, pct_tip)
pct_slope=pct_params[0]
pct_intercept=pct_params[1]

fig_pct = plt.figure()
plt.scatter(x, pct_tip)
plt.plot(bill_ends, linear(bill_ends, pct_slope, pct_intercept), color="red")
plt.xlabel("Bill (dollars)")
plt.ylabel("Tip percentage (%)")
fig_pct.savefig("plot_pct_tip.png")

print(print_equation(pct_slope, pct_intercept, x_units, "%"))

plt.show()
