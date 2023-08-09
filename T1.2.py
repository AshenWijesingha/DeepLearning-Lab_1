import matplotlib.pyplot as plt

plt.hist(np.random.exponential(1, 100000), density=True, bins=100, histtype="step", color="blue", label="exponential")
plt.hist(np.random.rand(100000), density=True, bins=100, histtype="step", color="green", label="uniform")
plt.hist(np.random.normal(0, 1, 100000), density=True, bins=100, histtype="step", color="red", label="normal")
plt.legend(loc = "upper left")
plt.title("Random distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
