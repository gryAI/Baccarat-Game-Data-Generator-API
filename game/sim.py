import sys
import os
import string
import random
import datetime
from dataclasses import dataclass

# Adjust the Python path to include the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from helper_functions import play_game, announce_winner, announce_bet_winner, compute_payout

@dataclass
class BaccaratResult:
    game: str
    game_id: str
    player_id: str
    status: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    player_hand: list
    player_hand_value: int
    banker_hand: list
    banker_hand_value: int
    last_action: str
    player_wager: float
    player_payout: float
    game_outcome: str
    player_bet: str
    player_bet_outcome: str

def simulate_baccarat() -> BaccaratResult:
    game = "Baccarat"
    game_id = 'GID-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    player_id = f'PID-{random.randint(1, 50):06}'
    player_wager = float(random.randint(0, int(1001)))
    player_bet = random.choice(['Player', 'Banker', 'Tie'])
    status = "Success"
    start_time = datetime.datetime.fromtimestamp(
        random.randint(int(datetime.datetime(2023, 1, 1).timestamp()), 
                       int(datetime.datetime(2024, 6, 30, 23, 59, 59).timestamp())))
    end_time = start_time + datetime.timedelta(minutes=random.randint(1, 3), seconds = random.randint(start_time.second, 59))

    if player_wager > 500 or (start_time.hour >= 20 or start_time.hour >= 0 and start_time.hour <=9 and player_bet == 'Banker'):
        game_result = play_game('rigged')
    else:
        game_result = play_game('normal')

    player_hand = [
        {
            'value': game_result.player_hand[0].split(' of ')[0],
            'rank': game_result.player_hand[0].split(' of ')[1]
        },
        {
            'value': game_result.player_hand[1].split(' of ')[0],
            'rank': game_result.player_hand[1].split(' of ')[1]
        },
    ]

    if len(game_result.player_hand) == 3:
        player_hand.append(
            {
                'value': game_result.player_hand[2].split(' of ')[0],
                'rank': game_result.player_hand[2].split(' of ')[1]
            }
        )

    player_hand_value = game_result.player_hand_value

    banker_hand = [
        {
            'value': game_result.banker_hand[0].split(' of ')[0],
            'rank': game_result.banker_hand[0].split(' of ')[1]
        },
        {
            'value': game_result.banker_hand[1].split(' of ')[0],
            'rank': game_result.banker_hand[1].split(' of ')[1]
        },
    ]

    if len(game_result.banker_hand) == 3:
        banker_hand.append(
            {
                'value': game_result.banker_hand[2].split(' of ')[0],
                'rank': game_result.banker_hand[2].split(' of ')[1]
            }
        )

    banker_hand_value = game_result.banker_hand_value

    winner = announce_winner(player_hand_value, banker_hand_value)
    player_payout = compute_payout(winner, player_wager, player_bet)
    last_action = game_result.last_action
    game_outcome = f'{winner} wins!' if winner in ['Player', 'Banker'] else "It's a tie!"
    player_bet_outcome = announce_bet_winner(player_bet, winner)

    return BaccaratResult(
        game, game_id, player_id, status, start_time, end_time,
        player_hand, player_hand_value, banker_hand, banker_hand_value, last_action,
        player_wager, player_payout,
        game_outcome, player_bet, player_bet_outcome
    )