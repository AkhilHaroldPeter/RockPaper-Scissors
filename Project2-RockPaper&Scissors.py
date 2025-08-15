from enum import Enum
import random
from art import text2art
import sys
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Enum for the choices
class Choice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def ascii_art(self) -> str:
        arts = {
            Choice.ROCK: '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
            Choice.PAPER: '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
            Choice.SCISSORS: '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
        }
        return arts[self]

class GameOver(Exception):
    """Exception to signal game end."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        
        

class InputProvider:
    """Class to get user input; can be swapped/mocked for testing."""
    def get_input(self, prompt: str) -> str:
        return input(prompt).strip()

class RockPaperScissorsGame:
    def __init__(self, input_provider: InputProvider):
        self.input_provider = input_provider
        self.is_running = True

    def run(self):
        print(text2art("ROCK PAPER SCISSORS", font="cybermedium"))
        try:
            while self.is_running:
                self.play_round()
                self.ask_continue()
        except GameOver as e:
            logger.info(e.message)
            print(text2art("GAME OVER"))
        except KeyboardInterrupt:
            logger.info("Game interrupted by user.")
            print(text2art("GAME OVER"))            

    @staticmethod
    def flip_ascii_art(art: str) -> str:
        flip_map = str.maketrans({
            '(': ')',
            ')': '(',
            '/': '\\',
            '\\': '/',
            '{': '}',
            '}': '{',
            '[': ']',
            ']': '[',
            '<': '>',
            '>': '<',
        })
        lines = art.strip('\n').split('\n')
        flipped_lines = []

        max_width = max(len(line) for line in lines)

        for line in lines:
            # Pad line to the right to match width (so flipped lines align)
            padded = line.ljust(max_width)
            # Reverse and translate
            flipped = padded[::-1].translate(flip_map)
            flipped_lines.append(flipped)

        return '\n'.join(flipped_lines)                
            
    def play_round(self):
        user_choice = self.get_user_choice()
        comp_choice = self.get_computer_choice()

#         print("You chose:")
#         print(user_choice.ascii_art())
#         print("Computer chose:")
#         print(comp_choice.ascii_art())

#         result = self.determine_winner(user_choice, comp_choice)
#         print(result)

        comp_art_lines = comp_choice.ascii_art().strip('\n').split('\n')
        user_art_lines = self.flip_ascii_art(user_choice.ascii_art()).strip('\n').split('\n')

        print("\nComputer vs You:\n")
        for comp_line, user_line in zip(comp_art_lines, user_art_lines):
            print(f"{comp_line:<30}    {user_line}")

        result = self.determine_winner(user_choice, comp_choice)
        print("\n" + result + "\n")

    def get_user_choice(self) -> Choice:
        while True:
            response = self.input_provider.get_input(
                "Choose [0] Rock, [1] Paper, [2] Scissors: "
            )
            if not response.isdigit():
                print("Invalid input! Please enter 0, 1, or 2.")
                continue
            val = int(response)
            if val in [choice.value for choice in Choice]:
                return Choice(val)
            print("Invalid choice! Please enter 0, 1, or 2.")

    def get_computer_choice(self) -> Choice:
        return Choice(random.randint(0, 2))

    def determine_winner(self, user: Choice, comp: Choice) -> str:
        if user == comp:
            return "It's a tie!"
        # Define winning cases for user
        wins = {
            Choice.ROCK: Choice.SCISSORS,
            Choice.PAPER: Choice.ROCK,
            Choice.SCISSORS: Choice.PAPER
        }
        if wins[user] == comp:
            return "You win!"
        else:
            return "You lose!"

    def ask_continue(self):
        while True:
            cont = self.input_provider.get_input('Play again? (Y/N): ').strip().upper()
            if cont == 'N':
                self.is_running = False
                raise GameOver("Thanks for playing!")
            elif cont == 'Y':
                return
            else:
                print('Invalid input! Please enter "Y" or "N".')

if __name__ == "__main__":
    game = RockPaperScissorsGame(InputProvider())
    game.run()
