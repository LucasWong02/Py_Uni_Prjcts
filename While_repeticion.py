#while True:
#    n = int(input())
#    if n<=10 and n>=2:
#        break;

n = 0
while n > 10 or n < 1:
    n = int(input("Ingrese el total de notas: "))

sumador = 0
max_nota = 0
min_nota = 21
for i in range(n):
    nota = 0
    while nota > 20 or nota < 1:
        nota = float(input("Ingrese la nota " +str(i+1) +": "))
    sumador += nota
    if nota > max_nota:
        max_nota = nota
    if nota < min_nota:
        min_nota = nota

print("El promedio es:", sumador/n)
print("La maxima nota es:", max_nota)
print("La minima nota es:", min_nota)
