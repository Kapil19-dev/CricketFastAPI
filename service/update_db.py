import numpy as np

from db.models.models import Matches
from db.postgres.database import SessionLocal, engine
from .conduct_game import conduct_match
from .update_match import update_match_db
from .update_player import update_player_db
from .update_player_performance import update_player_performance_db
from .update_points_table import update_points_table_db
from .update_stadium import update_stadium_db
from .update_team import update_team_db

SessionLocal.configure(bind=engine)
s = SessionLocal()

game_ids = np.array(s.query(Matches.match_id).all()).reshape(-1)


def update_complete_db():
    for current_game_id in game_ids:
        # stadium_id = s.query(Matches.stadium).filter(Matches.match_id == int(current_game_id)).all()[0][0]
        current_game_data = (
            s.query(Matches).filter(Matches.match_id == int(current_game_id)).all()[0]
        )
        team1 = current_game_data.team1
        team2 = current_game_data.team2
        stadium_id = current_game_data.stadium
        game_result, batting, bowling = conduct_match(team1, team2)
        update_match_db(game_result, current_game_data)
        update_stadium_db(game_result, stadium_id)
        update_team_db(game_result["winner"], team1, team2)
        update_points_table_db(game_result, batting, bowling)
        update_player_db(game_result, batting, bowling)
        update_player_performance_db(game_result, batting, bowling, current_game_id)
        s.commit()
