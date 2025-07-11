# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is 
# the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output
# 20 12 17 21

Dataset = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
DNAcount = {'A':0,'C':0,'G':0,"T":0} #create a dictionary that have the nucleotides and the number 0 to start counting

# loop every nucleotide and add it to the dictionary
for n in Dataset:
    if n in DNAcount:
        DNAcount[n] += 1

# since we only want the values we only print values, end = " " is added so that the print wont go to a new line per value
for key, value in DNAcount.items():
    print(value, end=" ")
