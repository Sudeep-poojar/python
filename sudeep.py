import random
min_val = 1
max_val = 6
rollagain = "yes"
while rollagain == "yes" or rollagain == "y":
    print("Dices rolling...")
    break

print("The values are:")
print(random.randint(min_val, max_val))
print(random.randint(min_val, max_val))

roll_again = input("Roll the Dices Again?")
