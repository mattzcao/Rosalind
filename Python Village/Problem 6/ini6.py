

with open ("rosalind_ini6.txt", "r") as f:
    s = f.readline()

d = {}

for word in s.split(" "):
    try:
        d[word] += 1
    except:
        d[word] = 1

for key, value in d.items():
    print key + " " + str(value)

