from Character import Character


class Duke(Character):

    def hability(self):
        if not self.canUseHability():
            raise PermissionError('Não é possível executar essa ação agora')
        self.coins += 3
        return (f'Duque está usando seu poder, ficando com {self.coins} moedas')
    
    def canUseHability(self) -> bool:
        return True
    
    def counter(self):
        pass