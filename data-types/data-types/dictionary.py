# Dictionary is a built-in data type that represents an unordered collection of key-value pairs. 
# It is also known as a "hash map" or an "associative array" in other programming languages. 
# Dictionaries are useful for storing and retrieving data in a structured way.

# Syntax:
# Dictionaries are defined using curly braces {}. 
# Each key-value pair is separated by a colon :.
'''
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

'''''
# Sample example for implementing Dictionary data type

''''''

a = {1:"first name",2:"last name", "age":33}

a ={
    1:"first name",
    2:"last name",
    "age":33
}

#print value having key=1
print(a[1])
#print value having key=2
print(a[2])
#print value having key="age"
print(a["age"])


b = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors":["red", "white", "blue"]
  }

#print value having key=brand
print(b["brand"]) #Ford
#print value having key=electric
print(b["electric"]) # {False}
#print value having key="colors"
print(b["colors"]) # {['red', 'white', 'blue']}