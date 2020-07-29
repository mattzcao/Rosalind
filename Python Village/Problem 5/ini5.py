arr = [];

with open ("rosalind_ini5.txt", "r") as f:
    for line in f.readlines():
        arr.append(line)

for i in len(arr):
    if i % 2 == 1:
        print arr[i]


