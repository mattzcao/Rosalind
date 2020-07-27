key = [] # Iterable Dictionary Keys
valSeq = [] # Iterable Dictionary Values
valGC = [] # Iterable Dictionary Value

with open ("rosalind_gc.txt", "r") as f:
    for line in f.readlines():
        if line.startswith(">"):
            key.append(line.replace(">", "").replace("\n", ""))
            valSeq.append(f.readline().replace("\n", "")) # Right after we identify the ID, we append a new line to our sequence array
        else:
            valSeq[len(valSeq) - 1] = valSeq[len(valSeq) - 1] + line.replace("\n", "") # Since we appended earlier, now we just concatenate until we hit next ID
        

def gc_content(seq):
    cg = seq.replace("A", "").replace("T", "")
    return float(len(cg)) / float(len(seq)) * 100

for seq in valSeq:
    valGC.append(gc_content(seq))

def greatestIndex():
    gi = 0
    gv = 0

    i = 0
    while i < len(key):
        if valGC[i] > gv:
            gv = valGC[i]
            gi = i
        i += 1

    return gi 

print key[greatestIndex()]
print valGC[greatestIndex()]
