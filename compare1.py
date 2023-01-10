import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


m = [1,2,2,2,3,4]
n = [1,1,2,3,3,3]
a, b = np.array(m),np.array(n)


s = [1,2,3,4,5,6]
t = [1,1,1,1,1,1]
c, d = np.array(s),np.array(t)

x = np.arange(0. , 1.01, 0.01)

y = np.zeros([x.shape[0], a.shape[0]])
z = np.zeros([x.shape[0], c.shape[0]])

plt.title("比較")
plt.xlabel("t")
plt.ylabel("y")

for i in range(a.shape[0]):
    y[:,i] = stats.beta.pdf(x,a[i],b[i])
    plt.subplot(4,3,i+1)
    plt.plot(x, y[:,i], color = "red")

for i in range(a.shape[0]):
    z[:,i] = stats.beta.pdf(x,c[i],d[i])
    plt.subplot(4,3,i+7)
    plt.plot(x, z[:,i], color = "blue")

plt.show()