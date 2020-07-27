with open ("rosalind_ini2.txt", "r") as line:
    str = line.readline()

a, b = str.split(" ")
a = int (a)
b = int (b)

print a**2 + b**2
