
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.hist(df["y"], bins=10, color='green', edgecolor='orange')
plt.xlabel("Y values")
plt.ylabel("Frequency")
plt.title("Histogram of Y values")
plt.grid(True, axis='y')
plt.show()
