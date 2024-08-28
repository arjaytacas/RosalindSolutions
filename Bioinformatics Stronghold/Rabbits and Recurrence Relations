# read problem here > https://rosalind.info/problems/fib/

# Given: Positive integers n≤40 and k≤5

# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, 
# every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# Sample Dataset
# 5 3
# Sample Output
# 19

# What we know is that the rabbits will be able to reproduce at 3rd month and there will be 3 new pairs of rabbit
# in first month, we have 1 pair of rabbits but needed another month to grow and mature before mating in the 3rd month
# so lets do it manually. let BR = baby rabbit pair, MR = mature rabbit
# 1st month = 1 RB, 2nd month = 1 MR, 3rd month = 1 MR + 3 BR, 4th month = 1 MR + 3 BR + 3MR, 5th month = 1 MR + 3 BR + 3MR + 3 MR + 9 BR
# which is [1,1,4,7,19]
# using fibonacci formula Fn = Fn-1 + Fn-2

n = 5 #number of months observed
k = 3 #rabbit pair produced

def rabbits (n, k):
    rabbitpairs = [0] * (n+1)
    rabbitpairs[1] = 1 # stands for number of rabbits in the first month

    for i in range (2, n+1): #since we set the value of rabbits in month 1 we can start range in month 2
        rabbitpairs[i] = rabbitpairs[i-1] + k*rabbitpairs[i-2] #first term on right hand side represents the old rabbit pairs while 
                                                               #the second one represents the new ones

    return rabbitpairs

print(rabbits(n,k)[n]) #we add [n] so it only prints the last value which is the expected output

