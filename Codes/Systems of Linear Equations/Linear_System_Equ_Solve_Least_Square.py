import numpy as np

A = np.array([[1, 2],
[3, 4],
[7, 8]])
b = np.array([[5],
[6],
[9]])

x = np.linalg.lstsq(A, b, rcond=None)[0]

print("Solution is x=%.3f, y=%.3f" %(x[0], x[1]))
