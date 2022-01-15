import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Set the seed
np.random.seed(123)

all_walks = []

for i in range(10000):
    # Initialize random_walk
    random_walk = [0]

    # 1 or 2    > 1 step down
    # 3, 4 or 5 > 1 step up
    # 6         > throw the die again and climb the result
    for x in range(100):
        # Starting step
        step = random_walk[-1]

        # Roll the dice
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)
        elif 2 < dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        # Implement clumsiness
        if np.random.rand() < 0.001:
            step = 0

        # append next_step to random_walk
        random_walk.append(step)
    all_walks.append(random_walk)

# Transpose np_aw: np_aw_t
all_walks_transposed = np.transpose(np.array(all_walks))

# Print out all random walks numpy array shape
print(all_walks_transposed.shape)

# Select last row from np_aw_t: ends
ends = all_walks_transposed[-1, :]
simulations = len(ends)
sixtieth_or_over_floor = len(ends[ends >= 60])

mean = np.mean(ends)
std = np.std(ends)

print("Estimated probability: " + str((sixtieth_or_over_floor / simulations) * 100))
print("Normal probability with mean and std: " + str((1 - stats.norm(loc=mean, scale=std).cdf(60)) * 100))
print("Mean: " + str(mean) + "; Standard Deviation: " + str(std))
print("Min. value: " + str(np.min(ends)) + "; Max. value: " + str(np.max(ends)))

# Plot histogram of ends, display plot
plt.hist(ends, bins=30)

# Plot a histogram of random samples of a normal with mean and std
# s = np.random.normal(mean, std, 100000)
# plt.hist(s, 100, density=False)

# Create a normal distribution line scaled to match the original histogram
x_axis = np.linspace(0, 130, num=100)
max_density = stats.norm.pdf(mean, mean, std)
counts, bin_edges = np.histogram(ends, bins=30)
scale = max(counts) / max_density
plt.plot(x_axis, scale * stats.norm.pdf(x_axis, mean, std))

# Show the plot
plt.show()
