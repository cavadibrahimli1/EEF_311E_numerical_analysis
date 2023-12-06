import math as mt
import numpy as np

# Open File
f = open("simdata.txt", "w")

def writedata(t, x):
    time = str(t)
    value = str(round(x, 2))
    f.write(time + "\t" + value)
    f.write("\n")

# Simulation Parameters
x = np.zeros(25+1)
t = np.arange(0, 25+1, 1)

for k in range(25+1):
    x[k] = mt.exp(0.1*t[k]) 
    writedata(t[k], x[k])
    
f.close()
