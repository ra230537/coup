from __future__ import annotations
from Character import Character
import logging

logger = logging.getLogger()

class Assassin(Character):
    
    def hability(self, target: Character) -> None:
        self.coins -= 3
        return (f'Assassino está gastando 3 moedas, restando {self.coins} moedas')
    
    def canUseHability(self) -> bool:
        return self.coins >= 3
    
    def counter(self, target):
        pass