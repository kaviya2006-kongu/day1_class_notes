
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.bar(df["x"], df["y"], color='green')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("X vs Y Bar Plot")
plt.grid(True, axis='y')
plt.show()
