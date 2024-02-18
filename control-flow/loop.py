'''
Prgram to display hello if the entered number is divisible by 5 else print bye
'''
'''
num = int(input("Enter the Integer Value ="))
if num%5==0:
    print("hello")
else:
    print("bye")
'''
'''
num =int(input ("enter the number ="))
if num%3==0:
    print('yes')
else:
    print('no')
'''

# name = ["sam", "olu", "Abbey", "sophie",]

# for x in name:
#      print(x)  #x will print in iteration
'''''
name = ["sam", "olu", "Abbey", "sophie",]

for x in name:
    if x=="abbey":
       print(x)
'''''
#Tuple
'''
Program to calculate the sum of the numbers
'''

# nums = (1, 2, 3, 4)

# sum_nums = 0  ## to store the sum, every time loop runs

# for num in nums:
#     sum_nums = sum_nums + num

# ##0+1-->1
# ##1+2-->3
# ##3+3-->6
# ##6+4-->10

# print(f'Sum of numbers is {sum_nums}') #Sum of numbers is 10

'''''
nums = (1, 2, 3, 4)

sum = 0

for x in nums: 
    sum = sum+x
print(f"sum of the numbers are {sum}")
'''''

# Create a tuple named 'numbers' containing integer values from 1 to 9
no = (1, 2, 3, 4, 5, 6, 7, 8, 9) #tuples

# Initialize counters for counting odd and even numbers
count_odd = 0
count_even = 0

for x in no:
    if x%2 == 0:
        count_even = count_even+1
# count = 0+1=1 [x is 2]
# count = 1+1=2 [x is 4]
# count = 2+1=3 [x is 6]
# count = 3+1=4 [x is 8]
    else:
        count_odd = count_odd+1
# count = 0+1=3 [x is 1]
# count = 1+1=2 [x is 2]
# count = 2+1=3 [x is 5]
# count = 3+1=4 [x is 7]
# count = 4+1=5 [x is 9]       
print(f"no for even count is {count_even}") #no for even count is 4
print(f"no for even count is {count_odd}") #no for even count is 5
print("no for even count:", count_odd)  #no for even count: 5
print("no for even count:", count_odd)  #no for even count: 5
print(count_even) #4
print(count_odd) #5


#range
y = range(1, 51, 3) ##(stating no, laster no, increamnetal)

for r in y:
    print(r)