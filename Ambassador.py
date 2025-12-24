from __future__ import annotations
import logging

from Captain import Captain
from Position import Position
from Character import Character

logger = logging.getLogger()
class Ambassador(Character):

    def __init__(self, player):
        super().__init__(player)
        self.position = Position.AMBASSADOR

    def hability(self):
        if not self.canUseHability():
            raise PermissionError('Não é possível executar essa ação agora')
        self.coins += 3
        return (f'Duque está usando seu poder, ficando com {self.coins} moedas')
    
    def canUseHability(self) -> bool:
        return True
    
    def counter(self, target: Captain):
        # Impede a habilidade do capitão
        pass