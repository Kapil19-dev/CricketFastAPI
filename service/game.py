import random


def switch_strike(strike):
    if strike == 0:
        return 1
    else:
        return 0


class CricketGame:
    def __init__(self, team_id_1, team_id_2):
        self.team_id_1 = team_id_1
        self.team_id_2 = team_id_2

    def toss(self, team1, team2):
        batting_first = random.randint(team1, team2)
        if batting_first == team1:
            bowling_first = team2
        else:
            bowling_first = team1
        return batting_first, bowling_first

    def innings(self, first_innings, target=0):
        total_score = 0
        wickets = 0
        strike = 0
        current_partnership = [0, 1]
        player_runs = [0] * 11
        runs_in_overs = [-1] * 11
        player_wickets = [0] * 11
        player_fours = [0] * 11
        player_sixes = [0] * 11
        player_overs = [0] * 11
        player_maidens = [0] * 11
        player_economy = [0] * 11
        last_batsman = 1
        last_bowler = 6
        extras = 0

        for over in range(0, 5):
            for ball in range(1, 7):
                ball_event = random.randint(-1, 7)

                if (total_score > target or wickets == 10) and (first_innings == False):
                    break

                if ball_event == -1:
                    last_batsman += 1
                    player_wickets[last_bowler] += 1
                    current_partnership[strike] = last_batsman
                    wickets += 1

                elif ball_event == 4:
                    player_runs[current_partnership[strike]] += 4
                    player_fours[current_partnership[strike]] += 1
                    runs_in_overs[last_bowler] += 4
                    total_score += 4

                elif ball_event == 6:
                    player_runs[current_partnership[strike]] += 6
                    player_sixes[current_partnership[strike]] += 1
                    runs_in_overs[last_bowler] += 6
                    total_score += 6

                elif ball_event == 7:
                    ball -= 1
                    total_score += 1
                    extras += 1
                    runs_in_overs[last_bowler] += 1

                else:
                    player_runs[current_partnership[strike]] += ball_event
                    total_score += ball_event
                    runs_in_overs[last_bowler] += ball_event

            if runs_in_overs[last_bowler] == 0:
                player_maidens[last_bowler] += 1
            player_overs[last_bowler] += 1
            if runs_in_overs[last_bowler] > 0:
                player_economy[last_bowler] = (
                    runs_in_overs[last_bowler] / player_overs[last_bowler]
                )
            last_bowler += 1
            strike = switch_strike(strike)

        return {
            "total_score": total_score,
            "wickets": wickets,
            "player_runs": player_runs,
            "player_wickets": player_wickets,
            "player_fours": player_fours,
            "player_sixes": player_sixes,
            "current_partnership": current_partnership,
            "extras": extras,
            "runs_in_overs": runs_in_overs,
            "player_overs": player_overs,
            "player_maidens": player_maidens,
            "player_economy": player_economy,
        }

    def result(self):
        batting_first, bowling_first = self.toss(self.team_id_1, self.team_id_2)

        first_innings = self.innings(True)
        second_innings = self.innings(False, first_innings["total_score"] + 1)

        first_innings_fours = 0
        first_innings_sixes = 0
        second_innings_fours = 0
        second_innings_sixes = 0

        for four in first_innings["player_fours"]:
            first_innings_fours += four

        for six in first_innings["player_sixes"]:
            first_innings_sixes += six

        for four in second_innings["player_fours"]:
            second_innings_fours += four

        for six in second_innings["player_sixes"]:
            second_innings_sixes += six

        if first_innings["total_score"] > second_innings["total_score"]:
            return {
                "winner": batting_first,
                "toss": batting_first,
                "first_innings": first_innings,
                "second_innings": second_innings,
            }

        elif second_innings["total_score"] > first_innings["total_score"]:
            return {
                "winner": bowling_first,
                "toss": batting_first,
                "first_innings": first_innings,
                "second_innings": second_innings,
            }

        else:
            first_innings_boundary_count = first_innings_sixes + first_innings_fours
            second_innings_boundary_count = second_innings_sixes + second_innings_fours

            if first_innings_boundary_count > second_innings_boundary_count:
                return {
                    "winner": batting_first,
                    "toss": batting_first,
                    "first_innings": first_innings,
                    "second_innings": second_innings,
                }

            elif second_innings_boundary_count > first_innings_boundary_count:
                return {
                    "winner": bowling_first,
                    "toss": batting_first,
                    "first_innings": first_innings,
                    "second_innings": second_innings,
                }
            else:
                if first_innings_fours > second_innings_fours:
                    return {
                        "winner": batting_first,
                        "toss": batting_first,
                        "first_innings": first_innings,
                        "second_innings": second_innings,
                    }
                elif second_innings_fours > first_innings_fours:
                    return {
                        "winner": bowling_first,
                        "toss": batting_first,
                        "first_innings": first_innings,
                        "second_innings": second_innings,
                    }
                else:
                    if first_innings_sixes > second_innings_sixes:
                        return {
                            "winner": batting_first,
                            "toss": batting_first,
                            "first_innings": first_innings,
                            "second_innings": second_innings,
                        }
                    elif second_innings_sixes > first_innings_sixes:
                        return {
                            "winner": bowling_first,
                            "toss": batting_first,
                            "first_innings": first_innings,
                            "second_innings": second_innings,
                        }

        return {
            "winner": None,
            "toss": batting_first,
            "first_innings": first_innings,
            "second_innings": second_innings,
        }


# game = CricketGame(6,7)
# result = game.result()
# print(result)
