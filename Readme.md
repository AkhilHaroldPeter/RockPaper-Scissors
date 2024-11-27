# Rock, Paper, Scissors Game

### To play RockPaperScissors, please click here : https://replit.com/@akhilpeter/Project2-RockPaperandScissors?v=1


## Description

Rock, Paper, Scissors is a classic hand game usually played between two people. The game has three possible outcomes: a tie, or a win for either player. Each player simultaneously forms one of three shapes with an outstretched hand. The possible shapes are:

- Rock: represented by a closed fist.
- Paper: represented by an open hand.
- Scissors: represented by a fist with the index and middle fingers extended, forming a V.

The winner is determined based on the chosen shapes according to the following rules:

- Rock crushes Scissors (Rock wins against Scissors).
- Scissors cuts Paper (Scissors win against Paper).
- Paper covers Rock (Paper wins against Rock).
- If both players choose the same shape, the game is a tie.

## Rules for the Python Project

1. **Player Input**: The player will choose one of the three options: Rock, Paper, or Scissors. This can be done  by typing the choice.

2. **Computer Input**: The computer will randomly select one of the three options: Rock, Paper, or Scissors.

3. **Comparison**: The choices made by the player and the computer will be compared to determine the winner based on the rules mentioned above.

4. **Display Result**: The result of the game (win, lose, or tie) will be displayed to the player.

5. **Repeat or Quit**: After displaying the result, the player should have the option to play again or quit the game.

By implementing these rules, players can enjoy the classic Rock, Paper, Scissors game in a Python project, providing an interactive and entertaining experience.




## Dependencies

This project relies on the following Python packages:

- `text2art`:It is a tool utilized for transforming text into ASCII art. If the package is not already installed, you can install it by executing the following command: `pip install text2art`
- `random`: random module is in the python standard library. Used to give random choice from a given list of options.

## Installation

To install the required packages, use the following `pip` commands:

```pip install text2art```

---

## Python Installation

To run this project, you need to have Python installed on your system. If you haven't installed Python yet, follow these steps:

### Windows

1. Download Python installer from the [official website](https://www.python.org/downloads/).
2. Run the installer, ensuring that the option to add Python to your PATH is selected.
3. Follow the installation steps, and Python will be installed on your system.

### macOS

1. macOS usually comes with Python pre-installed. To check if Python is installed, open the Terminal and type `python3 --version`. If Python is installed, it will display the version number.
2. If Python is not installed, you can install it using [Homebrew](https://brew.sh/). Open Terminal and run the following command:
`brew install python@3.9`

### Linux

1. Python is often installed by default on Linux systems. To check if Python is installed, open a terminal and type `python3 --version`. If Python is installed, it will display the version number.
2. If Python is not installed, you can install it using your distribution's package manager. For example, on Ubuntu, you can use `apt`:
`sudo apt update`
`sudo apt install python3`


## After you have installed python you can run the code by following the below steps:
- Clone the repository to your local machine: https://github.com/AkhilHaroldPeter/Python.git (If this is your first time doing this, please follow through the following documentation: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- Navigate to the directory containing the RockPapaer&Scissors game files.
- Install the required packages using pip.
- Run the `Project2-RockPaper&Scissors.py` script.
- Follow the prompts to play the game and choose your move (Rock, Paper, or Scissors).
#### Alternatively, you can download the repository as a zip file, unzip it, and then use it on your local machine.


## Key Concepts

- User Input Handling: Implemented mechanisms to handle user input for selecting moves (Rock, Paper, or Scissors), ensuring smooth interaction with the game.
- Random Selection: Utilized the `random` module to generate random selections for the computer opponent, adding unpredictability to the game.
- Conditional Statements: Employed conditional statements to determine the outcome of each round based on the player's and computer's selections, facilitating game logic.
- Looping Constructs: Utilized looping constructs to allow for multiple rounds of gameplay, enhancing the overall gaming experience.
- Score Tracking: Implemented score tracking mechanisms to keep track of the player's and computer's wins, losses, and ties throughout the game.
