# 🎮 Retro Games Collection

Sistema de catálogo de jogos retro com API REST e interface web.

## 🚀 Tecnologias

- **Python 3.8+**
- **FastAPI** - API REST moderna
- **Poetry** - Gerenciamento de dependências
- **Pydantic** - Validação de dados
- **Jinja2** - Templates HTML

## 📦 Instalação

```bash
# Instalar dependências
poetry install

# Ou com pip
pip install fastapi uvicorn jinja2 python-multipart
```

## 🎯 Execução

```bash
# Com Poetry
poetry run python main.py

# Ou diretamente
python main.py
```

## 🌐 Acesso

- **Interface Web**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🎮 Funcionalidades

### Interface Web
- ✅ Catálogo visual de jogos retro
- ✅ Adicionar/editar/remover jogos
- ✅ Filtros por console e gênero
- ✅ Sistema de favoritos
- ✅ Avaliações com notas
- ✅ Design temático retro

### API REST
- `GET /games` - Listar jogos (com filtros)
- `POST /games` - Adicionar jogo
- `GET /games/{id}` - Buscar jogo
- `PUT /games/{id}` - Atualizar jogo
- `DELETE /games/{id}` - Remover jogo
- `GET /consoles` - Listar consoles
- `GET /genres` - Listar gêneros

## 🎯 Consoles Suportados

- NES
- Super Nintendo
- Mega Drive/Genesis
- Atari 2600
- Game Boy
- Arcade
- PlayStation
- Nintendo 64

## 🎨 Gêneros

- Plataforma
- RPG
- Luta
- Corrida
- Puzzle
- Tiro
- Aventura
- Esportes

## 📊 Dados Iniciais

O sistema vem com jogos clássicos pré-cadastrados:
- Super Mario Bros. (NES, 1985)
- The Legend of Zelda (NES, 1986)
- Street Fighter II (SNES, 1991)
- Sonic the Hedgehog (Genesis, 1991)