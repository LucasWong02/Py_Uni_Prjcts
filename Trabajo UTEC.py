def inicial():
    print("Este programa te permite hallar los diferentes elementos para el MRUA")
    print("Donde:")
    print("a = Aceleracion(m/s^2)")
    print("Vf = Velocidad final(m/s)")
    print("Vi = Velocidad inicial(m/s)")
    print("t = Tiempo(s)")
    print("x = Distancia")
    x = input("Dime que necesitas con las iniciales antes mostradas: ")
    if (x == "a"):
        print("Que datos tienes en el momento?")
        print("1 = Vi, Vf, t")
        print("2 = x, Vi, t")
        print("3 = Go back")
        aceleracion = int(input("Elige un numero: "))
#formula de aceleracion
        if (aceleracion == 1):
            Vf1 = float(input("Vf: "))
            Vi1 = float(input("Vi: "))
            t = float(input ("t: "))
            ace = float((Vf1 - Vi1)/t)
            print("Aceleracion: " + str(ace))
#formula de distacia
        elif (aceleracion == 2):
            x = float(input("x: "))
            Vi2 = float(input("Vi: "))
            t = float(input ("t: "))
            ace1 = float(2*(x - (Vi2 * t))/t**2)
            print("Aceleracion: " + str(ace1))
        elif (aceleracion == 3):
            inicial()
    elif (x == "t"):
        print("Que datos tienes en el momento?")
        print("1 = Vi, Vf, a")
        print("2 = x, Vi, a")
        print("3 = Go back")
        tiempo = int(input("Elige un numero: "))
#formula de tiempo
        if (tiempo == 1):
            Vi3 = float(input("Vi: "))
            Vf2 = float(input("Vf: "))
            a = float(input("a: "))
            tiem = float((Vf2 - Vi3)/a)
            print("Tiempo: " + tiem)
        elif (tiempo == 2):
            x1 = float(input("x: "))
            Vi4 = float(input("Vi: "))
            a1 = float(input("a: "))
            tiem1 = float((2*n1)/((2*Vi4) + (a*t)))
            print("Tiempo: " + str(tiem1))
        elif (tiempo == 3):
            inicial()
    elif (x == "x"):
        print("Que datos tienes en el momento?")
        print("1 = Vi, Vf, a")
        print("2 = x, Vi, a")
        print("3 = Go back")
        posicion = int(input("Elige un numero: "))   
#formula de posicion
        if (posicion == 1):
        elif (posicion == 2):
        elif (posicion == 3):
            inicial()
#formula de Vf
#formula de Vi
inicial()

 
