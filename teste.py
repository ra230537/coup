from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Character(ABC):
    coins: int
    @abstractmethod
    def hability(self) -> str:
        raise NotImplemented
    
class Assassin(Character):

    def __init__(self, coins):
        self.coins = coins
    
    def hability(self):
        self.coins -= 3
        return (f'Assassino está gastando 3 moedas, restando {self.coins} moedas')
    
class Duke(Character):

    def __init__(self, coins):
        self.coins = coins
    
    def hability(self):
        self.coins += 3
        return (f'Duque está usando seu poder, ficando com {self.coins} moedas')

def useHability(characters: List[Character]):
    actions = []
    for character in characters:
        actions.append(character.hability())
    return actions

