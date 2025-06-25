# read problem here > https://rosalind.info/problems/prot/

# we need to translate RNA into its protein counterpart
# 3 letter of RNA is translated to 1 letter protein. 
# we need a table called RNA codon table

# I copied this dictionary from the internet. Just modified it so that stop codons give nothing to match our expected output.
RNA_Codons = {
    # 'M' - START, '' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "", "UAG": "", "UGA": ""
}

Dataset = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

# we need to loop this but we need to start at every 4th letter every time since the 3 prior letters would be used for a different letter
Protein = ''
for nuc in range(0,len(Dataset),3):
    codon = Dataset[nuc:nuc+3]
    Protein += RNA_Codons[codon]

print(Protein)
