from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class Console(str, Enum):
    NES = "NES"
    SNES = "Super Nintendo"
    GENESIS = "Mega Drive/Genesis"
    ATARI_2600 = "Atari 2600"
    GAME_BOY = "Game Boy"
    ARCADE = "Arcade"
    PSX = "PlayStation"
    N64 = "Nintendo 64"

class Genre(str, Enum):
    PLATFORM = "Plataforma"
    RPG = "RPG"
    FIGHTING = "Luta"
    RACING = "Corrida"
    PUZZLE = "Puzzle"
    SHOOTER = "Tiro"
    ADVENTURE = "Aventura"
    SPORTS = "Esportes"

class Game(BaseModel):
    id: Optional[int] = None
    titulo: str
    console: Console
    ano: int
    genero: Genre
    desenvolvedor: str
    descricao: Optional[str] = None
    favorito: bool = False
    nota: Optional[float] = None

class GameUpdate(BaseModel):
    titulo: Optional[str] = None
    console: Optional[Console] = None
    ano: Optional[int] = None
    genero: Optional[Genre] = None
    desenvolvedor: Optional[str] = None
    descricao: Optional[str] = None
    favorito: Optional[bool] = None
    nota: Optional[float] = None