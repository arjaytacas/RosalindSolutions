# read problem here > https://rosalind.info/problems/cons/

from Bio import motifs
from Bio import SeqIO

# Read fasta file
sequences = [seq_record.seq for seq_record in SeqIO.parse("python village\input.txt", "fasta")]

# Create a motif object
m = motifs.create(sequences)

# Print Consensus
print(m.consensus)

# Print matrix
for base in "ACGT":
    print(f"{base}: {' '.join(f"{count:.0f}" for count in m.counts[base])}")
