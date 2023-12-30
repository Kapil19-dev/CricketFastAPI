from pydantic import BaseModel


class PointsTableRequest(BaseModel):
    team: int
    matches: int
    win: int
    loss: int
    draw: int
    fours: int
    sixes: int
    points: int
