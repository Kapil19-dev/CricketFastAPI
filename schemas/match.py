from datetime import date, datetime

from pydantic import BaseModel, Field
from sqlalchemy import types


class MatchRequest(BaseModel):
    stadium: int
    team1: int
    team2: int
    status: str
    date: date
