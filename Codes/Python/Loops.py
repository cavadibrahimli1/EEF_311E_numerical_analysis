data = [1, 5, 6, 3, 12, 3]

sum = 0
for x in data:
    sum += x  

print(sum)

N = len(data)
mean = sum/N
print(mean)

# %%
cars = ["Ford", "Toyota", "Tesla"]

marka = cars[1]

x = len(cars)

cars.append("Porche")
cars.remove("Tesla")
cars.sort()


for car in cars:
    print(car)
# %% While loop
import numpy as np
import matplotlib.pyplot as plt

xstart = -20
xstop = 20
increment = 0.1

x = np.arange(xstart,xstop,increment)  
y = 2 * x**2 + 20 * x - 22

plt.plot(x,y)
plt.grid
i = 0

while y[i] > y[i+1]:  
    i = i+1

print(x[i]) 
print(y[i]) #min value 


