import re
from collections import defaultdict
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor

class ScoringEngine:

    REGEXP_PARSE_INPUT =  r"^(?P<home_team>[\w\W]*)\s(?P<home_score>[\d]+)[\s]*\,[\s]*(?P<visitor_team>[\w\W]*)\s(?P<visitor_score>[\d]+)$"

    def score(game_fixtures: list[str]):
        pass


    @staticmethod    
    def parse_fixture(fixture,regxp=REGEXP_PARSE_INPUT):
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


class NaiveScoringEngine(ScoringEngine):

    @staticmethod
    def score(game_fixtures: list[str]):

        team_scores = defaultdict(lambda: 0)

        for line in game_fixtures:
            # parse line base on regular expression

            home_team, home_score, visitor_team, visitor_score = ScoringEngine.parse_fixture(line)  

            if visitor_score == home_score:
                team_scores[home_team] += 1
                team_scores[visitor_team] += 1
            elif visitor_score > home_score:
                team_scores[visitor_team] += 3
            else:
                team_scores[home_team] += 3

        return ScoringEngine.sort_results(team_scores)

class ParallelParseScoringEngine(ScoringEngine):

    #@staticmethod
    #def parallel_parse(game_fixtures):
    #    pool = mp.Pool(mp.cpu_count())
    #    #results = pool.map(ScoringEngine.parse_fixture, [fixture for fixture in game_fixtures],chunksize=10000)
    #    results = pool.map_async(ScoringEngine.parse_fixture, [fixture for fixture in game_fixtures],chunksize=5000)
    #    results.wait()
    #    return results.get()
    
    @staticmethod
    def parallel_parse(game_fixtures):
        with ProcessPoolExecutor() as executor:
            return list(executor.map(ScoringEngine.parse_fixture, game_fixtures, chunksize=100000))


    @staticmethod
    def score(game_fixtures: list[str]):

        team_scores = defaultdict(lambda: 0)
    
        parallel_parse_results = ParallelParseScoringEngine.parallel_parse(game_fixtures)

        for home_team, home_score, visitor_team, visitor_score in parallel_parse_results:

            if visitor_score == home_score:
                team_scores[home_team] += 1
                team_scores[visitor_team] += 1
            elif visitor_score > home_score:
                team_scores[visitor_team] += 3
            else:
                team_scores[home_team] += 3

        return ScoringEngine.sort_results(team_scores)
