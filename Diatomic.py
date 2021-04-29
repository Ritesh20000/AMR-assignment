import random
import math
import matplotlib.pyplot as plt
import library
import numpy as np





def GenMat(x,y,z,n):
    Y = []
    i = 0
    while i < n:
        X = []
        j = 0
        while j<n:
            X.append(0)
            j = j + 1
        Y.append(X)
        i = i + 1
    for i in range(n):
        for j in range(n):
            if (i == j):
                Y[i][j] = x
                if i >= n-1:
                    break
                else:
                    Y[i+1][j] = y
                if j >= n-1:
                    break
                else:
                    Y[i][j+1] = y
    i = 0
    while i<n:
        Y[i][i] = z
        i = i + 2
        

    i = 0
    j = 0
            
        
            
    
    return Y
print(GenMat(10,0.5,5,7))


def plot(x,y,z,n):
    Y = GenMat(x,y,z,n)
    w,v = np.linalg.eig(Y)
    print("max eigenvalue is: ",max(w), "min eigenvalue is: ", min(w))
    wid=n
    wid = int(wid)
    plt.hist(w, bins= wid)
    plt.xlabel('Eigenvalue')
    plt.ylabel('Density')
    plt.title(plt.title('N= '+str(n)+', Beta = '+str(y)))
    plt.show()


plot(10,-2,5,1000)
plot(10,-2,5,500)
plot(10,-2,5,250)

plot(10,-2,5,1000)
plot(10,-1,5,1000)
plot(10,-0.5,5,1000)





