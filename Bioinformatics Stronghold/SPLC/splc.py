dna = []
s = ""
introns = []
cd = {} # Codon dictionary

with open ("rosalind_splc.txt", "r") as f:
    for line in f.readlines():
        if line.startswith(">"):
            dna.append(f.readline().replace("\n", ""))
        else:
            dna[len(dna) - 1] = dna[len(dna) - 1] + line.replace("\n", "")

s = dna[0]

for i in range(1, len(dna)):
    introns.append(dna[i])

for intron in introns:
    i = s.index(intron)
    s = s[0:i] + s[i+len(intron):len(s)]

with open ("dna-codon-table.txt", "r") as f:
    for line in f.readlines():
        cd[line.replace("\n", "").split()[0]] = line.replace("\n", "").split()[1]

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
