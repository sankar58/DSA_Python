from array import *

#1.create an 1.array and traverse
print("step 1")
my_array=array('i',[1,2,3,4,5])
for i in range(len(my_array)):
    print(i)
print(my_array)
#2.access individual elements through indexes
print("step 2")
print(my_array[4])
#3.append any value to the 1.array using append() method
print("step 3")
my_array.append(6)
print(my_array)
#4.insert value in an 1.array using insert() method
print("step 4")
my_array.insert(6,7)
print(my_array)
#5. extend python 1.array using extend() method
print("step 5")
my_array1=array("i",[8,9,10])
my_array.extend(my_array1)
print(my_array)
#6. add items from list into 1.array using fromlist() method
print("step 6")
temp_list=[11,12,13]
my_array.fromlist(temp_list)
print(my_array)
#7.remove any 1.array element using remove() method
print("step 7")
my_array.remove(13)
print(my_array)
#8.remove last 1.array element using pop() method
print("step 8")
my_array.pop()
print(my_array)
#9. fetch any element through its index using index() method
print("step 9")
my_array.index(4)
print(my_array)
#10. reverse a python 1.array using reverse() method
print("step 10")
my_array.reverse()
print(my_array)
#11. get 1.array buffer information through buffer_inf() method
print("step 11")
print(my_array.buffer_info())
#12. check for number of occurrences od an element using count() method
print("step 12")
print(my_array.count(11))
#13 convert 1.array to string using toString() method
print("step 13")
# my_str=my_array.tostring()
# print(my_str)

#14. convert 1.array to a python list with same elements using tolist() method
print("step 14")
# my_array.tolist()
print(my_array)
#15 append a string to char 1.array using fromstring() method

#16 slice element from an 1.array
print("step 16")
print(my_array[:5])

