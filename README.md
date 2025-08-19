# 🎮 Retro Games API

> API REST moderna para catálogo de jogos retro com sistema de avaliações e favoritos

## 📋 Descrição do Projeto

A **Retro Games API** é uma aplicação web desenvolvida em Python que permite gerenciar um catálogo completo de jogos clássicos. O sistema oferece funcionalidades para cadastrar, avaliar, favoritar e filtrar jogos de diferentes plataformas retro, desde Arcade até consoles como NES, SNES e PlayStation 1.

### Principais Características:
- 🎯 **CRUD Completo**: Criar, listar, atualizar e remover jogos
- 🔍 **Filtros Avançados**: Por plataforma, gênero e favoritos
- ⭐ **Sistema de Avaliação**: Notas de 0 a 10 para cada jogo
- 📊 **Estatísticas**: Relatórios detalhados do catálogo
- 🚀 **API REST**: Documentação automática com Swagger/OpenAPI
- ✅ **Validação**: Dados validados automaticamente com Pydantic

## 🛠️ Tecnologias Utilizadas

- **[Python 3.8+](https://python.org)** - Linguagem de programação
- **[FastAPI](https://fastapi.tiangolo.com)** - Framework web moderno e rápido
- **[Poetry](https://python-poetry.org)** - Gerenciador de dependências e build
- **[Pydantic](https://pydantic.dev)** - Validação de dados com type hints
- **[Uvicorn](https://uvicorn.org)** - Servidor ASGI de alta performance
- **[Requests](https://requests.readthedocs.io)** - Cliente HTTP para testes


### Instalando o Poetry

```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# Linux/macOS
curl -sSL https://install.python-poetry.org | python3 -

# Ou via pip
pip install poetry
```

## 🚀 Instalação e Configuração

### 1. Clone o Repositório
```bash
git clone https://github.com/Joao07912/Projeto
cd retro-games-api
```

### 2. Instale as Dependências
```bash
# Instalar todas as dependências do projeto
poetry install

# Ou usando pip (alternativa)
pip install -r requirements.txt
```

### 3. Ative o Ambiente Virtual (Poetry)
```bash
poetry shell
```

## ▶️ Execução

### Método 1: Script Automatizado (Recomendado)
```bash
# Windows
run_simple.bat

# Ou manualmente
python build.py
```

### Método 2: Poetry
```bash
# Iniciar servidor de desenvolvimento
poetry run uvicorn retro_games.main:app --reload

# Ou usando o script personalizado
poetry run start
```

### Método 3: Python Direto
```bash
# Após instalar dependências com pip
python -m uvicorn retro_games.main:app --reload
```

## 🌐 Acesso à Aplicação

Após iniciar o servidor, acesse:

- **🏠 API Base**: http://localhost:8000
- **📚 Documentação Interativa (Swagger)**: http://localhost:8000/docs
- **📖 Documentação Alternativa (ReDoc)**: http://localhost:8000/redoc

## 🔧 Build e Distribuição

### Build Automatizado
```bash
# Executa instalação, testes e build
python build.py
```

### Build Manual
```bash
# Gerar pacote distribuível
poetry build

# Arquivos gerados em: dist/
# - retro_games_api-1.0.0.tar.gz (código fonte)
# - retro_games_api-1.0.0-py3-none-any.whl (wheel)
```

## 🧪 Testes

### Executar Testes Automatizados
```bash
# Testar todos os endpoints
python test_api.py

# Com Poetry
poetry run python test_api.py
```

### Teste Manual via Swagger
1. Acesse http://localhost:8000/docs
2. Explore e teste os endpoints interativamente

## 📡 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|----------|
| `GET` | `/` | Informações gerais e estatísticas |
| `POST` | `/games/` | Adicionar novo jogo |
| `GET` | `/games/` | Listar jogos (com filtros) |
| `GET` | `/games/{id}` | Obter jogo específico |
| `PUT` | `/games/{id}` | Atualizar/avaliar jogo |
| `DELETE` | `/games/{id}` | Remover jogo |
| `GET` | `/stats` | Estatísticas detalhadas |

### Filtros Disponíveis
- `?platform=Arcade` - Filtrar por plataforma
- `?genre=Ação` - Filtrar por gênero
- `?favorites_only=true` - Apenas favoritos

## 🎮 Plataformas e Gêneros

### Plataformas Suportadas
- Arcade
- Nintendo (NES)
- Super Nintendo (SNES)
- Sega Genesis
- Atari 2600
- Game Boy
- PlayStation 1

### Gêneros Disponíveis
- Ação
- Aventura
- RPG
- Plataforma
- Puzzle
- Corrida
- Luta
- Tiro

## 📊 Exemplo de Uso

```python
import requests

# Adicionar novo jogo
game_data = {
    "title": "Street Fighter II",
    "platform": "Arcade",
    "genre": "Luta",
    "year": 1991,
    "description": "Clássico jogo de luta da Capcom"
}

response = requests.post("http://localhost:8000/games/", json=game_data)
print(response.json())
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

### 🔧 Resolução de Conflitos

Este projeto já passou por situações de conflito de merge que foram resolvidas com sucesso:

**Conflito Resolvido**: Configuração do servidor
- **Situação**: Dois desenvolvedores alteraram a mesma linha de configuração do uvicorn
- **Resolução**: Combinamos as melhores práticas de ambas as alterações
- **Resultado**: Servidor configurado com host local, reload ativo e debug habilitado

**Como resolver conflitos**:
```bash
git checkout main
git pull origin main
git checkout sua-branch
git merge main
# Resolver conflitos manualmente
git add .
git commit -m "resolve: descrição do conflito resolvido"
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

