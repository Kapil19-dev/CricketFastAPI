from db.models.models import Matches, Team
from db.postgres.database import engine, SessionLocal
import numpy as np
from .conduct_game import conduct_match

SessionLocal.configure(bind=engine)
s = SessionLocal()


def update_match_db(game_result, current_game_data):
    winning_team_name = (
        s.query(Team.team_name)
        .filter(Team.team_id == game_result["winner"])
        .all()[0][0]
    )
    current_game_data.status = winning_team_name
    s.commit()
