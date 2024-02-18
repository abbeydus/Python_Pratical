'''
Break Statement

we have a list of numbers and we want to check if a number is present or not
'''

# nums = [1, 2, 3, 4, 5, 5, 6]

# n = 4

# for x in nums:
#     if x == n:
#         print("is available")
#         break
        

'''''
nums = [1, 2, 3, 4, 5, 5, 6]

n = input("enter the int you want to check =")

for x in nums:
    if x == n:
        print("is available")
        break
'''''
'''
Continue Statement

use continue statements inside a for loop to skip the execution of the for loop body for a specific condition.
'''
#sum of only positive 
# nums = [1, 2, -3, 4, -5, 6]

# sum = 0

# for x in nums:
#     if x<0:
#         continue
#     sum = sum +x
# print(sum)

'''
while
'''
# num = 0

# while num < 5: ## while num is less than 5
#     num = num +1
#     print(f'number = {num}')
'''
num = 0

while num < 5: ## while num is less than 5
    num = num +1
    if num == 3:
        break
    print(f'number = {num}')
'''
num = [1,2, 3, 4, 5,6]

while True: ## condition is true
    length = len(num)
    if length > 0:
        print('data is available in the data set')
        break
    