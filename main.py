from actions.move_down import MoveDown
from actions.move_left import MoveLeft
from actions.move_right import MoveRight
from actions.move_up import MoveUp
from entities.board import Board
from entities.game import Game

map = {
    "w": MoveUp,
    "s": MoveDown,
    "a": MoveLeft,
    "d": MoveRight
}

game = Game()

while True:
    game.show()
    command = input()
    print("\033[H\033[2J", end='')
    Action = map.get(command)
    if Action is not None:
        game.play(Action())
    if game.is_over():
        print("\033[H\033[2J", end='')
        print("GAME OVER\n")
        break