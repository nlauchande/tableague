import re
from collections import defaultdict
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor


class ScoringEngine:
    REGEXP_PARSE_INPUT = r"^(?P<home_team>[\w\W]*)\s(?P<home_score>[\d]+)[\s]*\,[\s]*(?P<visitor_team>[\w\W]*)\s(?P<visitor_score>[\d]+)$"

    def score(game_fixtures: list[str]):
        pass

    @staticmethod
    def parse_fixture(fixture, regxp=REGEXP_PARSE_INPUT):
        # parse line base on regular expression
        matches = re.search(regxp, fixture)

        home_team = matches.group("home_team")
        home_score = matches.group("home_score")
        visitor_team = matches.group("visitor_team")
        visitor_score = matches.group("visitor_score")

        return home_team, home_score, visitor_team, visitor_score

    @staticmethod
    def print_results(results):
        i = 1
        prev_points = -1
        pos = 0
        for team, points in results:
            s = "" if points == 1 else "s"
            end = "\n" if i < len(results) else ""
            if points != prev_points:
                pos = i
            print(f"{pos}. {team}, {points} pt{s}", end=end)
            prev_points = points
            i += 1

    @staticmethod
    def sort_results(team_scores):
        # sort team scores by value showing the keys
        return sorted(
            team_scores.items(),
            key=lambda x: (x[1], [-ord(c) for c in x[0]]),
            reverse=True,
        )

    @staticmethod
    def return_scores(home_team_score, visitor_team_score):
        if visitor_team_score == home_team_score:
            return 1, 1
        elif home_team_score > visitor_team_score:
            return 3, 0
        else:
            return 0, 3


class NaiveScoringEngine(ScoringEngine):
    @staticmethod
    def score(game_fixtures: list[str]):
        team_scores = defaultdict(int)

        for line in game_fixtures:
            (
                home_team,
                home_score,
                visitor_team,
                visitor_score,
            ) = ScoringEngine.parse_fixture(line)
            home_points, visitor_points = ScoringEngine.return_scores(
                home_score, visitor_score
            )
            team_scores[home_team] += home_points
            team_scores[visitor_team] += visitor_points

        return ScoringEngine.sort_results(team_scores)


class ParallelParseScoringEngine(ScoringEngine):
    @staticmethod
    def parallel_parse(game_fixtures):
        with ProcessPoolExecutor() as executor:
            return list(
                executor.map(
                    ScoringEngine.parse_fixture, game_fixtures, chunksize=100000
                )
            )

    @staticmethod
    def score(game_fixtures: list[str]):
        team_scores = defaultdict(int)
        parallel_parse_results = ParallelParseScoringEngine.parallel_parse(
            game_fixtures
        )

        for (
            home_team,
            home_score,
            visitor_team,
            visitor_score,
        ) in parallel_parse_results:
            home_points, visitor_points = ScoringEngine.return_scores(
                home_score, visitor_score
            )
            team_scores[home_team] += home_points
            team_scores[visitor_team] += visitor_points

        return ScoringEngine.sort_results(team_scores)
