import random

number = random.randint(1,100)
tries = 0
found = False


print("Guess the number between 1 and 100")
while not found:
    guess = int(input("Guess: "))
    tries +=1
    if guess == number:
        found = True
        print(f"you have found the {number} in {tries} tries!")
    elif guess > number:
        print(f"The number you are looking for is less than {guess}")

    else:
        print(f"The number you are looking for is greater than {guess}")


