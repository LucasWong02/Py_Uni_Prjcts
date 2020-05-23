#Formas Geometricas
n = int(input("N:"))
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        if i <= n - j:
            print("*", end = "")
        else:
            print("+", end = "")
    print()
n = int(input())
for i in range(1, n+1):
    for i in range(1, n+1):
        print(i)
