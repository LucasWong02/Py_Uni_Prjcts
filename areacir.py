def CalcularAreaCirculo(rad):
    pi = 3.141592
    return pi * rad ** 2


#---- Main ------
radio = int(input("Radio:"))
area = CalcularAreaCirculo(radio)
print("El area es:", area)
