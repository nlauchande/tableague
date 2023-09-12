from typer.testing import CliRunner
import typer
import tableague

runner = CliRunner()

from tableague import main as app


def test_happypath_app():
    typer.Typer(add_completion=False)
    result = runner.invoke(
        app.app, ["--filename", "tests/fixtures/test_main_input.txt"]
    )

    with open("tests/fixtures/test_main_output.txt", "r") as file:
        expected_output_content = file.read()

    assert result.exit_code == 0
    assert result.stdout == expected_output_content


def test_filenotfound_input():
    typer.Typer(add_completion=False)
    result = runner.invoke(
        app.app, ["--filename", "tests/fixtures/test_notexists_input.txt"]
    )
    assert result.exit_code != 0  # file not found
    assert (
        "File tests/fixtures/test_notexists_input.txt does not exist" in result.stdout
    )


def test_empty_file_input():
    typer.Typer(add_completion=False)
    result = runner.invoke(
        app.app, ["--filename", "tests/fixtures/test_empty_input.txt"]
    )
    assert result.exit_code != 0
    assert "Invalid value: File is empty" in result.stdout


def test_invalid_input():
    typer.Typer(add_completion=False)
    result = runner.invoke(
        app.app, ["--filename", "tests/fixtures/test_invalid_input.txt"]
    )

    assert result.exit_code != 0
    assert "Invalid format in one of the fixtures" in result.stdout
