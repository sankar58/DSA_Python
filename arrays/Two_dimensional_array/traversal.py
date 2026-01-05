import numpy as np

TwoDarray=np.array([[1,2,2,3],[1,2,2,3],[1,2,2,3],[1,2,2,3]])
print(TwoDarray)

def traversal(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traversal(TwoDarray)