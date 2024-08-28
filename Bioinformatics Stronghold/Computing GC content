# Read problem here > https://rosalind.info/problems/gc/

# Problem needs to compute for the g-c content, which is computed by the total number of g and c symbols over total length of string
# and return the one with the highest %
# input will be inside a file and in a fasta forma, lets call the file fasta_file

from Bio import SeqIO

# Read fasta file
fasta_file = r'python village\fasta_file'
label = []
sequence = []
with open (fasta_file, 'r') as file:
    for record in SeqIO.parse(file, 'fasta'):
        label.append(record.id)
        sequence.append(str(record.seq))

# gc content computation
def gcalc(seq): 
    return round((seq.count('G')+seq.count('C'))/len(seq),6)

gc_contents = [gcalc(seq) for seq in sequence]

# getting the details of the sequence with max gc content
maxgc = max(gc_contents)
maxindex = gc_contents.index(maxgc)
maxlabel = label[maxindex]

print(maxlabel)
print(maxgc)
