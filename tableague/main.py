import typer
import re
from .scoring_engine import NaiveScoringEngine

app = typer.Typer()


def express_parse_input_file(fixture):
    regexp_parse_input = r"^(?P<home_team>[\w\W]*)\s(?P<home_score>[\d]+)[\s]*\,[\s]*(?P<visitor_team>[\w\W]*)\s(?P<visitor_score>[\d]+)$"

    team_scores = {}

    for line in fixture:
        # parse line base on regular expression
        matches = re.search(regexp_parse_input, line)

        home_team = matches.group("home_team")
        home_score = matches.group("home_score")
        visitor_team = matches.group("visitor_team")
        visitor_score = matches.group("visitor_score")

        for team in [home_team, visitor_team]:
            if team not in team_scores:
                team_scores[team] = 0

        if visitor_score == home_score:
            team_scores[home_team] += 1
            team_scores[visitor_team] += 1
        elif visitor_score > home_score:
            team_scores[visitor_team] += 3
        else:
            team_scores[home_team] += 3

    # sort team scores by value showing the keys
    return sorted(
        team_scores.items(), key=lambda x: (x[1], [-ord(c) for c in x[0]]), reverse=True
    )


@app.command()
def addscores(filename: str = "input.txt"):
    """
    add multiple-scores based on a file
    """
    with open(filename) as f:
        lines = f.readlines()
    result = express_parse_input_file(lines)

    i = 1
    prev_points = -1
    pos = 0
    for team, points in result:
        s = "" if points == 1 else "s"
        end = "\n" if i < len(result) else ""
        if points != prev_points:
            pos = i
        print(f"{pos}. {team}, {points} pt{s}", end=end)
        prev_points = points
        i += 1


if __name__ == "__main__":
    app()
