import numpy as np

a = np.array([[2, 7, -1, 3, 1], [2, 3, 4, 1, 7], [6, 2, -3, 2, -1],
           [2, 1, 2, -1, 2], [3, 4, 1, -2, 1]],float)
b = np.array([5, 7, 2, 3, 4], float)
b = b[:,np.newaxis] #vector to matrix conversion, new dimension added

n = len(b) #number of unknown parameters
x = np.zeros(n, float) #solution arra for the unknown values

A_y = np.concatenate((a, b), axis = 1)
print(f"Rank of matrix:{np.linalg.matrix_rank(a)} \
      \nRank of augmented matrix:{np.linalg.matrix_rank(A_y)}\n")
      
def yazdirM(M):
    for i in range( M.shape[0]):
        for j in range( M.shape[1] ):
            print("%7.2f" %M[i,j], end="")
            if j==n-1: print("")        

print("Given Matrix")
yazdirM(a); print()

#%% Elimination           
for k in range(n-1): #except last column
    for i in range(k+1, n): #for each row
        fctr = a[k, k] / a[i, k]
        # k value also indicates diagonal element's row
        # current row is substracted from the diagonal element's row
        b[i] = fctr*b[i] - b[k]
        for j in range(k, n):
            a[i, j] = fctr*a[i, j] - a[k, j]
        #***
        yazdirM(a); print()
            
print('\nEliminated System:')
yazdirM(a)
#%% Back-substitution
x[n-1] = b[n-1] / a[n-1, n-1] # from the bottom row unknown x[n-1] value is cal.

for i in range(n-2, -1, -1): #from (n-2)th row all x values are cal. 
    terms = 0
    for j in range(i+1, n):
        terms += a[i, j]*x[j]
    x[i] = (b[i] - terms)/a[i, i]
    # from bottom to top each "x" value is calculated

print('\nThe solution of the system:')
for i in range(len(x)): print("%.2f" %x[i], end=' ')