from typer.testing import CliRunner

runner = CliRunner()

from tableague import main as app

def test_app():
    pass
    result = runner.invoke(app, ["addscore","--result","Lions 3, Snakes 3"])
    #assert result.exit_code == 0
    #assert "Hello Camila" in result.stdout
    