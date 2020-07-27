cd = {} # Codon Dictionary
sa = [] # String Array
s = "" # mRNA sequence

# Import Codon Table
with open ("codon_table.txt", "r") as ct:
    for line in ct.readlines():
        sa = line.split(" ")
        cd[sa[0]] = sa[1].replace("\n", "") # When importing, many amino codes had "\n" at the end of them, potentially ruining the answer

# Import mRNA Sequence
with open ("rosalind_prot_1.txt", "r") as f:
    s = f.readline()

# Convert mRNA Sequence to Protein Sequence
def convert(seq):
    ac = "" # Amino Code
    ps = "" # Protein sequence
    
    i = 0
    while i < len(seq):
        try: # Try/Catch in case the mRNA sequence isn't a multiple of 3
            ac = cd[seq[i:i+3]] # Substring used as key for codon table dictionary
        except:
            return ps # If there are less than 3 nucleotides left to read, just return the protein sequence
        if (ac == "Stop"): 
            return ps 
        else:
            ps = ps + ac 
        i += 3
    return ps;

print convert(s)
