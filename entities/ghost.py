class Ghost:

    def __init__(self, x: int, y: int) -> None:
        self.__position = (x,y)

    @property
    def position(self):
        return self.__position
