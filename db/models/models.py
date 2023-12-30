import enum
from db.postgres.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy import types


class MyEnum(str, enum.Enum):
    Batsman = "Batsman"
    Bowler = "Bowler"


class Team(Base):
    __tablename__ = "team"

    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String)
    matches = Column(Integer)
    wins = Column(Integer)
    loss = Column(Integer)
    draw = Column(Integer)


class Stadium(Base):
    __tablename__ = "stadium"
    stadium_id = Column(Integer, primary_key=True, index=True)
    stadium_name = Column(String)
    city = Column(String)
    state = Column(String)
    capacity = Column(Integer)
    avg_first_innings_score = Column(Integer)
    avg_second_innings_score = Column(Integer)
    matches = Column(Integer)
    home_team = Column(Integer, ForeignKey("team.team_id"))


class Matches(Base):
    __tablename__ = "matches"
    match_id = Column(Integer, primary_key=True, index=True)
    stadium = Column(Integer, ForeignKey("stadium.stadium_id"))
    team1 = Column(Integer, ForeignKey("team.team_id"))
    team2 = Column(Integer, ForeignKey("team.team_id"))
    status = Column(String)
    date = Column(types.Date)


class Player(Base):
    __tablename__ = "player"
    player_id = Column(Integer, primary_key=True, index=True)
    team = Column(Integer, ForeignKey("team.team_id"))
    name = Column(String)
    role = Column(Enum(MyEnum))
    runs = Column(Integer)
    hundreds = Column(Integer)
    fifties = Column(Integer)
    highest_score = Column(Integer)
    fours = Column(Integer)
    sixes = Column(Integer)
    average = Column(Integer)
    overs = Column(Integer)
    wickets = Column(Integer)
    maidens = Column(Integer)
    fifers = Column(Integer)
    economy = Column(types.Double)


class PointsTable(Base):
    __tablename__ = "points_table"
    points_id = Column(Integer, primary_key=True, index=True)
    team = Column(Integer, ForeignKey("team.team_id"))
    matches = Column(Integer)
    win = Column(Integer)
    loss = Column(Integer)
    draw = Column(Integer)
    fours = Column(Integer)
    sixes = Column(Integer)
    points = Column(Integer)


class PlayerPerformance(Base):
    __tablename__ = "player_performance"
    performance_id = Column(Integer, primary_key=True, index=True)
    match = Column(Integer, ForeignKey("matches.match_id"))
    team = Column(Integer, ForeignKey("team.team_id"))
    player = Column(Integer, ForeignKey("player.player_id"))
    runs = Column(Integer)
    fours = Column(Integer)
    sixes = Column(Integer)
    overs = Column(Integer)
    wickets = Column(Integer)
    maiden = Column(Integer)
    economy = Column(types.Double)
