#Set Data Type
#set is a built-in data type that represents an unordered collection of unique elements. 
#Sets are similar to lists and tuples, but they have some distinct characteristics:

# Uniqueness: 
# A set cannot contain duplicate elements. 
# If you try to add an element that is already present, it won't result in duplicate entries.

# Unordered:
# The elements in a set are not stored in any specific order. 
# Unlike lists and tuples, sets do not have an index.

# Mutability:
# Sets are mutable, meaning you can add and remove elements after the set is created.

# Syntax:
# Sets are defined using curly braces {} or by using the set() constructor.

# Operations:
# Sets support various operations, including union, intersection, difference, and more.

my_set = {1, 2, 3, 4, 5}
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2) 
print(union_set)         # {1, 2, 3, 4, 5}

intersection_set = set1.intersection(set2) 
print(intersection_set) # {3}

difference_set = set1.difference(set2)  
print(difference_set)  # {1, 2}

# Methods:
# Sets have methods for adding and removing elements, as well as for performing set operations.

my_set.add(6)      # Adds the element 6 to the set
my_set.remove(1)   # Removes the element 3 from the set

print(my_set) # {2, 3, 4, 5, 6}

...

c={11,12,"abbey", 20}
print(c)

c.add(15)
print(c) #  Unordered:{11, 12, 15, 'abbey', 20}  {'abbey', 11, 12, 15, 20}
c.pop()
print(c)
c.clear()
print(c)