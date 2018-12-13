import matplotlib.pyplot as plt
import numpy as np
import math

grados = np.arange(180)
x = (-grados/360)*2*math.pi
y = -(np.cos(x)-1)


plt.plot(x,y)
plt.show()

print(x)
