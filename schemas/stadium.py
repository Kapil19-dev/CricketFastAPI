from pydantic import BaseModel, Field


class StadiumRequest(BaseModel):
    stadium_name: str = Field(min_length=1)
    city: str
    state: str
    capacity: int = 0
    avg_first_innings_score: int = 0
    avg_second_innings_score: int = 0
    matches: int = 0
    home_team: int = 0
