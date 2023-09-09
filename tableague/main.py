import typer

app = typer.Typer()

@app.callback()
def callback():
    """
    Awesome Portal Table League CLI
    """

@app.command()
def addscores(filename:str):
    """
    add multiple-scores based on a file
    """
    typer.echo("Add multiple scores on a file")

@app.command()
def addscore(home:str,visitor:str,home_score:int,visitor_score:int):
    """
    add score
    """
    typer.echo("Adding game")


@app.command()
def showtable():
    """
    Add game
    """
    typer.echo("Add game")


if __name__ == "__main__":
    app()