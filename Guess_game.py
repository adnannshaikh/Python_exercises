import random
ran = random.randint(1,100)
while True:
    num = int(input("Guess the number: "))
    if num==ran:
        print("You're correct!!!")
        break
    elif num > ran:
        print("You've entered a larger number")
    else:
        print("You've entered a smaller number")
