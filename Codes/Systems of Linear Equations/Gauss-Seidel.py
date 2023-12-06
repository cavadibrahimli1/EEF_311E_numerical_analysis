#Gauss Seidel Method
import numpy as np
# x1-5x2=-4; 7x1-x2=6
a = np.array([[1, -5],[7, -1]],float)
b = np.array([-4, 6], float)

# -5x2+x1=-4; -x2+7x1=6
# a = np.array([[-5, 1],[-1, 7]],float)
# b = np.array([-4, 6], float)

n = np.shape(b)[0]
x = np.full(n, 0, float)  #initial guess of x values
xdiff = np.empty(n, float) #for tolerance calculation
iterlimit = 100; tolerance = 1.0e-6

# iterations:
for iteration in range(iterlimit):
    for i in range(n):
        s = 0
        for j in range(n): 
            if j != i:
                s += a[i, j]*x[j] #matrix multiplication for each row
        xnew = (b[i]-s) / a[i,i]
        xdiff[i]=abs(xnew-x[i])
        x[i]=xnew #calculated x[i] value is used in the calculations
                
    if (xdiff < tolerance).all():
        break
else:
    print("Iteration limit reached!!!!")

print('Number of iterations: %d '% (iteration+1))
print('The solution of the system:\n', x)
#%% Convergence
c = np.empty(n, float) 
#for the sum of the absolute values of the non diagonal elements of the matrix in a row
d = np.empty(n, float) #diagonal elements of the matrix

for i in range(n):
    s = 0
    for j in range(n): # for all the rows of matrix, xnew is calc.
        if j != i: s += abs(a[i, j])
        else: d[i]=abs(a[i, j]) #diagonal element values
    c[i]=s
    
if ((d - c) > 0).all():
    print("Gauss Seidel Method converge")
else:
    print("Gauss Seidel Method does not converge")