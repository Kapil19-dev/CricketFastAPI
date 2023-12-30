from .types import type_role
from pydantic import BaseModel, Field



class PlayerRequest(BaseModel):
    team: int
    name: str = Field(min_length=1)
    role: type_role
    runs: int = 0
    hundreds: int = 0
    fifties: int = 0
    highest_score: int = 0
    fours: int = 0
    sixes: int = 0
    average: int = 0
    overs: int = 0
    wickets: int = 0
    maidens: int = 0
    fifers: int = 0
    economy: float = 0