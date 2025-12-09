
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
plt.pie(df["y"], labels=df["x"], autopct="%1.1f%%", startangle=90, colors=plt.cm.Greens(np.linspace(0.3, 0.8, len(df))))
plt.title("Pie Chart of Y values by X categories")
plt.axis("equal")
plt.show()
