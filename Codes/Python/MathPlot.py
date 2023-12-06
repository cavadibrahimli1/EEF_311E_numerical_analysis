# Plot
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 2,4, 4, 8, 7, 4, 8, 10, 9]

plt.plot(x,y)
plt.xlabel('Time (s)')
plt.ylabel('Temperature (degC)')
plt.show()

# %%
x1 = [0, 1, 2, 3, 4, 5, 6, 7]
y1 = np.sin(x1)  

plt.plot(x1, y1,'k-.')
plt.plot(x1, y1+0.5,'m--') #plots on the current figure
plt.xlabel('x'); plt.ylabel('y'); plt.show()

# %%
xstart = 0
xstop = 2*np.pi
increment = 0.1

x2 =np.arange(xstart,xstop,increment)
y2 = np.sin(x2)

plt.plot(x2, y2,'r*')
plt.xlabel('x'); plt.ylabel('y')
plt.grid();plt.show()

# %%
xstart = 0
xstop = 2*np.pi
increment = 0.1

x3 =np.arange(xstart,xstop,increment)
y3 = np.sin(x2); y4 = np.cos(x2)

plt.plot(x3, y3,'r*', x3, y4, 'c')
plt.xlabel('x')
plt.ylabel('cos & sin curves')
plt.grid()
plt.show()
# %% Sub-plot
xstart = 0 
xstop = 2*np.pi 
increment = 0.1

x = np.arange(xstart,xstop,increment)
y = np.sin(x)

plt.subplot(2,1,1)
plt.plot(x, y)
plt.title("Subplot Example")
plt.xlabel('x')
plt.ylabel('sin(x)')

z = np.cos(x)

plt.subplot(2,1,2)
plt.plot(x, z)
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid()
plt.show()