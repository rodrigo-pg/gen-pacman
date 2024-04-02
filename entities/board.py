from entities.action import Action
from entities.ghost import Ghost
from entities.pacman import Pacman

class Board:
    __state = []
    __ghosts: list[Ghost] = []

    def __init__(self, size: int):
        self.__size = size
        self.__state = [["x" for _ in range(self.__size)] for _ in range(self.__size)]
        self._create_ghosts()

    def set_state(self, x: int, y: int, state: str):
        self.__state[x][y] = state

    def get_state(self, x: int, y: int):
        return self.__state[x][y]

    def _create_ghosts(self):
        self.__ghosts.append(Ghost(1, 1))
        self.__ghosts.append(Ghost(1, self.__size - 2))
        self.__ghosts.append(Ghost(self.__size - 2, 1))
        self.__ghosts.append(Ghost(self.__size - 2, self.__size - 2)) 
        for ghost in self.__ghosts:
            (x, y) = ghost.position
            self.__state[x][y] = "G"

    def show(self):
        for i in range(len(self.__state)):
            print(self.__state[i])