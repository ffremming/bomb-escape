import random

from board import Board


DIRECTIONS = {"o": "up", "n": "down", "h": "right", "v": "left"}


def main():
    board = Board(40, 15)
    direction = "up"

    while True:
        board.draw()
        choice = input("o/n/h/v to face, enter to move, g=grenade, b=bomb: ")

        if choice in DIRECTIONS:
            direction = DIRECTIONS[choice]
        elif choice == "g":
            board.throw_grenade(direction)
        elif choice == "b":
            board.bomb()
        elif choice == "":
            board.move_player(direction)

        if random.randint(0, 3) < 2:
            board.get_enemy().update()

        if board.get_enemy().get_position() == board.get_player().get_position():
            print("Caught! Game over.")
            break

        board.collect_coins()


if __name__ == "__main__":
    main()
