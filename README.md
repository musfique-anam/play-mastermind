# Mastermind (CLI Edition)
A Python Command-Line Version of the classic Mastermind game. Guess the secret number within limited attempts using feedback on correct digits.

## Features

- Choose difficulty: 3, 4, or 5 digits (default is 4 digits).

- Randomly generated number each game.

- Maximum 10 attempts to guess the number.

- Feedback after each guess:

  - Shows how many digits are correct.

  - Indicates which digits in your guess are correct.

- Timer to track how long it takes to guess the number.

- Game over message if attempts run out.

- Congratulatory message if you guess the number correctly.

## How to Play

Run the Python script:
```
game.py
```

>Enter the difficulty (3, 4, or 5 digits).

> Make your first guess.

After each guess, the game provides feedback:

> Correct digits are shown.

> Number of digits correctly placed is displayed.

Keep guessing until you either:

### Guess the number correctly (win).

### Run out of attempts (game over).

> Game ends and shows total attempts and time taken.

## Requirements

<Strong> Python 3.x </Strong>

## Example
```
Welcome to Mastermind (CLI Edition)
Choose difficulty(3/4/5 digits): 4
Guess the 4-digit number: 1234
Not quite the number. But you did get 1 digit(s) correct!
Also these numbers in your input were correct:
X 2 X X
Attempts left: 9
Enter your next choice of numbers: 
```
## Notes

- Only numeric inputs of the correct length are allowed.

- Default difficulty is 4 digits if an invalid input is entered.