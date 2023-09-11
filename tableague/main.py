import typer
import re
from .scoring_engine import NaiveScoringEngine,ParallelParseScoringEngine

app = typer.Typer()

def get_file_contents(filename: str):
    with open(filename) as f:
        lines = f.readlines()
    return lines

@app.command()
def addscores(filename: str = "input.txt" ,engine:str='naive'):
    lines = get_file_contents(filename)
    engine=NaiveScoringEngine if engine!='turbo' else ParallelParseScoringEngine
    result = engine.score(lines)
    engine.print_results(result)

if __name__ == "__main__":
    app()
