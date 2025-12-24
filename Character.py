from __future__ import annotations
from abc import ABC, abstractmethod
from Actions import ActionType
from Position import Position
from Player import Player
from State import States
import uuid
import logging

logger = logging.getLogger()
class Character(ABC):
    identity: str
    state: States
    player: Player
    position: Position

    def __init__(self, player: Player):
        self.player = player
        self.identity = str(uuid.uuid4())
        self.state = States.IN_DECK
        if self not in player.cards:
            player.cards.append(self)

    @abstractmethod
    def hability(self) -> str:
        raise NotImplemented
    
    @abstractmethod
    def canUseHability(self) -> bool:
        raise NotImplemented
    
    def income(self) -> None:
        self.player.coins += 1
        logger.info(f'O jogador {self.player.name} está recebendo 1 moeda, ficando com {self.player.coins} moedas')
    
    def foreign_aid(self) -> None:
        self.player.coins += 2
        logger.info(f'O jogador {self.player.name} está recebendo 2 moedas, ficando com {self.player.coins} moedas')
    
    def coup(self, target: Player) -> None:
        if not self.can_coup():
            raise PermissionError('O jogador não tem moedas o suficiente para executar o golpe de estado')
        self.player.coins -= 7
        deposed_card = target.deposed()
        logger.info(f'O jogador {self.player.name} deu um golpe de estado em {target.name}, eliminado um {deposed_card.position}, restando {self.player.coins} moedas')
    
    def can_coup(self):
        return self.player.coins >= 7

    @abstractmethod
    def counter(self, target: Character) -> None:
        raise NotImplemented

    def action(self, action_type: ActionType) -> None:
        if self.player.coins >= 10:
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
    