
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.barh(df["x"], df["y"], color='green')
plt.ylabel("X values")
plt.xlabel("Y values")
plt.title("X vs Y Horizontal Bar Plot")
plt.grid(True, axis='x')
plt.show()
