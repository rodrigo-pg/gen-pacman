from entities.action import Action
from entities.pacman import Pacman

class MoveUp(Action):

    def act(self, pm: Pacman) -> Pacman:
        pm.up()
        return pm