# Tuple Data type

 #tuple is a data type that represents an ordered, immutable sequence of elements. 
 #Immutable means that once a tuple is created, you cannot change its elements or size. 
 #Tuples are similar to lists, but the key difference is that lists are mutable, whereas tuples are not.


a=[1,2,3,4]
print(a) #prints the whole tuple (1, 2, 3, 4)

# #tuple having multiple type of data.
b=("hello", 1,2,3,"go",4) #indexies 5, lenght is 6
print(b)
print(type(a))
print(type(b))
print(b[4])
print(len(b))
print(len(b)-1)
print(b[len(b)-1])


# print(b) #prints the whole tuple

# #index of tuples are also 0 based.

# print(b[4]) #this prints a single element in a tuple, in this case "go"