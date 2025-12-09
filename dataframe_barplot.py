
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(44)
data = {
    "x": np.arange(1, 15),
    "y": np.random.randint(48, 160, size=14)
}
df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(8, 5))
plt.bar(df["x"], df["y"], color='green')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("X vs Y Bar Plot")
plt.grid(True, axis='y')
plt.show()
