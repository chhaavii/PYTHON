

# Word Guessing Game

## Description
This is a Python-based Word Guessing Game where players guess a randomly selected word based on different difficulty levels: Easy, Medium, and Hard. The game provides a hint and a limited number of attempts for players to guess the correct word. If a guessed letter is in the correct position, it is replaced by an asterisk (`*`).

## Features
- **Three Levels of Difficulty**:
  - **Easy**: 5-letter words with 4 attempts.
  - **Medium**: 7-letter words with 6 attempts.
  - **Hard**: 8-letter words with 5 attempts.
- **Hints**: Provides the first and last letters of the word based on the difficulty level.
- **Attempts Logging**: Stores the player’s name, selected level, and remaining attempts in a CSV file (`project.csv`).
- **Score Viewing**: Players can view their attempts history saved in `project.csv`.

## Requirements
- Python 3.x
- Required libraries:
  - `pandas`
  - `csv`

## Installation
1. Clone or download the repository.
2. Install the required libraries with:
   ```bash
   pip install pandas
   ```

## Usage
1. Run the script:
   ```bash
   python word_guessing_game.py
   ```
2. Choose a difficulty level:
   - Type `1`, `Easy`, `easy`, or `EASY` for Easy.
   - Type `2`, `Medium`, `medium`, or `MEDIUM` for Medium.
   - Type `3`, `Hard`, `hard`, or `HARD` for Hard.
   - Type `4`, `Attempts`, or `attempts` to view previous scores.
3. Guess the word based on the hint provided. Enter one letter at a time. If you guess the word correctly, you win!
4. After each round, you have the option to continue or exit by typing `y` or `n`.

## How it Works
- The game randomly selects a word from a pre-defined list based on the selected level.
- Players are prompted to guess the word and given hints to assist them.
- Each correct letter is marked with an asterisk (`*`).
- If the player fails to guess the word within the given attempts, the game reveals the correct word.
- All scores and attempts are saved in `project.csv` for review.

## Example
Upon starting, the player will see:
```
WELCOME TO YOU!
RULE
There's one randomly selected word of FIVE, SEVEN, OR EIGHT letters.
You will get FEW attempts to guess the word according to the level.
If any letter is in the correct position, the letter would be replaced by '*'.
Have FUN!
LEVEL
1. EASY
2. MEDIUM
3. HARD
4. ATTEMPTS
Choose level: 1
Hint of the word: S _ _ _ _
Enter word: Study
Great! You won the game
```

## License
This project is open source and available under the MIT License.

--- 

