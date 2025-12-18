from fastapi import FastAPI
from teste import useHability, Assassin, Duke
app = FastAPI()


@app.get("/")
async def root():
    assassin = Assassin(5)
    duke = Duke(5)
    return useHability([assassin, duke])