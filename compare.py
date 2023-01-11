import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a = 0.9
b = 0.6
n = [1,5,10,20,50,100]

k = np.arange(0. , 1.01, 0.01)


for i in range(6):
    k = np.arange(0, n[i]+1)
    x1 = np.linspace(0, 1, n[i]+1)
    #print(x1)
    plt.subplot(4,3,i+1)
    binom_pmf_before = stats.binom.pmf(k, n[i], b)
    plt.plot(x1, binom_pmf_before, color = "red")
    #print(binom_pmf)

for i in range(6):
    k = np.arange(0, n[i]+1)
    x2 = np.linspace(0, 1, n[i]+1)
    #print(x2)
    plt.subplot(4,3,i+1)
    binom_pmf_after = stats.binom.pmf(k, n[i], a)
    plt.plot(x2, binom_pmf_after, color = "blue")
    #print(binom_pmf)

plt.title("比較")
plt.xlabel("t")
plt.ylabel("y")

plt.show()