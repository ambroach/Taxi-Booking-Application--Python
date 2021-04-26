import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 2),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df)

r = df.rolling(window=3,min_periods=1)
print (r.aggregate(np.sum))
x