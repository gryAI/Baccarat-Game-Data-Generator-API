# Libraries
import pandas as pd
import numpy as np
import itertools
import random
from dataclasses import dataclass


# Dataclass:
@dataclass
class GameResult:
    player_hand: tuple
    player_hand_value: int
    banker_hand: tuple
    banker_hand_value: int
    last_action: str
    

# Helper Functions
def build_deck():

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    original_deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    
    return original_deck


def rebuild_deck(original_deck, excluded_cards: list):
    deck_remaining = [card for card in original_deck if card not in excluded_cards]
    return deck_remaining


def build_combinations(deck):

    card_combinations = list(itertools.combinations(deck, 2))
    card_combinations_df = pd.DataFrame(card_combinations, columns = ['card_1', 'card_2'])

    card_combinations_df['card_combination'] = card_combinations_df.apply(
        lambda row:
            (row['card_1'], row['card_2']), 
            axis = 1
    )

    card_combinations_df['card_1_value'] = card_combinations_df['card_1'].apply(
        lambda x: 
            int(x.split(' ')[0]) if x.split(' ')[0].isdigit() else 1 if x.split(' ')[0] == 'A' else 10
    )

    card_combinations_df['card_2_value'] = card_combinations_df['card_2'].apply(
        lambda x: 
            int(x.split(' ')[0]) if x.split(' ')[0].isdigit() else 1 if x.split(' ')[0] == 'A' else 10
    )

    card_combinations_df['card_combination_value'] = card_combinations_df.apply(
    lambda row:
        int(str(row['card_1_value'] + row['card_2_value'])[-1]),
        axis = 1
    )

    deck_dict = dict(zip(card_combinations_df['card_combination'], card_combinations_df['card_combination_value']))

    return card_combinations, card_combinations_df, deck_dict


def draw_player_hand():
    
    deck = build_deck()
    card_combinations, card_combinations_df, deck_dict = build_combinations(deck)

    player_hand = tuple(random.choice(card_combinations))
    player_hand_value = int(str(deck_dict[player_hand])[-1])

    return player_hand, player_hand_value


def draw_banker_hand(player_hand, with_weights = 'No'):

    original_deck = build_deck()
    deck_remaining = rebuild_deck(original_deck, player_hand)
    card_combinations, card_combinations_df, deck_dict = build_combinations(deck_remaining)

    if with_weights != 'No':
        weights = np.where(card_combinations_df['card_combination_value'] >= 7, 10, 1)

    else:
        weights = np.ones(len(card_combinations))

    
    banker_hand = tuple(random.choices(card_combinations, weights = weights)[0])
    banker_hand_value = int(str(deck_dict[banker_hand])[-1])

    return banker_hand, banker_hand_value


def draw_player(drawn_cards, player_hand, player_hand_value):
    
    original_deck = build_deck()
    deck_remaining = rebuild_deck(original_deck, drawn_cards)
    card_combinations, card_combinations_df, deck_dict = build_combinations(deck_remaining)

    player_draw = (random.choice(deck_remaining), )
    player_draw_rank = player_draw[0].split(' ')[0]
    player_draw_value = int(player_draw_rank) if player_draw_rank.isdigit() else 1 if player_draw_rank == 'A' else 10
    player_hand = player_hand + player_draw    
    player_hand_value =  int(str(player_hand_value + player_draw_value)[-1])

    return player_hand, player_hand_value, player_draw


def draw_banker(drawn_cards: list, banker_hand, banker_hand_value):
    
    original_deck = build_deck()
    deck_remaining = rebuild_deck(original_deck, drawn_cards)
    card_combinations, card_combinations_df, deck_dict = build_combinations(deck_remaining)

    banker_draw = (random.choice(deck_remaining), )
    banker_draw_rank = banker_draw[0].split(' ')[0]
    banker_draw_value = int(banker_draw_rank) if banker_draw_rank.isdigit() else 1 if banker_draw_rank == 'A' else 10
    banker_hand = banker_hand + banker_draw    
    banker_hand_value = int(str(banker_hand_value + banker_draw_value)[-1])

    return banker_hand, banker_hand_value, banker_draw


def announce_winner(player_hand_value, banker_hand_value):
    winner = str()

    if player_hand_value > banker_hand_value:
        winner = 'Player'

    elif player_hand_value < banker_hand_value:
        winner = 'Banker'

    else:
        winner = 'Tie'

    return winner


def announce_bet_winner(player_bet, winner):
    if player_bet == 'Banker' and winner == 'Banker':
        return 'Player bet on banker wins!'
    
    elif player_bet == 'Banker' and winner != 'Banker':
        return 'Player bet on banker losses!'

    elif player_bet == 'Player' and winner == 'Player':
        return 'Player bet on player wins!'

    elif player_bet == 'Player' and winner != 'Player':
        return 'Player bet on player losses!'

    elif player_bet == 'Tie' and winner == 'Tie':
        return 'Player bet on tie wins!'

    else:
        return 'Player bet on tie losses!'


def compute_payout(winner, wager, bet):
    if winner == 'Player':
        if bet == 'Player':
            payout = wager * 1
        else:
            payout = -wager

    elif winner == 'Banker':
        if bet == 'Banker':
            payout = wager * .95
        else:
            payout = -wager

    elif winner == 'Tie':
        if bet == 'Tie':
            payout = wager * 8
        else:
            payout = -wager

    return payout


def dataclass_to_dict(obj):
    return {k: (v if not isinstance(v, list) else list(v)) for k, v in vars(obj).items()}


# Function Wrapper
def play_game(type = 'normal') -> GameResult:

    # 1. Draw Player Cards
    player_hand, player_hand_value = draw_player_hand()
    drawn_cards = player_hand
    
    # 2. Draw Banker Cards
    if type == 'normal':
        banker_hand, banker_hand_value = draw_banker_hand(player_hand, 'No')
        drawn_cards += tuple(banker_hand)
    
    elif type == 'rigged':
        banker_hand, banker_hand_value = draw_banker_hand(player_hand, with_weights='Yes')
        drawn_cards += tuple(banker_hand)

    # 3. Decision logic for drawing additional card (Player)
    if player_hand_value <= 5:
        
        player_hand, player_hand_value, player_draw = draw_player(drawn_cards, player_hand, player_hand_value)
        drawn_cards += tuple(player_draw)
        last_action = 'player_draw'

    else:
        last_action = 'initial_deal'

    # 3. Decision logic for drawing additional card (Banker)
    if banker_hand_value <= 5:
        
        banker_hand, banker_hand_value, banker_draw = draw_banker(drawn_cards, banker_hand, banker_hand_value)
        drawn_cards += tuple(banker_draw)
        last_action = 'banker_draw'

    else:
        last_action = 'initial_deal'

    
    return GameResult(player_hand, player_hand_value, banker_hand, banker_hand_value, last_action)