with open ("rosalind_dna.txt", "r") as f:
    s = f.readline()

a, c, t, g = 0, 0, 0, 0

for nuc in s:
    if nuc == 'A':
        a += 1
    elif nuc == 'C':
        c += 1
    elif nuc == 'T':
        t += 1
    else:
        g += 1

print a, c, g, t

