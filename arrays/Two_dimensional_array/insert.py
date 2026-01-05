import numpy as np

TwoDarray=np.array([[1,2,2,3],[1,2,2,3],[1,2,2,3],[1,2,2,3]])
# print(TwoDarray)

new_TwoDarray=np.insert(TwoDarray,0,[[1,2,2,3]],axis=1)

print(new_TwoDarray)