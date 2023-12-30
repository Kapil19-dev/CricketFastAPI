import numpy as np

from db.models.models import Matches, Player, Team, PlayerPerformance
from db.postgres.database import SessionLocal, engine
from service.conduct_game import conduct_match

SessionLocal.configure(bind=engine)
s = SessionLocal()

game_ids = np.array(
    s.query(Matches.match_id).order_by(Matches.match_id.asc()).all()
).reshape(-1)


def update_player_performance_db(game_result, batting, bowling, current_game_id):
    first_innings_players = np.array(
        s.query(Player.player_id)
        .filter(Player.team == batting)
        .order_by(Player.player_id.asc())
        .all()
    ).reshape(-1)
    second_innings_players = np.array(
        s.query(Player.player_id)
        .filter(Player.team == bowling)
        .order_by(Player.player_id.asc())
        .all()
    ).reshape(-1)

    for id in range(len(first_innings_players)):
        player_score = game_result["first_innings"]["player_runs"][id]
        player_fours = game_result["first_innings"]["player_fours"][id]
        player_sixes = game_result["first_innings"]["player_sixes"][id]
        bowler_wickets = game_result["second_innings"]["player_wickets"][id]
        bowler_overs = game_result["second_innings"]["player_overs"][id]
        bowler_maidens = game_result["second_innings"]["player_maidens"][id]
        # bowler_runs = game_result["second_innings"]["runs_in_overs"][id]
        bowler_economy = game_result["second_innings"]["player_economy"][id]
        player_performance = PlayerPerformance(
            match=int(current_game_id),
            team=batting,
            player=int(first_innings_players[id]),
            runs=player_score,
            fours=player_fours,
            sixes=player_sixes,
            overs=bowler_overs,
            wickets=bowler_wickets,
            maiden=bowler_maidens,
            economy=bowler_economy,
        )
        s.add(player_performance)

    for id in range(len(second_innings_players)):
        player_score = game_result["second_innings"]["player_runs"][id]
        player_fours = game_result["second_innings"]["player_fours"][id]
        player_sixes = game_result["second_innings"]["player_sixes"][id]
        bowler_wickets = game_result["first_innings"]["player_wickets"][id]
        bowler_overs = game_result["first_innings"]["player_overs"][id]
        bowler_maidens = game_result["first_innings"]["player_maidens"][id]
        # bowler_runs = game_result["first_innings"]["runs_in_overs"][id]
        bowler_economy = game_result["first_innings"]["player_economy"][id]

        player_performance = PlayerPerformance(
            match=int(current_game_id),
            team=bowling,
            player=int(second_innings_players[id]),
            runs=player_score,
            fours=player_fours,
            sixes=player_sixes,
            overs=bowler_overs,
            wickets=bowler_wickets,
            maiden=bowler_maidens,
            economy=bowler_economy,
        )
        s.add(player_performance)
    s.commit()
