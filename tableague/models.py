from typing import Optional

from sqlmodel import Field, SQLModel

class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

class Team(SQLModel, table=True):
    pass