# Round off errors
4.9 - 4.845 == 0.055 #round off error
0.1 + 0.2 + 0.3 == 0.6

# If we only do once answer is 
1 + 1/3 - 1/3

#round off error is accumulated
x=1
for i in range(5):  x+=1/3
for i in range(5):  x-=1/3
print(x)
