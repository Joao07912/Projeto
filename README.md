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

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8 ou superior** ([Download](https://python.org/downloads))
- **Poetry** (gerenciador de dependências)

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
git clone <url-do-repositorio>
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
executar.bat
```

### Opção 2: Comandos manuais
```bash
# Compilar
mvn compile

# Executar
mvn exec:java -Dexec.mainClass="Calculadora"

# Executar testes
mvn test
```

### Opção 3: Executar testes
```bash
executar-testes.bat
```

## 📚 O que você aprende:

1. **pom.xml** - Como configurar um projeto Maven
2. **Calculadora.java** - Como escrever código Java
3. **CalculadoraTest.java** - Como criar testes unitários
4. **mvn compile** - Como compilar com Maven
5. **mvn test** - Como executar testes
6. **mvn exec:java** - Como executar com Maven

## 🧪 Testes Unitários:

**8 testes criados:**
- ✅ **4 Testes Positivos**: Dados válidos que o sistema espera
- ❌ **4 Testes Negativos**: Dados inválidos que causam erros

**Executar testes:**
```bash
executar-testes.bat
# ou
mvn test
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo JOÃO VICTOR para mais detalhes.

