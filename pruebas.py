import numpy as np
import matplotlib. pyplot as plt

plt.plot([0,1,2],[0,1,4],"rd-")

x = np.logspace(0,1,10)
y = x**2
plt.loglog(x,y,"bo-")

plt.subplot(333)
plt.subplot(3, 3, 3)