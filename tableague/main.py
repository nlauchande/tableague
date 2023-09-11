import typer
import re
from .scoring_engine import NaiveScoringEngine

app = typer.Typer()

def get_file_contents(filename: str):
    with open(filename) as f:
        lines = f.readlines()
    return lines


@app.command()
def addscores(filename: str = "input.txt"):
    lines = get_file_contents(filename)
    result = NaiveScoringEngine.score(lines)
    NaiveScoringEngine.print_results(result)

if __name__ == "__main__":
    app()
