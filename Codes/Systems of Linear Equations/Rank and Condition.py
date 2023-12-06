#Rank and condition
import numpy as np

# A = np.array([[1,1,0],[0,1,0],[1,0,1]])
A = np.array([[1,1,0],[0,1,0],[2,2,0]]) #inconsistent solution
print("\nMatrix:\n", A)

print("Condition number:\n", np.linalg.cond(A))
print("Rank:\n", np.linalg.matrix_rank(A))

B = np.array([[1], [2], [1]])

A_y = np.concatenate((A, B), axis = 1)
print("\nAugmented matrix:\n", A_y)
print("Rank of augmented:\n", np.linalg.matrix_rank(A_y))

#If rank(A) = rank(A|B) = the number of rows in matrix
if (np.linalg.matrix_rank(A)==np.linalg.matrix_rank(A_y)==np.shape(A)[0]):
    print("rank(A) = rank(A|B) = the number of rows. \
# \nThe system has a unique solution. ", end='')
elif (np.linalg.matrix_rank(A)==np.linalg.matrix_rank(A_y)<np.shape(A)[0]):
    print("The system has infinite number of solutions.")
elif (np.linalg.matrix_rank(A)<np.linalg.matrix_rank(A_y)):
    print("rank(A) = rank(A|B) < the number of rows. \
          \nThe system is inconsistent.")
#%%    
coefficients = np.linalg.solve(A, B)
print(f"\nSolution is:\n{coefficients}")