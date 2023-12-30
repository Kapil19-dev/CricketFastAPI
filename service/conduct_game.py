from .game import CricketGame


def conduct_match(team1, team2):
    ongoing_game = CricketGame(team1, team2)
    game_result = ongoing_game.result()
    batting, bowling = ongoing_game.toss(team1, team2)
    return game_result, batting, bowling
