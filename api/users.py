from typing import Annotated
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db.models.models import (
    Team,
    Stadium,
    Player,
    Matches,
    PlayerPerformance,
    PointsTable,
)
from db.postgres.database import SessionLocal
from exception import exceptions
from schemas.types import type_role
from service import update_db

user_router = APIRouter(tags=["users"])
user_exception = exceptions.CricketExceptions()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@user_router.get("/play_game")
async def play_match():
    update_db.update_complete_db()


@user_router.get("/team/all")
async def get_teams(db: db_dependency):
    team_model = db.query(Team).all()
    user_exception.get_exceptions(team_model)
    return team_model


@user_router.get("/team/{team_id}")
async def get_team_by_id(db: db_dependency, team_id: int):
    team_model = db.query(Team).filter(team_id == Team.team_id).first()
    user_exception.get_exceptions(team_model)
    return team_model


@user_router.get("/stadium/all")
async def get_stadium(db: db_dependency):
    stadium_model = db.query(Stadium).all()
    user_exception.get_exceptions(stadium_model)
    return stadium_model


@user_router.get("/stadium/{stadium_id}")
async def get_stadium_by_id(db: db_dependency, stadium_id: int):
    stadium_model = db.query(Stadium).filter(stadium_id == Stadium.stadium_id).first()
    user_exception.get_exceptions(stadium_model)
    return stadium_model


@user_router.get("/player/all")
async def get_players(db: db_dependency):
    player_model = db.query(Player).all()
    user_exception.get_exceptions(player_model)
    return player_model


@user_router.get("/player/{player_id}")
async def get_player_by_id(db: db_dependency, player_id: int):
    player_model = db.query(Player).filter(player_id == Player.player_id).first()
    user_exception.get_exceptions(player_model)
    return player_model


@user_router.get("/player/team/{team_id}")
async def get_player_by_team_id(db: db_dependency, team_id: int):
    player_model = db.query(Player).filter(team_id == Player.team).all()
    user_exception.get_exceptions(player_model)
    return player_model


@user_router.get("/player/role/{role_name}")
async def get_player_role(db: db_dependency, role_name: type_role):
    player_model = db.query(Player).filter(role_name.value == Player.role).all()
    user_exception.get_exceptions(player_model)
    return player_model


@user_router.get("/matches/all")
async def get_all_matches(db: db_dependency):
    match_model = db.query(Matches).all()
    user_exception.get_exceptions(match_model)
    return match_model


@user_router.get("/matches/{team_id}")
async def get_match_by_team_id(db: db_dependency, team_id: int):
    match_model = db.query(Matches).filter(Matches.team1 == team_id).all()
    user_exception.get_exceptions(match_model)
    return match_model


@user_router.get("/matches/venue/{venue_id}")
async def get_match_by_venue_id(db: db_dependency, venue_id: int):
    match_model = db.query(Matches).filter(Matches.stadium == venue_id).all()
    user_exception.get_exceptions(match_model)
    return match_model


@user_router.get("/performance/all")
async def get_all_performance(db: db_dependency):
    performance_model = db.query(PlayerPerformance).all()
    user_exception.get_exceptions(performance_model)
    return performance_model


@user_router.get("/performance/match/{match_id}")
async def get_performance_in_match(db: db_dependency, match_id: int):
    performance_model = (
        db.query(PlayerPerformance).filter(PlayerPerformance.match == match_id).all()
    )
    user_exception.get_exceptions(performance_model)
    return performance_model


@user_router.get("/performance/team/{team_id}")
async def get_performance_by_team(db: db_dependency, team_id: int):
    performance_model = (
        db.query(PlayerPerformance).filter(PlayerPerformance.team == team_id).all()
    )
    user_exception.get_exceptions(performance_model)
    return performance_model


@user_router.get("/performance/player/{player_id}")
async def get_performance_by_player(db: db_dependency, player_id: int):
    performance_model = (
        db.query(PlayerPerformance).filter(PlayerPerformance.player == player_id).all()
    )
    user_exception.get_exceptions(performance_model)
    return performance_model


@user_router.get("/points_table")
async def get_points_table(db: db_dependency):
    points_table_model = db.query(PointsTable).all()
    user_exception.get_exceptions(points_table_model)
    return points_table_model
