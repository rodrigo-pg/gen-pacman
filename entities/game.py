from enum import Enum
from entities.action import Action
from entities.board import Board
from entities.pacman import Pacman

class GameStatus(Enum):
    WINNER = 1
    GAME_OVER = 2
    PLAYING = 3

class Game:
    __player: Pacman = None
    __board: Board = None
    __score = 0
    __status = GameStatus.PLAYING

    def __init__(self):
        self.__player = Pacman(0, 0, 10)
        self.__board = Board(10)
        self.__board.set_state(0, 0, "ᗣ")

    @property
    def score(self):
        return self.__score
    
    def simulate(self, actions: list[Action]) -> tuple[int, int, int]:
        steps_til_die = 0
        for action in actions:
            steps_til_die += 1
            self.play(action)
            if self.is_over(): return (steps_til_die, self.__score, 0)
        return (steps_til_die, self.__score, self.__score)

    def is_won(self):
        return self.__status == GameStatus.WINNER

    def is_over(self):
        return self.__status == GameStatus.GAME_OVER

    def play(self, action: Action):
        (before_x, before_y) = self.__player.position
        player_after_play = action.act(self.__player)
        future_house_state = self.__board.get_state(player_after_play.position[0], player_after_play.position[1])
        if future_house_state == "x":
            self.__score += 20
        elif future_house_state == "G":
            self.__status = GameStatus.GAME_OVER
            return
        self.__board.set_state(before_x, before_y, "")
        self.__board.set_state(player_after_play.position[0], player_after_play.position[1], "ᗣ")

    def show(self):
        print("score: " + str(self.__score))
        self.__board.show()