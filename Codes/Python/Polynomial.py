import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

xstart = 0
xstop = 2*np.pi
increment = 0.1

x = np.arange(xstart,xstop,increment)
y = np.sin(x)
plt.plot(x, y, label="sin()")

N = 5
p = poly.polyfit(x,y,N)  
print(p)

y2 = poly.polyval(x, p)
plt.plot(x, y2,label="New Function")  
plt.legend()
plt.grid()
plt.show()
