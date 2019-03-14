

class Card(object):
    
    """ A playing card.
    this class will build a single card
    to build a card call Card() and pass in a rank and a suit
    card1 = Card(rank = "A",suit = "s")
    """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♠", "♡", "♣", "♢"]

    def __init__(self,rank,suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self): 
        if self.is_face_up:
            rep = self.rank +self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up= not self.is_face_up
        

##card = Card(rank = random.choice(Card.RANKS),suit = random.choice(Card.SUITS))
##card2 = Card(rank = random.choice(Card.RANKS),suit = random.choice(Card.SUITS))
##card3 = Card(rank = random.choice(Card.RANKS),suit = random.choice(Card.SUITS))
##card4 = Card(rank = random.choice(Card.RANKS),suit = random.choice(Card.SUITS))
##card5 = Card(rank = random.choice(Card.RANKS),suit = random.choice(Card.SUITS))
##print(card,card2,card3,card4,card5)

class Hand(object):
    """ A hand of playing cards.
        This class will create hands for you and another player.
        You can also clear, add, or give cards.
        to use it call Hand() as my_hand = Hand()
    """
    def __init__(self):
        self.cards=[]

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep +=str(card) + " "
        else:
            rep = "<empty>"
        return rep
    
    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

##my_hand = Hand()
##
##your_hand = Hand()
##deck=[]
##for i in range (10):
##    card = Card(rank = random.choice(Card.RANKS),suit=random.choice(Card.SUITS))
##    deck.append(card)
##
##for i in range(5):
##    my_hand.add(deck.pop())
##    your_hand.add(deck.pop())
##print(my_hand)
##print(your_hand)
##
##my_hand.give(my_hand.cards[0],your_hand)

class Deck(Hand):
    """This class will populate the hand of the player(s)
        it will shuffle the deck so that the cards are in a
        random order, and it will deal the top card to the player
        as long as their are still cards left.
    """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))


    def shuffle(self):
        import random
        random.shuffle(self.cards)
        
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue to deal. Out of cards!")

##class Unprintable_Card(Card):
##    """ A Card that won't reveal its rank or suit when printed."""
##    def __str__(self):
##        return "<unprintable>"
        




if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")









