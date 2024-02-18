nums = [1,2,3,4,5,5,7,8,9]
number = 20
for x in nums:
    if x == number:
        
        print("number is availble")
        
    else:
        print("number is NOT availble")
        



nums = [1, 2, -3, 4, -5, 6]

sum_positives = 0

for num in nums:
    if num < 0:
        continue
    sum_positives += num

print(f'Sum of Positive Numbers: {sum_positives}')