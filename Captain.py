from __future__ import annotations
from Character import Character
from Player import Player
import logging

from Player import Player
from Position import Position
logger = logging.getLogger()
class Captain(Character):
    player: Player 

    def __init__(self, player):
        super().__init__(player)
        self.position = Position.CAPTAIN

    def hability(self, target: Player):
        if not self.canUseHability():
            raise PermissionError('Não é possível executar essa ação agora')
        target.stealed_by_captain(self.player)
        self.steal(target)
    
    def canUseHability(self) -> bool:
        return True
    
    def counter(self, target: Captain):
        pass

    def steal(self, target: Player):
        self.player.coins += 2
        logger.info(f'O capitão {self.player.name} roubou 2 moedas do {target.name}')
