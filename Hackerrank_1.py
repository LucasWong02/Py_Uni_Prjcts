n = int(input("Pon un numero: "))
if n == (2,4):
    print("Not weird")
elif (n % 2) == 0 and (5 < n < 21):
    print("Weird")
elif (n % 2) == 0 and (n > 19):
    print("Not Weird")
else:
    print("Weird")
