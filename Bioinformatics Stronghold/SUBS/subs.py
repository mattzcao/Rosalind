
with open ("rosalind_subs.txt", "r") as f:
    s = f.readline().replace("\n","")
    t = f.readline().replace("\n","")

indices = []

i = 0
while i < len(s) - len(t):
    if s[i:i+len(t)] == t:
        indices.append(str(i + 1))
    i += 1


print ' '.join(indices)
