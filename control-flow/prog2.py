'''
Multiple variable assignment & Global local variables
'''
# a = b = c = 10

# print(a)
# print(b)
# print(c)

# a,b,c= 45, 1000, "Cynefo"
# print(f"{a} {b} {c}")



# local and global variable 

def f():
    name="abbey"   ## local variable
    print(f"hello from {name}")

def k():

    name="tee"   ## local variable
    print(f"hello from {name}")

f()
k()


# f()
# name="bee"
# k()
# print(name)