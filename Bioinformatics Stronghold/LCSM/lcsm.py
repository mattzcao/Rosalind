
dna = []
motifs = []

with open ("rosalind_lcsm.txt", "r") as f:
    for line in f.readlines():
        if line.startswith(">"):
            dna.append(f.readline().replace("\n", ""))
        else:
            dna[len(dna)-1] = dna[len(dna)-1] + line.replace("\n", "")

def getShortSeqIndex():
    lowLength = 1001
    lowIndex = 0
    for i in range(len(dna)):
        if len(dna[i]) < lowLength:
            lowLength = len(dna[i])
            lowIndex = i
    return lowIndex

lowestIndex = getShortSeqIndex()

def getMotifs():
    sseq = dna[lowestIndex]
    passed = True
    i = 0
    while i < len(sseq) - 1:
        j = i + 2
        while j < len(sseq) + 1:
            for seq in dna:
                if sseq[i:j] not in seq:
                    passed = False
                    break
            if passed is True:
                motifs.append(sseq[i:j])
            passed = True
            j += 1
        i += 1
getMotifs()

def getLongMotif():
    longMotif = ""
    for motif in motifs:
        if len(motif) > len(longMotif):
            longMotif = motif
    return longMotif

with open("output_lcsm.txt", "w+") as o:
    o.write("Longest Motif: " + str(getLongMotif()))





