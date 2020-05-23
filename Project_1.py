print ("What's your name?")
name = input ("NAME: ")
print ("Hi " + name + "!!!")
print ("Guess the number between 1 to 10")
print ("The number has to be a positive, even and full number...")
a = int(input("Guess the number: "))
if 2 <= a < 10:
    input ("Your number is wrong try again")
    b = 1
    int(input("Guess the number: "))
    if b == 1:
        input (name + " your guess is right!!!")
    else:
        input (name + " you are wrong :(")
elif a == 1:
    input (name + " your guess is right!!!")
elif a > 10:
    input ("Guess the number between 1 to 10")
    c = 1
    int(input("Guess the number: "))
    if c == 1:
        input (name + " your guess is right!!!")
    else:
        input (name + " you are wrong :(")
else:
    int(input("Guess the number: "))
    
              
              
