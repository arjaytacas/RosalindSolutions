# Read problem here > https://rosalind.info/problems/fibd/

# similar with the former rabbits problem but with lifespan of rabbits added

def rabbit_pairs(n, m): # n is total number of months and m is the lifespan of rabbits
    rabbits = [0] * m
    rabbits[0] = 1  # 

    for month in range(1, n):
        new_pairs = sum(rabbits[1:])
        rabbits = [new_pairs] + rabbits[:-1] # total number of rabbits at the nth month

    return sum(rabbits)

n = 97
m = 16

print(rabbit_pairs(n, m))
