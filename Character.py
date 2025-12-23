from __future__ import annotations
from abc import ABC, abstractmethod
from Actions import ActionType
from Player import Player
from State import States
import uuid
import logging

logger = logging.getLogger()
class Character(ABC):
    identity: str = uuid.uuid4()
    state: States = States.IN_DECK
    player: Player

    def __init__(self, player: Player):
        self.player = player

    @abstractmethod
    def hability(self) -> str:
        raise NotImplemented
    
    @abstractmethod
    def canUseHability(self) -> bool:
        raise NotImplemented
    
    def income(self) -> None:
        self.coins += 1
        return (f'Personagem está recebendo 1 moeda, ficando com {self.coins} moedas')
    
    def foreign_aid(self) -> None:
        self.coins += 2
        return (f'Personagem está recebendo 2 moedas, ficando com {self.coins} moedas')
    
    def coup(self) -> None:
        self.coins -= 7
        return (f'Personagem está gastando 7 moedas, restando {self.coins} moedas')

    @abstractmethod
    def counter(self, target: Character) -> None:
        raise NotImplemented

    def action(self, action_type: ActionType) -> None:
        if self.coins >= 10:
            self.coup()
        match action_type:
            case ActionType.INCOME:
                self.income()
            case ActionType.FOREIGN_AID:
                self.foreign_aid()
            case ActionType.COUP:
                self.coup()
            case ActionType.HABILITY:
                self.hability()
            case ActionType.COUNTER:
                self.coutner()
            case _:
                raise ValueError("Ação inválida") 
    