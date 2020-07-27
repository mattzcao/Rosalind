with open ("rosalind_ini4.txt", "r") as line:
    nums = line.readline()

a, b = nums.split(" ")
a = int (a)
b = int (b)
sum = 0;

for i in range (a, b+1):
    if i % 2 == 1:
        sum += i

print sum

