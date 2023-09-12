import string
import typer
from enum import Enum
import os
from .scoring_engine import NaiveScoringEngine, ParallelParseScoringEngine

app = typer.Typer()


def get_file_contents(filename: str):
    with open(filename) as f:
        lines = f.readlines()
    return lines


class InvalidFixtureFormatException(typer.BadParameter):
    pass


class EmptyFileException(typer.BadParameter):
    pass


class Engine(str, Enum):
    naive = "naive"
    turbo = "turbo"


@app.command()
def addscores(filename: str = "input.txt", engine: Engine = Engine.naive):
    if not os.path.isfile(filename):
        raise typer.BadParameter(f"File {filename} does not exist")

    lines = get_file_contents(filename)

    if len(lines) == 0:
        raise EmptyFileException(f"File is empty")

    engine = (
        NaiveScoringEngine if engine != Engine.turbo else ParallelParseScoringEngine
    )
    result = None

    try:
        result = engine.score(lines)
    except AttributeError as e:
        raise InvalidFixtureFormatException(f"Invalid format in one of the fixtures")

    engine.print_results(result)


if __name__ == "__main__":
    app()
