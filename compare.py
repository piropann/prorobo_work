import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a = 0.9
b = 0.6
n = 20

for i in range(n):
    k = np.arange(0, n+1)
    x1 = np.linspace(0, 1, n+1)
    #print(x1)
    binom_pmf_before = stats.binom.pmf(k, n, b)
    #print(binom_pmf)

for i in range(n):
    k = np.arange(0, n+1)
    x2 = np.linspace(0, 1, n+1)
    #print(x2)
    binom_pmf_after = stats.binom.pmf(k, n, a)
    #print(binom_pmf)
#y1 = np.linspace(0.01, 0.01, 101)

plt.title("比較")
plt.xlabel("t")
plt.ylabel("y")

plt.plot(x1, binom_pmf_before, color = "red")
plt.plot(x2, binom_pmf_after, color = "blue")
#plt.plot(x2, y2, marker = "A", color = "blue")

plt.show()