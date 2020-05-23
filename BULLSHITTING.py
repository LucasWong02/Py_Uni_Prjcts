def prjct(a):
    if a in ("Si", "si"):
        b = input("Que le gusta?: ")
        print("Primero que todo tienes que saber como dar una primera impresión")
        print("Bañate, ponte elegante")
        c = input("Diste una buena impresión?(Si/No): ")
        if c in ("Si", "si"):
            print("Que bueno!!!")
            d = input("Sientes que tienes confianza con ella?(Si/No): ")
            if d in ("Si", "si"):
                print("Ya casi estamos!!!")
                print("Ahora da el siguiente paso: Una salida")
                print("Haz con ella lo que mas le gusta: " + b)
                print("Si todo sale bien... ya estamos!!!")
                print("Ahora todo esta en tus manos")
            elif d in ("No", "no"):
                print("No te rindas!!!")
                print("Trata una vez mas!!!")
        elif c in ("No", "no"):
            print("Sigue tratando hasta que tengas confianza con el/ella")
    
    elif a in ("No", "no"):
        print("Consiguete a alguien pues!!!")
    else:
        return prjct(a)
a = input(("Te gusta alguien?(Si/No): "))
prjct(a)
print("Fin del programa")
