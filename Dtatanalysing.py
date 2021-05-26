import numpy as np
import pandas as pd
df = pd.DataFrame(np.array([[2, 2], [3, 20], [4, 200], [5, 200]]),
                  columns=['p', 'q'])
print(df.quantile(.1))

print(df)



df.quantile(0.5)
df.p.median()
import matplotlib.pyplot as plt

import seaborn as sns

plt.figure(figsize= (15,8))
sns.boxplot(df)
plt.show()



"""to get the value of Q1 that is quartile1 formula is Q1= [(n+1)/4]"""


"""Q1 = [(n+1)/4] th item
N
that means it is giving us the position of that quartile. 1.5 means the 1.5th term of the series"""


""""to get the value of Q1 that is quartile1 formula is Q1= [(n+1)/4]
Quartile1 is equals to 0.25 quantile.
n = total num of elements in an array or series
these values are helpful in analysing the distribution of data.
N
so for that we plot boxplot
[(8+1)/4] = 2.25
N
just a min
ok
Q1 = [(n+1)/4] th item
N
that means it is giving us the position of that quartile. 1.5 means the 1.5th term of the series"""
