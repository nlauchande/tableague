from typing import Optional


@dataclass
class Team():
    name: str = 'Unamed team'
    points: int = 0

class Game:
    visitor_team: Team
    home_team: Team
    visitor_score: int
    home_score: int

    def result(team:str):
        raise ValueError(f"Team {team} is not in this game") if team not in [self.visitor_team.name,self.home_team.name]
        
        if team == self.visitor_team.name:
            return 3 self.visitor_score
        else:
            return self.home_score
        


class ScoringUtils:
    def parse_score(fixture:str)->Optional[Game]:
        pass

class ScoringEngine:
    teams: Dictionary[Team]
    games: List[Game]
    scores: List[Team]

    
    def add_game(Game):
        pass

    def add_score():
        pass
