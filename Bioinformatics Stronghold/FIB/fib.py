s = ""
n = 0 # Given months to grow
k = 0 # Pairs of litter offspring per pair every generation

with open ("rosalind_fib.txt", "r") as f:
    s = f.readline().split(" ")

n, k = int(s[0]), int(s[1])
print "Input:"
print n, k
print "Output:"

"""
# Unfortunately this is the wrong code 
def rabbit_pop(m, r):
    if m < 1:
        return 1
    else:
        return k**m + rabbit_pop(m-1, k)

print rabbit_pop(n, k)
"""

"""
def rabbit_pop():
    b, c, a = 0, 1, 0 # Baby pairs, Child pairs, Adult pairs
    p = 0 # total popualation

    for i in range(n - 1):
        b = a * k # All adults produce k pairs of offspring per month
        a = a + c # Children pairs have now matured and become adults
        c = b # The new generation of children are the babies
        p = a + c # Total population is the current adult and children population

    return p

print rabbit_pop()
"""

def rabbit_pop(m, a, c):
    if m - 1 < 1:
        return a + c
    else:
        a = a + c
        c = (a - c) * k
        return rabbit_pop(m - 1, a, c)

print rabbit_pop(n, 0, 1)













