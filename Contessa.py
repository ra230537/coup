from Assassin import Assassin
from Character import Character
from Position import Position


class Contessa(Character):

    def __init__(self, player):
        super().__init__(player)
        self.position = Position.CONTESSA

    def hability(self, target: Assassin):
        if not self.canUseHability():
            raise PermissionError('Não é possível executar essa ação agora')
        self.coins += 3
        return (f'Duque está usando seu poder, ficando com {self.coins} moedas')
    
    def canUseHability(self) -> bool:
        return True
    
    def counter(self, target: Assassin):
        # Dar algum sinal que foi counterado
        pass