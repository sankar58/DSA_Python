import numpy as np

TwoDarray=np.array([[1,2,2,3],[1,2,2,3],[1,2,2,3],[1,2,2,3]])
print(TwoDarray)

def AccessElement(array,rowindex,colindex):
    if rowindex >=len(array) or colindex >= len(array):
        print("there is no colunm or row in the given 1.array")
    else:
        print(array[rowindex][colindex])

AccessElement(TwoDarray,5,0)