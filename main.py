from fastapi import FastAPI
import logging

from Assassin import Assassin
from Captain import Captain
from Contessa import Contessa
from Duke import Duke
from Player import Player

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
app = FastAPI()


@app.get("/")
async def root():
    player1 = Player(name='joão')
    player2 = Player(name='john')
    assassin = Assassin(player1)
    duke = Duke(player1)
    captain = Captain(player2)
    contessa = Contessa(player2)
    # precisamos acessar o campitão através do seu jogador e não diretamente
    captain.hability(player1)