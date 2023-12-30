from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from db.models import models
from db.postgres.database import SessionLocal
from schemas.points_table import PointsTableRequest
from schemas.stadium import StadiumRequest
from schemas.team import TeamRequest
from schemas.player import PlayerRequest
from schemas.match import MatchRequest
from exception import exceptions

admin_router = APIRouter(tags=["admin"])
admin_exception = exceptions.CricketExceptions()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@admin_router.post("/team/add", status_code=status.HTTP_201_CREATED)
async def create_team(db: db_dependency, team_request: TeamRequest):
    team_model = models.Team(**team_request.dict())
    admin_exception.get_exceptions(team_model)
    # if team_model is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED, detail="Not a Valid Entry"
    #     )
    db.add(team_model)
    db.commit()


@admin_router.post("/stadium/add", status_code=status.HTTP_201_CREATED)
async def create_stadium(db: db_dependency, stadium_request: StadiumRequest):
    stadium_model = models.Stadium(**stadium_request.dict())
    admin_exception.get_exceptions(stadium_model)
    # if stadium_model is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED, detail="Not a Valid Entry"
    #     )
    db.add(stadium_model)
    db.commit()


@admin_router.post("/player/add", status_code=status.HTTP_201_CREATED)
async def create_player(db: db_dependency, player_request: PlayerRequest):
    player_model = models.Player(**player_request.dict())
    admin_exception.get_exceptions(player_model)
    # if player_model is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED, detail="Not a Valid Entry"
    #     )
    db.add(player_model)
    db.commit()


@admin_router.post("/matches/add", status_code=status.HTTP_201_CREATED)
async def create_match(db: db_dependency, match_request: MatchRequest):
    match_model = models.Matches(**match_request.dict())
    admin_exception.get_exceptions(match_model)
    db.add(match_model)
    db.commit()


@admin_router.post("/points_table/add", status_code=status.HTTP_201_CREATED)
async def initialize_points_table(db: db_dependency, point_request: PointsTableRequest):
    point_model = models.PointsTable(**point_request.dict())
    admin_exception.get_exceptions(point_model)
    db.add(point_model)
    db.commit()
