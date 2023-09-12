# Table League CLI

This CLI tool is designed to parse a given input file, which contains fixture results of soccer matches, calculate the final table standing. It calculates and displays the rankings of teams based on their scores.

## Main Dependencies

- `typer`: For creating command-line applications.
- `poetry`: For dependency management

## Installation
1. Ensure you have Python 3.8+ installed  on your system.
2. Install the required libraries:
3. Install Poetry (if you haven't already) : 
`curl -sSL https://install.python-poetry.org | python3 -`
4. Clone the Repository : 
`git clone https://github.com/nlauchande/tableague.git`
5. Navigate to the Directory :
 `cd tableleague`
6. Install the Project's Dependencies with Poetry
7. Activate the Virtual Environment  : `poetry shell`

## Executing a CLI command


1. While on the virtual environment created on the above space

`tableague --filename ./tests/resources/test_main_input.txt > output.txt`

2. General help

`tableague --help`

## Run tests
1. Run tests ( assuming environment is installed locally)

`poetry run pytest -vvv`

## Generate fake testing data
1. While on the virtual environment above you can change the script below to generate files with different sizes

`python ./performance_scripts/generate_fake_game_data.py > huge_file.txt`

## Disclaimer
The intention of this project is solely as a demonstration of different tools and architecture of a sample CLI package in Python.