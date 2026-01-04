from array import *

arr1=array('i',[1,2,3,4,5,6])

def search(array, value):
    for i in array:
        if i==value:
            return array.index(value)
    return "the value that you are searching for doesnt exist"

print(search(arr1,6))
