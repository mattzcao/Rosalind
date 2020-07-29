
p = "" # Protein String

freq = {
    'G': 4, 'A': 4, 'V': 4, 'L': 6, 'I': 3,
    'P': 4, 'F': 2, 'Y': 2, 'W': 1, 'S': 6,
    'T': 4, 'C': 2, 'M': 1, 'N': 2, 'Q': 2,
    'K': 2, 'R': 6, 'H': 2, 'D': 2, 'E': 2,
    'B': 4, 'Z': 4, 'stop': 3,
}

with open("rosalind_mrna.txt", "r") as f:
    for line in f.readlines():
        p = p + line.replace("\n","")    

def combo(ps):
    c = 1 # Combinations
    for aa in ps:
        c *= freq[aa]
    return c

print combo(p) * freq['stop'] % 1000000
        
    
