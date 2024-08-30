# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s
# then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s
# of length at most 1000 bp.

# Return: The reverse complement s^c of s

# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT

dataset = 'AAAACCCGGT'

# using python to make a shorter code, you can check the long version below
def reversecomplement(seq):
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]

print(reversecomplement(dataset))

# Other way
# we can loop first to make our complements
# newdataset = ''

# for nuc in dataset:
#     if nuc == 'A':
#         newdataset += 'T'
#     elif nuc == 'T':
#         newdataset += 'A'
#     elif nuc == 'C':
#         newdataset += 'G'
#     elif nuc == 'G':
#         newdataset += 'C'

# print (newdataset[::-1])
