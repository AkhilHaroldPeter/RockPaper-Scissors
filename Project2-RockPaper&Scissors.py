#Below ascii art from here : https://www.asciiart.eu/people/body-parts/hand-gestures
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
from art import *
import sys
game_over=False
print(text2art("ROCK PAPER SCISSOR", font="cybermedium"))
while not game_over:
    lst = [rock,paper,scissors]
    user_choice = input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
    if not user_choice.isdigit(): #to check if the user has provided any junk value and exit the code
        print(text2art("Game Over"))
        sys.exit('Invalid input, please select "0" for rock "1" for paper and "2" for "Scissors"')
    else:
        user_choice = int(user_choice)
    random_choice = random.randint(0,2)
    print('User Chose')
    if user_choice>2:
        print('Invalid input, please select "0" for rock "1" for paper and "2" for "Scissors"')
        print(text2art("Game Over"))
        game_over=True
    else:
        print(lst[user_choice])
        print("Computer Chose")
        print(lst[random_choice])
        if user_choice == random_choice:
          print("It's a tie")
        elif user_choice == 0 and random_choice == 1:#paper beat rock
          print("You lose")
        elif user_choice == 0 and random_choice == 2:#rock beats scissors
          print('You win')
        elif user_choice == 1 and random_choice == 0:#paper beats rock
          print('You win')
        elif user_choice == 1 and random_choice == 2:#scissors beats paper
          print('You lose')
        elif user_choice==2 and random_choice==1:#scissors beats paper
          print('You win')
        elif user_choice==2 and random_choice==0:#rock beats scissors
          print('You lose')
        elif user_choice>2:
          print("Invalid choice")
        game_continue_choice = input('Do you want to continue:"Y" for Yes and "N" for No :')
        if game_continue_choice.upper()=="N":
            game_over=True
            print(text2art("Game Over"))
        elif game_continue_choice.upper()=='Y':
            game_over=False
        else:
            print('Invalid Input! Please Type "Y" for Yes or "N" for NO')
            print(text2art("Game Over"))
            game_over=True
