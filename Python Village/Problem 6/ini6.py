d = {}
a = []

with open ("rosalind_ini6.txt", "r") as f:
    s = f.readline().replace("\n", "")
    a = s.split(" ")

for word in a:
    try:    
        d[word] += 1
    except:
         d[word] = 1
    

for key, value in d.items():
    print key + " " + str(value)

