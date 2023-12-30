from db.models.models import Team
from db.postgres.database import SessionLocal, engine

SessionLocal.configure(bind=engine)
s = SessionLocal()


def update_team_db(winner, team1_id, team2_id):
    team1 = s.query(Team).filter(Team.team_id == team1_id).all()[0]
    team2 = s.query(Team).filter(Team.team_id == team2_id).all()[0]

    if team1_id == winner:
        team1.wins = team1.wins + 1
        team2.loss = team2.loss + 1
    elif team2_id == winner:
        team2.wins = team2.wins + 1
        team1.loss = team1.loss + 1
    else:
        team1.draw = team1.draw + 1
        team2.draw = team2.draw + 1
    team1.matches = team1.matches + 1
    team2.matches = team2.matches + 1
    s.commit()
