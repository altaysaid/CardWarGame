from card_game import Deck, Player
from war_card_game import WarCardGame

player = Player("Altay", Deck(is_empty=True))

computer = Player("ComputerTroubleMaker", Deck(is_empty=True), is_computer=True)


deck = Deck()

game = WarCardGame(player, computer, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()
    
    # answer = input("\n Are you ready for the next round ?\n PRess Enter to Continue or X to stop")
    
    # if answer.lower() == "x":
    #     break