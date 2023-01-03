import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a = 0.9
b = 0.6
n = 5
k = np.arange(0, n+1)

x1 = np.linspace(0, 1, n+1)
print(x1)
binom_pmf = stats.binom.pmf(k, n, p)
print(binom_pmf)
#y1 = np.linspace(0.01, 0.01, 101)

plt.title("比較")
plt.xlabel("t")
plt.ylabel("y")

plt.plot(x1, binom_pmf, color = "red")
#plt.plot(x2, y2, marker = "A", color = "blue")

plt.show()