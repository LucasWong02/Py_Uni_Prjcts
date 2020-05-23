### --- funciones ------
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
    
def comb(N, k):
    return fact(N)/(fact(k) * fact(N - k))

### ---- Main --------
N = int(input("N:"))
k = int(input("k:"))
print("Grupos:", int(comb(N, k)))
