# Problem
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing 
# all occurrences of 'T' in t with 'U' in u

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.

# Sample Dataset
# GATGGAACTTGACTACGTAAATT
# Sample Output
# GAUGGAACUUGACUACGUAAAUU

dataset = 'GATGGAACTTGACTACGTAAATT'

def transcription(DNAseq):
    # transforming 'T' to 'U' in DNA seq
    return DNAseq.replace('T','U')

print(transcription(dataset))

# Other way
# loop version we make a new data called new strand
# newdataset = ''

# for nuc in dataset:
#     if nuc == 'T':
#         newdataset += 'U'
#     else:
#         newdataset += nuc

# print(newdataset)
