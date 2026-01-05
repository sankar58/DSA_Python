import numpy as np

TwoDarray=np.array([[1,2,2,3],[1,2,2,3],[1,2,2,3],[1,2,2,3]])
print(TwoDarray)

new_twoDarray=np.delete(TwoDarray,0,axis=1)
print(new_twoDarray)