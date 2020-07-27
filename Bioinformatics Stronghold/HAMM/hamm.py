

with open ("rosalind_hamm.txt", "r") as f:
    s = f.readline()
    sA = [n for n in s]
    t = f.readline()
    tA = [n for n in t]

hd = 0

i = 0
while i < len(sA):
    if sA[i] != tA[i]:
        hd+=1
    i+=1

print hd
        

