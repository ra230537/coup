from __future__ import annotations
from typing import List, TYPE_CHECKING
import uuid
import logging

if TYPE_CHECKING:
    from Character import Character

logger = logging.getLogger()

'''
Precisa ter a classe player
O player tem 0 a 2 cartas, identidade, moeda e nome
'''

class Player:
    cards: List['Character'] = []
    identity: str = uuid.uuid4()
    coins: int = 2
    name: str = ''
    def __init__(self, name):
        self.name = name
    
    def stealed_by_captain(self, captain: Player) -> None:
        self.coins -= 2
        logger.info(f'O jogador {self.name} foi roubado em 2 moedas pelo capitão {captain.name}')

    