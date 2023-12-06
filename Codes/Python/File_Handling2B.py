import matplotlib.pyplot as plt

# Open File
f = open("simdata.txt", "r")

t = []; x = [] #empty list definitions

for record in f:
    record = record.replace("\n", "") #remove \n character
    time, value = record.split("\t")
    t.append(int(time)) 
    x.append(float(value))

f.close()

# Plot the File Data
plt.plot(t,x)
plt.title('Simulation of Dynamic System')
plt.xlabel('t'); plt.ylabel('x')
plt.grid()
plt.show()
