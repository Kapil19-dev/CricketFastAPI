import numpy as np

from db.models.models import Matches, Player, Team
from db.postgres.database import SessionLocal, engine


SessionLocal.configure(bind=engine)
s = SessionLocal()

# game_ids = np.array(s.query(Matches.match_id).all()).reshape(-1)


def update_player_db(game_result, batting, bowling):
    matches = s.query(Team.matches).filter(Team.team_id == batting).all()[0][0]
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
        player_data = (
            s.query(Player)
            .filter(Player.player_id == int(first_innings_players[id]))
            .all()[0]
        )
        player_score = game_result["first_innings"]["player_runs"][id]
        player_fours = game_result["first_innings"]["player_fours"][id]
        player_sixes = game_result["first_innings"]["player_sixes"][id]
        player_wickets = game_result["second_innings"]["player_wickets"][id]
        bowler_overs = game_result["second_innings"]["player_overs"][id]
        bowler_maidens = game_result["second_innings"]["player_maidens"][id]
        bowler_runs = game_result["second_innings"]["runs_in_overs"][id]
        bowler_economy = game_result["second_innings"]["player_economy"][id]

        player_data.runs += player_score
        if player_score >= 100:
            player_data.hundreds += 1
            player_data.fifties += 1
        if 50 <= player_score < 100:
            player_data.fifties += 1

        player_data.highest_score = max(player_data.highest_score, player_score)
        player_data.fours += player_fours
        player_data.sixes += player_sixes
        player_data.wickets += player_wickets
        player_data.overs += bowler_overs
        player_data.maidens += bowler_maidens
        player_data.average = player_data.runs / matches
        player_data.economy = (player_data.economy + bowler_economy) / matches
        if player_wickets >= 5:
            player_data.fifers += 1

        if bowler_runs > -1:
            player_data.economy = (bowler_runs) / player_data.overs

    for id in range(len(second_innings_players)):
        player_data = (
            s.query(Player)
            .filter(Player.player_id == int(second_innings_players[id]))
            .all()[0]
        )
        player_score = game_result["second_innings"]["player_runs"][id]
        player_fours = game_result["second_innings"]["player_fours"][id]
        player_sixes = game_result["second_innings"]["player_sixes"][id]
        player_wickets = game_result["first_innings"]["player_wickets"][id]
        bowler_overs = game_result["first_innings"]["player_overs"][id]
        bowler_maidens = game_result["first_innings"]["player_maidens"][id]
        bowler_runs = game_result["first_innings"]["runs_in_overs"][id]
        bowler_economy = game_result["first_innings"]["player_economy"][id]
        player_data.runs += player_score
        if player_score >= 100:
            player_data.hundreds += 1
            player_data.fifties += 1
        if 50 <= player_score < 100:
            player_data.fifties += 1

        player_data.highest_score = max(player_data.highest_score, player_score)
        player_data.fours += player_fours
        player_data.sixes += player_sixes
        player_data.wickets += player_wickets
        player_data.overs += bowler_overs
        player_data.maidens += bowler_maidens
        player_data.average = player_data.runs / matches
        player_data.economy = (player_data.economy + bowler_economy) / matches
        if player_wickets >= 5:
            player_data.fifers += 1

        if bowler_runs > -1:
            player_data.economy = bowler_runs / player_data.overs

    s.commit()
