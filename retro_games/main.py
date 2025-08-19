from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Optional
import uvicorn
import logging
from datetime import datetime

from .models import Game, GameUpdate, Console, Genre

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('retro_games.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("retro_games")

app = FastAPI(title="Retro Games API", version="1.0.0", description="Sistema de Catálogo de Jogos Retro")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Banco de dados em memória com dados iniciais
games_db = []
next_id = 1

# Inicializar dados
def init_data():
    global next_id
    if not games_db:  # Só inicializa se estiver vazio
        initial_games = [
            Game(titulo="Super Mario Bros.", console=Console.NES, ano=1985, genero=Genre.PLATFORM, desenvolvedor="Nintendo", descricao="O clássico jogo de plataforma que definiu o gênero"),
            Game(titulo="The Legend of Zelda", console=Console.NES, ano=1986, genero=Genre.ADVENTURE, desenvolvedor="Nintendo", descricao="Aventura épica em Hyrule"),
            Game(titulo="Street Fighter II", console=Console.SNES, ano=1991, genero=Genre.FIGHTING, desenvolvedor="Capcom", descricao="O rei dos jogos de luta"),
            Game(titulo="Sonic the Hedgehog", console=Console.GENESIS, ano=1991, genero=Genre.PLATFORM, desenvolvedor="Sega", descricao="O ouriço azul mais rápido do mundo"),
        ]
        
        for game in initial_games:
            game.id = next_id
            games_db.append(game)
            next_id += 1

# Inicializar dados na importação
init_data()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/games", response_model=List[Game])
def get_games(
    console: Optional[Console] = None,
    genero: Optional[Genre] = None,
    favoritos: Optional[bool] = None
):
    logger.info(f"Buscando jogos - Console: {console}, Gênero: {genero}, Favoritos: {favoritos}")
    filtered_games = games_db
    
    if console:
        filtered_games = [g for g in filtered_games if g.console == console]
    if genero:
        filtered_games = [g for g in filtered_games if g.genero == genero]
    if favoritos is not None:
        filtered_games = [g for g in filtered_games if g.favorito == favoritos]
    
    logger.info(f"Retornando {len(filtered_games)} jogos")
    return filtered_games

@app.get("/games/{game_id}", response_model=Game)
def get_game(game_id: int):
    game = next((g for g in games_db if g.id == game_id), None)
    if not game:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return game

@app.post("/games", response_model=Game)
def create_game(game: Game):
    global next_id
    game.id = next_id
    next_id += 1
    games_db.append(game)
    logger.info(f"Jogo criado: {game.titulo} (ID: {game.id})")
    return game

@app.put("/games/{game_id}", response_model=Game)
def update_game(game_id: int, game_update: GameUpdate):
    game = next((g for g in games_db if g.id == game_id), None)
    if not game:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    
    update_data = game_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(game, field, value)
    
    return game

@app.delete("/games/{game_id}")
def delete_game(game_id: int):
    global games_db
    game = next((g for g in games_db if g.id == game_id), None)
    if not game:
        logger.warning(f"Tentativa de deletar jogo inexistente: {game_id}")
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    
    games_db = [g for g in games_db if g.id != game_id]
    logger.info(f"Jogo deletado: {game.titulo} (ID: {game_id})")
    return {"message": "Jogo removido com sucesso"}

@app.get("/consoles")
def get_consoles():
    return [{"value": console.value, "name": console.value} for console in Console]

@app.get("/genres")
def get_genres():
    return [{"value": genre.value, "name": genre.value} for genre in Genre]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)