from itertools import product

A = ['1', '8', '0', '2', '6', '7', '9']
prodA = list(product(A, repeat=2))
res = [''.join(x) for x in prodA]
print(res)