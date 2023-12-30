import numpy as np

from db.models.models import PointsTable, Matches
from db.postgres.database import SessionLocal, engine
from service.conduct_game import conduct_match
from service.game import CricketGame

SessionLocal.configure(bind=engine)
s = SessionLocal()


def update_points_table_db(game_result, batting, bowling):
    winner = game_result["winner"]
    first_innings_fours = sum(game_result["first_innings"]["player_fours"])
    first_innings_sixes = sum(game_result["first_innings"]["player_sixes"])
    second_innings_fours = sum(game_result["second_innings"]["player_fours"])
    second_innings_sixes = sum(game_result["second_innings"]["player_sixes"])

    points_data_first_innings = (
        s.query(PointsTable).filter(PointsTable.team == batting).all()[0]
    )
    points_data_second_innings = (
        s.query(PointsTable).filter(PointsTable.team == bowling).all()[0]
    )

    points_data_first_innings.matches += 1
    points_data_second_innings.matches += 1

    points_data_first_innings.fours += first_innings_fours
    points_data_second_innings.fours += second_innings_fours
    points_data_first_innings.sixes += first_innings_sixes
    points_data_second_innings.sixes += second_innings_sixes

    if winner == batting:
        points_data_first_innings.win += 1
        points_data_second_innings.loss += 1
        points_data_first_innings.points += 2

    elif winner == bowling:
        points_data_second_innings.win += 1
        points_data_first_innings.loss += 1
        points_data_second_innings.points += 2

    else:
        points_data_first_innings.draw += 1
        points_data_second_innings.draw += 1
        points_data_first_innings.points += 1
        points_data_second_innings.points += 1

    s.commit()
