import random

user = 0
comp = 0
round = 0

print("Three points first wins the game")

conditions = {
        'paper':'rock',
        'rock':'scissor',
        'scissor':'paper'
        }
choices = {
        'p':'paper',
        'r':'rock',
        's':'scissor'
        }

while user <3 and comp<3 :
    usr_choice = input("Enter 'p' for paper, 'r' for rock and 's' for scissor: ")
    round += 1
    if usr_choice in choices:
        usr_choice = choices[usr_choice]
        print(usr_choice)
    else:
        print("Invalid input. Plesae choose 'p', 'r', 's'")
        continue

    comp_choice = random.choice(list(conditions.keys()))
    print(comp_choice)

    if usr_choice in conditions.keys() and comp_choice in conditions[usr_choice]:
        print(f'\nuser won round {round}\n')
        user +=1

    elif usr_choice == comp_choice:
        print (f"\nRound {round} Draw \n")

    else:
        print(f'\ncomp won round {round}\n')
        comp += 1
        
print (f"final score: User {user} -- Comp {comp}")
if user > comp:
    print("User wins the game!")

else:
    print("Computer wins the game!")



