from pydantic import BaseModel, Field

class TeamRequest(BaseModel):
    team_name: str = Field(min_length=1)
    matches: int = 0
    wins: int = 0
    loss: int = 0
    draw: int = 0
