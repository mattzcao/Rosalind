md = {} # Monoisotopic mass dictionary
sa = [] # String array
p = "" # Protein sequence

with open ("protein-mass-table.txt", "r") as f:
    for line in f.readlines():
        sa = line.split(" ")
        md[sa[0]] = float(sa[1].replace("\n", ""))

with open ("rosalind_prtm.txt", "r") as f:
    p = f.readline().replace("\n", "")

def calc_mass(seq):
    m = 0 # Protein sequence mass

    for aa in seq:
        m += md[aa]
        
    return m

print calc_mass(p)

