# Table League CLI

This CLI tool is designed to parse a given input file, which contains fixture results of soccer matches. It calculates and displays the rankings of teams based on their scores.

## Dependencies

- `typer`: For creating command-line applications.
- `re`: Python's regular expression module.

## Installation


1. Ensure you have Python 3.8 installed  on your system.
2. Install the required libraries:
3. Clone the Repository : ``
4. Navigate to the Directory : ``
5. Install Poetry (if you haven't already) : `curl -sSL https://install.python-poetry.org | python3 -`
6. Install the Project's Dependencies with Poetry
7. Activate the Virtual Environment (Optional) : `poetry shell`

## Executing a CLI command
`tableague --filename .test/resources/test_main_input.txt > output.txt`


## Generate fake testing data
`python ./performance_scripts/generate_fake_game_data.py > huge_file.txt`