from entities.action import Action
from entities.pacman import Pacman

class MoveRight(Action):

    def act(self, pm: Pacman) -> Pacman:
        pm.right()
        return pm