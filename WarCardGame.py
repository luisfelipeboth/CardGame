import random

suits = ["Hearts","Clubs","Diamonds","Spades"]
ranks = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

class Card:
    # Definition of a card, each card has a rank, suit and value associated
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}!"
    
class Deck:
    # Definition of a deck of cards, a list containing all the cards objects
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def __str__(self):
        return f"The deck contain {len(self.all_cards)} cards!"
    
    # Things you can do with a deck:
    def shuffle(self):
        # Shuffle the hole deck
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Remove one card at a time from the deck
        return self.all_cards.pop()

class Player:
    # Definition of a player deck, each player have a name and a deck(list) of cards
    def __init__(self, name):
        self.name = name
        self.player_deck = []
        
    def __str__(self):
        return f"The player {self.name} has {len(self.player_deck)} cards!"

    # Things a player can do with his deck
    def add_cards(self,new_cards):
        # Add one or multiple cards to his deck
        if type(new_cards) == type([]):
            # Add multiple cards (a list of new cards)
            self.player_deck.extend(new_cards)
        else:
            self.player_deck.append(new_cards)

    def remove_one(self):
        # Remove one card of his deck
        return self.player_deck.pop(0)     # Remove allways the top card of the deck


def main():
    # Setup for the game:
        # Create deck
        # Shuffle deck
        # Create players
        # Create players deck

    # Actual gameplay:
        # Check size of players deck
        # Remove a card of each player decks (put the card in the table)
        # Check for war (first iteration, consider war is on)
            # Check player one card > player two card
                # Add cards to player one deck
                # Set war to false
            # Check player two card > player one card
                # Add cards to player two deck
                # Set war to false
            # Check player one card == player two card
                # Check if both players can draw more cards (if players deck is bigger than the amount of cards to be drawn in war situation)
                # Draw cards for each player and repeat the War loop

    deck = Deck()                                       # Create the deck
    deck.shuffle()                                      # Shuffle the deck
    player_one = Player("Luis")                         # Create player one
    player_two = Player("Felipe")                       # Create player two

    for i in range(int(len(deck.all_cards)/2)):              # Fill players deck
        # Iterates separing the deck in half
        player_one.add_cards(deck.deal_one())
        player_two.add_cards(deck.deal_one())


    game_on = True                                      # Condition to finish the game
    round_num = 0                                       # Counter of rounds

    while game_on:
        at_war = True                                   # Set war situation as occurring
        round_num += 1
        print(f"Round {round_num}!")

        if len(player_one.player_deck) == 0:
            # Check if player one have cards to play
            print(f"Player {player_one.name} out of cards.")
            print(f"Player {player_two.name} is the winner!")
            game_on = False
            break

        if len(player_two.player_deck) == 0:
            # Chack if player two have cards to play
            print(f"Player {player_two.name} out of cards.")
            print(f"Player {player_one.name} is the winner!")
            game_on = False
            break

        player_one_tabble_cards = []
        player_one_tabble_cards.append(player_one.remove_one())        # Add a card to list of cards in the table of player one
        player_two_tabble_cards = []
        player_two_tabble_cards.append(player_two.remove_one())        # Add a card to list of cards in the table of player two

        while at_war:
            if player_one_tabble_cards[-1].value > player_two_tabble_cards[-1].value:
                # Player one won the battle and gets both cards
                player_one.add_cards(player_one_tabble_cards)          # Add back the tabble cards to player one deck
                player_one.add_cards(player_two_tabble_cards)          # Add player two tabble cards to player one deck
                at_war = False                                         # Set the game to not be at war situation
            elif player_two_tabble_cards[-1].value > player_one_tabble_cards[-1].value:
                # Player two won the battle and gets both cards
                player_two.add_cards(player_two_tabble_cards)          # Add back the tabble cards to player two deck
                player_two.add_cards(player_one_tabble_cards)          # Add player one tabble cards to player two deck
                at_war = False                                         # Set the game to not be at war situation
            else:
                # War situation, draw more cards
                print("WAR!")
                if len(player_one.player_deck) < 5:
                    # Player one unable to draw more cards, lost the game
                    print(f"Player {player_one.name} unabble to play war. Game Over at war!")
                    print(f"Player {player_two.name} Wins!")
                    game_on = False
                    break

                elif len(player_two.player_deck) < 5:
                    # Player two unable to draw more cards, lost the game
                    print(f"Player {player_two.name} unabble to play war. Game Over at war!")
                    print(f"Player {player_one.name} Wins!")
                    game_on = False
                    break

                else:
                    # Still war condition, draw more cards
                    for i in range(5):
                        player_one_tabble_cards.append(player_one.remove_one())
                        player_two_tabble_cards.append(player_two.remove_one())

if __name__ == "__main__":
    main()