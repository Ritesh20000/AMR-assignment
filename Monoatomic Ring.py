import random
import math
import matplotlib.pyplot as plt
import library
import numpy as np





def GenMat(x,y,n):
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
                if i == n-1:
                    break

                else:
                    Y[i+1][j] = y
                if j == n-1:
                    break
                else:
                    Y[i][j+1] = y
    Y[0][n-1] = y
    Y[n-1][0] = y
    return Y


def plot(x,y,n):
    Y = GenMat(x,y,n)
    w,v = np.linalg.eig(Y)
    print("max eigenvalue is: ",max(w), "min eigenvalue is: ", min(w))
    wid=math.sqrt(n)
    wid = int(wid)
    plt.hist(w, bins= wid)
    plt.title(plt.title('N= '+str(n)+', Beta = '+str(y)))
    plt.xlabel('Eigenvalue')
    plt.ylabel('Density')
    plt.show()

plot(10,0.1,1000)
plot(10,0.1,500)
plot(10,0.1,250)

plot(10,0.1,1000)
plot(10,0.2,1000)
plot(10,0.3,1000)


def DEN(x,y,n1,n2):
    X = []
    Y = []
    i = n1
    while i<n2:
        M = GenMat(x,y,i)
        w,v = np.linalg.eig(M)
        band = max(w) - min(w)
        X.append(i)
        Y.append(band)
        i = i+1
    plt.plot(X,Y)
    plt.xlabel('N')
    plt.ylabel('Band width')
    plt.show()

DEN(10,0.1,10,100)






