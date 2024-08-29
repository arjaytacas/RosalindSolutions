# read problem > https://rosalind.info/problems/subs/

# They want us to locate the motif within the DNA 

import re


Dataset = 'GATATATGCATATACTT'
lookfor = '(?=ATAT)' # ?= was added because the code with only ATAT skips the part that overlaps with each other

matches = re.finditer(lookfor, Dataset)

if matches:
    locations = [match.start() +1 for match in matches]
    print(*locations)
