from __future__ import annotations
from Character import Character
import logging

from Player import Player
from Position import Position

logger = logging.getLogger()

class Assassin(Character):
    
    def __init__(self, player):
        super().__init__(player)
        self.position = Position.ASSASSIN

    def hability(self, target: Player) -> None:
        if not self.canUseHability():
            raise PermissionError('Não é possível executar essa ação agora')
        self.player.coins -= 3
        # Busca carta aleatória de uma pessoa
    
    def canUseHability(self) -> bool:
        return self.coins >= 3
    
    def counter(self, target):
        pass