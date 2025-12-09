
import numpy as np
import pandas as pd
np.random.seed(44)
data = {
    "x" : np.arange(1,15),
    "y" : np.random.randint(48,160,size=14)
}
df = pd.DataFrame(data)
print(df)
