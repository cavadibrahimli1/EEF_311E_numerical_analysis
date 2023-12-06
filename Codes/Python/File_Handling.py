#File Handling
Title="Title:Since we will be working with numerical methods later...."

f=open("Sample.txt", 'w')
f.write(f"{Title}\n")

for i in range(1,7,1):
    if i==1: f.write("The 1st line\n")
    elif i==2: f.write("The 2nd line\n")
    elif i==3: f.write("The 3rd line\n")
    else: f.write(f"The {i}th line\n")

f.close()
# %% Read all the text

f=open("Sample.txt", 'r')
Metin_From_File=f.read() #reads all the text
f.close()

# %% r+ mode

f=open("Sample.txt", 'r+') #cursor is at the begining of the file
f.write("XXXXXXXXXXXXX")
f.close()

# %%
f=open("Sample.txt", 'r+') #cursor is at the begining of the file
First_read=f.readline() 
#cursor is at the begining of the second line now
Second_read=f.readline()
#cursor is at the begining of the third line now
f.seek(0) #cursor is at the begining of the file (1st byte)
Third_read=f.readline()
f.close()
#%% Save Easy
import numpy as np
L1=np.arange(1,1.1,0.002)
L1=L1[:,np.newaxis]

#saves by preserving the format
np.savetxt("Easysave01.txt", L1.T , fmt="%.3f", header = "Header01:") 
#defult space delimiter is " "
np.savetxt("Easysave02.txt", L1.T , delimiter=",", fmt="%.3f", header = "Header03") 
my_csv = np.loadtxt("./Easysave02.txt", delimiter=",")
