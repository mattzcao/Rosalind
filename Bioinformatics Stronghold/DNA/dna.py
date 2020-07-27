with open ("rosalind_dna.txt", "r") as f:
    s = f.readline()

nCount = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for letter in list(s):
    if letter == 'A':
        nCount['A'] += 1
    elif letter == 'C':
        nCount['C'] += 1
    elif letter == 'G':
        nCount['G'] += 1
    elif letter == 'T':
        nCount['T'] += 1
        
print str(nCount['A']) + " " + str(nCount['C']) + " " + str(nCount['G']) + " " + str(nCount['T'])

