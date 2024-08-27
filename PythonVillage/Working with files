# Problem
# Given: A file containing at most 1000 lines.

# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# Sample Dataset
# Bravely bold Sir Robin rode forth from Camelot
# Yes, brave Sir Robin turned about
# He was not afraid to die, O brave Sir Robin
# And gallantly he chickened out
# He was not at all afraid to be killed in nasty ways
# Bravely talking to his feet
# Brave, brave, brave, brave Sir Robin
# He beat a very brave retreat
# Sample Output
# Yes, brave Sir Robin turned about
# And gallantly he chickened out
# Bravely talking to his feet
# He beat a very brave retreat

# since dataset is a bit long, we will put this into a file named Workingwithfiles.txt
# make sure to save the file so our code will recognize the txt

# we will read the file first r is added before file name so that python accepts \ as a normal text
# python village\Workingwithfiles.txt = should be the directory and file name where you save the file
with open (r'python village\Workingwithfiles.txt', 'r') as f:
    # add start=1 in enumerate to assume 1-based numbering of lines as said in the problem
    newsetofwords = [line for pos, line in enumerate(f.readlines(),start=1) if pos % 2 == 0]

# we will make a file for the output
with open (r'python village\workingwithfilesout', 'w') as f:
    f.write(''.join([line for line in newsetofwords]))


