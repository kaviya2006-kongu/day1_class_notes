
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.boxplot(df["y"], patch_artist=True, boxprops=dict(facecolor='green'))
plt.title("Box Plot of Y values")
plt.ylabel("Y values")
plt.grid(True, axis='y')
plt.show()
