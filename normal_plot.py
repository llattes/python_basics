import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1000 simulations of die roll
n = 10000

avg = []
for i in range(1,n):
    a = np.random.randint(1,7,10)
    avg.append(np.average(a))

# CHANGED: normalise this histogram too
plt.hist(avg[0:], 20, density=True)

zscore = stats.zscore(avg[0:])

mu, sigma = np.mean(avg), np.std(avg)
s = np.random.normal(mu, sigma, 10000)

# Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, density=True)

# Use scipy.stats implementation of the normal pdf
# Plot the distribution curve
x = np.linspace(1.5, 5.5, num=100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))

plt.show()
