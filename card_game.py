import random 

class Suit:
 
    SYMBOLS = {"clubs": '♣', "diamonds": '♦', "hearts": "♥", "spades": "♠"}    
    DESCRIPTION_ALLOWED = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self, description):
        if description.lower() in Suit.DESCRIPTION_ALLOWED:
            self._description = description            
            self._symbol = Suit.SYMBOLS[description.lower()]
        else:
            print('we have unrecognized description')
        
    
    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol

class Card:
    
    SPECIAL_CARD = {11:"Jack", 12:"Queen", 13:"King", 14:"Ace"}
    
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value
        
    @property
    def suit(self):
        return self._suit
    
    @property
    def value(self):
        return self._value
    
    def is_special(self):
        return self._value > 10
    
    def show(self):
        card_value = self._value
        if self.is_special():
            print(card_value)
            card_description = Card.SPECIAL_CARD[card_value]
        else:
            card_description = card_value
        card_suit = self._suit.description.capitalize()
        suit_symbol = self._suit.symbol
        
        print(f"{card_description} of {card_suit} {suit_symbol}")
        return card_value, card_description, card_suit, suit_symbol
    

class Deck:
    
    SUITS = ("clubs", "diamonds", "hearts", "spades")
    
    def __init__(self, is_empty=False):
        self._cards = []
        
        if not is_empty:
            self.build()
    
    @property
    def size(self):
        return len(self._cards)
    
    def build(self):
        for suit in Deck.SUITS:
            for value in range(2,15):
                self._cards.append(Card( Suit(suit), value))
    
    def show(self):
        for card in self._cards:
            card.show()
    
    def shuffle(self):
        random.shuffle(self._cards)
    
    def draw(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None

    def add(self, card):
        self._cards.insert(0,card)


class Player:
    
    def __init__(self, name, deck, is_computer=False):
        if isinstance(name, str):
            self.name = name
        else:
            print('The name is not a string')
        self._deck = deck
        self._is_computer = is_computer
        
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def deck(self):
        return self._deck
    
    def has_empty_deck(self):
        return self._deck.size == 0
        
    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()#.show()
            
    def add_card(self,card):
        self._deck.add(card)

