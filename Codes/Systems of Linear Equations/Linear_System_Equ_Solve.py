import numpy as np
# x1 + 2*x2 = 5
# 3*x1 + 4*x2 = 6
A = np.array([[1, 2], [3, 4]])
b = np.array([[5],[6]])

Ainv = np.linalg.inv(A)
x = np.dot(Ainv,b) #matrix product

print("Solution is x=%.3f, y=%.3f" %(x[0], x[1]))

xp = np.linalg.solve(A, b)
print("Solution with Phyton built-in function is x=%.3f, y=%.3f" %(x[0], x[1]))
