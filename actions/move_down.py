from entities.action import Action
from entities.pacman import Pacman

class MoveDown(Action):

    def act(self, pm: Pacman) -> Pacman:
        pm.down()
        return pm