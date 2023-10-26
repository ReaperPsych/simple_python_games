import random
import os
import time


colors = 'rgbys'
player = ''


for score in range(0,10):
    player += random.choice(colors)
    for color in player:
        print(color)
        time.sleep(1.5)
        os.system("clear")
    guess = input("Repeat: ")
    guess = guess.lower()
    os.system('clear')
    if guess != player:
        break

print(f"GAME OVER! your final score is {score}")
