#ill-conditioned matrix
import numpy as np
from numpy.linalg import cond

# x+y=2, x+1.001y=2
A = np.array([[1,1],[1,1.001]])
b = np.array([[2],[2]])
print("Equations: x+y=2, x+1.001y=2")
coefficients = np.linalg.solve(A, b)
print("Condition number of the matrix:%.2f" %cond(A))
print(f"Solution is:\n{coefficients}")

# x+y=2, x+1.001y=2.001
print("\nEquations: x+y=2, x+1.001y=2.001")
b1 = np.array([[2],[2.001]])
coefficients1 = np.linalg.solve(A, b1)
print("Condition number of the matrix:%.2f" %cond(A))
print(f"Solution is:\n{coefficients1}")

