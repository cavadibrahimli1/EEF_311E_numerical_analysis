#Jacobian Iterative
from numpy.linalg import matrix_rank
from numpy import array, shape, empty, full, copy, newaxis, concatenate

# x1-5x2=-4; 7x1-x2=6
a = array([[1, -5],[7, -1]],float)
b = array([-4, 6], float)

# -5x2+x1=-4; -x2+7x1=6
# a = array([[-5, 1],[-1, 7]],float)
# b = array([-4, 6], float)

b = b[:,newaxis] #vector to matrix conversion, new dimension added
A_y = concatenate((a, b), axis = 1)
print(f"Rank of matrix:{matrix_rank(a)}, augmented matrix:{matrix_rank(A_y)}")
#%%
n = shape(b)[0]
x = full(n, -1.0, float)  #initial guess of "x" is important
xnew = empty(n, float)
iterlimit = 100; tolerance = 1.0e-6

# iterations:
for iteration in range(iterlimit):
    for i in range(n): # for all the rows of matrix, xnew is calc.
        s = 0
        for j in range(n): 
            if j != i:
                s += a[i, j]*x[j] #matrix multiplication for each row
        xnew[i] = (b[i]-s) / a[i,i]
    
    if (abs(xnew - x) < tolerance).all(): break
    else: x = copy(xnew)
    
print('\nNumber of iterations: %d '% (iteration+1))
print('The solution of the system:\n', x)



