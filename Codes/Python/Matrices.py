import numpy as np

A = np.array([[0, 1],[-2, -3]])
B = np.array([[1, 0],[3, -2]])

C = A + B
print("A+B =", C)

C = A - B
print("A-B =", C)

C = A * B
print("A*B =", C) # Not Working!, only elementwise Multiplication!

#Working Alternative 1
C = A.dot(B)
print("A*B =", C)

#Working Alternative 2
C = np.dot(A,B)
print("A*B =", C)
# %%
import numpy as np

A = np.array([[1, 3, 7, 2],
		[5, 8, -9, 0],
		[6, -7, 11, 12]])
print("A="); print(A)
Atr = np.transpose(A)

print("Transpose of A="); print(Atr)
# %%
import numpy as np
import numpy.linalg as la

B = np.array([[-1, 3, 0], [2, 1, -5], [1, 4, -2]])

print("Matrix is\n",  B)

Bdet = la.det(B)
print("Determinant of matrix is %.3f" %Bdet)

Binv= la.inv(B)

print("Inv of of matrix is:\n", Binv)
