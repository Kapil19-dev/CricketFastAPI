import numpy as np

from db.models.models import Matches, Stadium
from db.postgres.database import engine, SessionLocal
from service.conduct_game import conduct_match

SessionLocal.configure(bind=engine)
s = SessionLocal()


def update_stadium_db(game_result, stadium_id):
    current_stadium = s.query(Stadium).filter(Stadium.stadium_id == stadium_id).all()[0]
    current_matches = current_stadium.matches
    total_matches = current_matches + 1
    first_innings_score = game_result["first_innings"]["total_score"]
    second_innings_score = game_result["second_innings"]["total_score"]
    current_stadium.avg_first_innings_score = (
        (current_stadium.avg_first_innings_score * current_matches)
        + first_innings_score
    ) / total_matches
    current_stadium.avg_second_innings_score = (
        (current_stadium.avg_second_innings_score * current_matches)
        + second_innings_score
    ) / total_matches
    current_stadium.matches = total_matches
    s.commit()
