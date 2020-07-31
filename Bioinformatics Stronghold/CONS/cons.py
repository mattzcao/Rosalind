
dna = []
a = []
c = []
g = []
t = []

with open ("rosalind_cons.txt", "r") as f:
    for line in f.readlines():
        if line.startswith(">"):
            dna.append(f.readline().replace("\n", ""))
        else:
            dna[len(dna) - 1] = dna[len(dna) - 1] + line.replace("\n", "")

def init_list():
    for i in range(len(dna[0])):
        a.append(0)
        c.append(0)
        g.append(0)
        t.append(0)
        

def count_nuc():
    for seq in dna:
        for i in range(len(seq)):
            if seq[i] == 'A':
                a[i] += 1
            elif seq[i] == 'C':
                c[i] += 1
            elif seq[i] == 'T':
                t[i] += 1
            else:
                g[i] += 1

def find_cons():
    cons = ""
    for i in range(len(a)):
        if a[i] > c[i]:
            if a[i] > t[i]:
                if a[i] > g[i]:
                    cons = cons + "A"
                else:
                    cons = cons + "G"
            else: # a[i] <= t[i]
                if t[i] > g[i]:
                    cons = cons + "T"
                else: # t[i] <= g[i]
                    cons = cons + "G"
        else: # a[i] <= c[i]
            if c[i] > t[i]: 
                if c[i] > g[i]:
                    cons = cons + "C"
                else:
                    cons = cons + "G"
            else: # c[i] <= t[i]
                if t[i] > g[i]:
                    cons = cons + "T"
                else:
                    cons = cons + "G"
                    
    print cons        
    

init_list()
count_nuc()
find_cons()

for i in range(len(a)):
    a[i] = str(a[i])
    c[i] = str(c[i])
    t[i] = str(t[i])
    g[i] = str(g[i])

print "A:", " ".join(a)
print "C:", " ".join(c)
print "G:", " ".join(g)
print "T:", " ".join(t)


"""
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
T: 1 5 0 0 0 1 1 6
G: 1 1 6 3 0 1 0 0
"""
