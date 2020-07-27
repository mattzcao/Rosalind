with open ("rosalind_ini3.txt", "r") as f:
    s = f.readline()
    nums = f.readline()

a, b, c, d = nums.split(" ")
a = int (a)
b = int (b)
c = int (c)
d = int (d)

print s[a:b+1] + " " + s[c,d+1]

