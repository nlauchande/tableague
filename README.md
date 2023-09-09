# Express Parse CLI

This CLI tool is designed to parse a given input file, which contains fixture results of soccer matches. It calculates and displays the rankings of teams based on their scores.

## Dependencies

- `typer`: For creating command-line applications.
- `re`: Python's regular expression module.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required libraries:

## Usage
To execute the command line application:


python <script_name>.py addscores [OPTIONS]
Replace <script_name> with the name you have saved the script as.

Options
filename: Name of the input file (default is "input.txt"). The file should contain lines in the followng format:

``
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
``

The output is in the following format
``
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
``



## Functionality

Reads the input from the given file.
Parses each line to extract team names and scores.
Calculates the scores for each team:
3 points for a win
1 point each for a draw
0 points for a loss
Displays the team rankings based on their scores.

Output
The output displays the ranking of each team in descending order of their scores. In case of ties in scores, the teams are ordered alphabetically in reverse.

Copy code
1. Team B, 3 pts
2. Team A, 1 pt

Note
The regular expression is designed to accommodate spaces and varied formats within the input file lines. However, the basic structure of team name followed by score, separated by a comma, should be maintained.

Make sure to check the formatting when you paste it into your Markdown editor, as some markdown editors might require adjustments to recognize nested code blocks or other formatting features.

