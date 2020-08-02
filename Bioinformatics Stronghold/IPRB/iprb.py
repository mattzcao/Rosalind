with open ("rosalind_iprb.txt", "r") as f:
    (AA, Aa, aa) = f.readline().split()
    (AA, Aa, aa) = (int(AA), int(Aa), int(aa))

def f(num):
    retval = 1
    for i in range(1, num + 1):
        retval *= i
    return retval

def c(n, k):
    return 0 if k > n else f(n)/(f(n - k) * f(k))


d = (c(AA,2)*4 + c(Aa,2)*3 + c(aa,2)*0 +
     c(AA,1)*c(Aa,1)*4 + c(AA,1)*c(aa,1)*4 +
     c(Aa,1)*c(aa,1)*2)

p = AA + Aa + aa

t = (p * (p - 1) / 2) * 4

print float(d) / float(t)

