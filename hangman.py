from Game import Game


def main_menu():
    exit_game = False

    while not exit_game:
        opt = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        if opt == "play":
            Game.start_game()
        elif opt == "results":
            Game.show_results()
        elif opt == "exit":
            exit_game = True


def main():
    print("H A N G M A N")
    main_menu()


main()
