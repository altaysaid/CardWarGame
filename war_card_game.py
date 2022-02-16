class WarCardGame:
    
    PLAYER = 0
    COMPUTER = 1
    TIE = 2 
    
    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck
        
        self.make_initial_decks()
        
    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)
        
    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)
    
    def start_battle(self, cards_from_war=None):
        print("\n == Let's start the Battle ==\n")
        
        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()
        
        print("Your Card:")
        player_card.show()
        
        print("\n Computer Card:")
        computer_card.show()
        
        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("\n You won this round!")
            self.add_cards_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\n The computer won this round! :(")
            self.add_cards_to_character(self._computer, cards_won)
        elif winner == WarCardGame.TIE:
            print("\n It's a tie. This is war!!")
            self.start_war(cards_won)
        
        return winner

    def get_round_winner(self, player_card, computer_card):
        if player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        elif player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        else:
            return WarCardGame.TIE
        
    def get_cards_won(self, player_card, computer_card, previous_cards):
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]
        
    def add_cards_to_character(self, character, cards_won):
        for card in cards_won:
            character.add_card(card)
            
    def start_war(self, previous_cards):
        player_cards = []
        computer_cards = []
        
        min_cards = 4
        if self._player.deck.size < 4:
            min_cards = self._player.deck.size
        if self._computer.deck.size < 4:
            if self._computer.deck.size < self._player.deck.size:
                min_cards = self._computer.deck.size
        
        for i in range(min_cards-1):
            player_card = self._player.draw_card()
            computer_card = self._computer.draw_card()
            
            player_cards.append(player_card)
            computer_cards.append(computer_card)
            # previous_cards += [player_card, computer_card]
            
        print(f"{len(player_cards + computer_cards + previous_cards)} hidden cards: XXX XXX")
        self.start_battle(player_cards + computer_cards + previous_cards)
        
    def check_game_over(self):
        if self._player.has_empty_deck():
            print("===========The computer wan============")
            print("===========   GAME OVER   ============")
            print("===========   Try Again !   ============")
            return True
        if self._computer.has_empty_deck():
            print("=======================================")
            print("===========   GAME OVER   ============")
            print(f"===========   You won !, {self._player.name}!! Congratulations   ============")
            return True
        else:
            return False
        
    def print_stats(self):
        print("\n-----")
        print(f"You have {self._player.deck.size} cards on your deck")
        print(f"The computer has {self._computer.deck.size} cards on its deck")
        print("-----")
    
    def print_welcome_message(self):
        
        print("===============================================")
        print("=================   Welcome   =================")
        print("===============================================")