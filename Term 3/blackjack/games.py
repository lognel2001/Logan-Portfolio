import cards
def ask_number(question, low, high):
    """ Ask for a number within a range."""
    response = None
    while True:
        try:
            response = int(input(question))
            if response in range(low, high):
                return response
            else:
                print("That's out of range")
        except:
            print("That's not a number")

def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question.lower())
    return response


def shuffle(self):
    
    """ this will shuffle your cards"""
    import random
    random.shuffle(self.cards)

def deal(self, hands, per_hand = 1):
    """ this will deal out cards to every players hands until they have a
         certain amount or the deck runs out of cards"""
    for rounds in range(per_hand):
        for hand in hands:
            if self.cards:
                top_card = self.cards[0]
                self.give(top_card, hand)
            else:
                print("Can't continue to deal. Out of cards!")

def switch_turn(num_players,turn):
    """ this will switch turns between the players"""
    turn += 1
    if turn == num_players:
        turn = 0
    return turn


class Player(object):
    
    """A player for a game"""
    def __init__(self, name,score):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name
        rep = rep +" "+str(score)
        return rep

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
