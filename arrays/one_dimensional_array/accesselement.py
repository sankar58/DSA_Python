from array import *

arr1=array('i',[1,2,3,4,5,5])


def accessElement(array,index):
    if index >= len(array):
        print("there is no element in the given index")
    else:
        print(len(array))
        print(array[index])
accessElement(arr1,5)
