arr = [];

with open ("rosalind_ini5.txt", "r") as f:
    for line in f.readlines():
        arr.append(line)
#    while str != None:
#        arr.append(str);
#        str = line.readline()

for i in range(len(arr)):
    if i % 2 == 0:
        print arr[i]


