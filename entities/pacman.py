class Pacman:

    def __init__(self, x: int, y: int, board_size: int) -> None:
        self.__position = (x,y)
        self.__board_size = board_size

    @property
    def position(self):
        return self.__position

    def up(self):
        if self.__position[0] - 1 >= 0:
            self.__position = (self.__position[0] - 1, self.__position[1])

    def down(self):
        if self.__position[0] + 1 < self.__board_size:
            self.__position = (self.__position[0] + 1, self.__position[1])

    def left(self):
        if self.__position[1] - 1 >= 0:
            self.__position = (self.__position[0], self.__position[1] - 1)

    def right(self):
        if self.__position[1] + 1 < self.__board_size:
            self.__position = (self.__position[0], self.__position[1] + 1)