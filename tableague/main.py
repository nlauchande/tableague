import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def addscore():
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