# Problem
# Given: Two positive integers a and b (a<b<10000).

# Return: The sum of all odd integers from a through b, inclusively.

# Sample Dataset
# 100 200
# Sample Output
# 7500

# declare variables
a, b = 100, 200
result = 0

# we need to make a list of all the odd integers first, +1 on b since we have the word "inclusively".
for num in range (a, b+1):
#   to confirm odd number we make sure that remainder is not equal to zero 
    if num % 2 != 0:
        result += num

print(result)
