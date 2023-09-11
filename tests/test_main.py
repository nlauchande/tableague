from typer.testing import CliRunner
import typer

runner = CliRunner()

from tableague import main as app


def test_happypath_app():
    typer.Typer(add_completion=False)
    result = runner.invoke(
        app.app, ["--filename", "tests/resources/test_main_input.txt"]
    )

    with open("tests/resources/test_main_output.txt", "r") as file:
        expected_output_content = file.read()

    assert result.exit_code == 0
    assert result.stdout == expected_output_content
