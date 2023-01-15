import random
number=random.randint(1,10)
for i in range(0,3):
    user=int(input("guess the number:"))
    if user = number:
        print("hurray")
        print("you guessed the number is right",number)
        break
    elif user>number:
        print("your guess is too high")
    elif user<number:
        print("your guess is too low")
else:
    print("nice try but the number is :",number)