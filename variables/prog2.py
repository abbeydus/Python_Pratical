'''
List Data type
'''

#list of having both integers and strings
# c= ["hey","you",1,2,3,"go"]
# print(c) ##['hey', 'you', 1, 2, 3, 'go']

# Index:

##An index is a position or a number that represents the location of an element within a sequence.
##In many programming languages, indexing starts from 0. For example, the first element in a sequence is at index 0, the second at index 1, and so on.
##Negative indexing is also common, where -1 refers to the last element, -2 to the second-to-last, and so forth.


#index are 0 based. this will print a single character
c=          ["hey","you",1,2,3,"go"]
#index from [  0,    1, 2,3,4, 5]
print(c[1])  # you

## Inserting a string at 0 index 
c.insert(0, "cynefo")
print(c)  #['cynefo', 'hey', 'you', 1, 2, 3, 'go']

# len:

## "len" stands for length and 
## is a function that returns the number of elements in a sequence.
##  It can be applied to strings, lists, arrays, or any other iterable data structure.

b=["karen, s3://test/test.log", "28/jan/2024", "zxcvbn", 56,10, 30] #list
print(len(b)) #output 6

# indx = len(b) - 1  #6-1
# print(indx) #output 5

# b.insert(len(b), 20) ## Inserting a string at last index 
# print(b)


b[1] = "s3://karen/tst.log" 
print(b) #output ['karen, s3://test/test.log', 's3://karen/tst.log', 'zxcvbn', 56, 10, 30, 20]


b.remove(56)
print(b) #['karen, s3://test/test.log', 's3://karen/tst.log', 'zxcvbn', 10, 30]

b.pop() #removed last lenth value
print(b) #output ['karen, s3://test/test.log', 's3://karen/tst.log', 'zxcvbn', 10]
