from Character import Character
import logging

from Position import Position

logger = logging.getlogger()

class Duke(Character):

    def __init__(self, player):
        super().__init__(player)
        self.position = Position.DUKE

    def hability(self):
        if not self.canUseHability():
            raise PermissionError('Não é possível executar essa ação agora')
        self.player.coins += 3
        return (f'Duque está usando seu poder, ficando com {self.coins} moedas')
    
    def canUseHability(self) -> bool:
        return True
    
    def counter(self):
        pass