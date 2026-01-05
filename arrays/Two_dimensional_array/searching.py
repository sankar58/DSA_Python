import numpy as np

TwoDarray=np.array([[1,2,2,3],[1,2,2,3],[1,2,2,3],[1,2,2,3]])
print(TwoDarray)

def searching(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]== value:
                return f"the value that you ara looking for is at {i} {j}"
        return "the element is not found in 1.array"

print(searching(TwoDarray,2))