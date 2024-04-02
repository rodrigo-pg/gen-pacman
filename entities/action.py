from abc import ABC, abstractmethod
from entities.pacman import Pacman

class Action(ABC):
    
    @abstractmethod
    def act(self, pm: Pacman) -> Pacman:
        return pm