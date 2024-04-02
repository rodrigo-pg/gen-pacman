from entities.action import Action
from entities.pacman import Pacman

class MoveLeft(Action):

    def act(self, pm: Pacman) -> Pacman:
        pm.left()
        return pm