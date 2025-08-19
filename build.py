#!/usr/bin/env python3
"""
Script de build automatizado para Retro Games API
Resolve dependências, executa testes e gera artefato final
"""

import subprocess
import sys
import os
import shutil
import zipfile
from pathlib import Path

def run_command(cmd, description):
    """Executa comando e trata erros"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - OK")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - ERRO")
        print(f"Erro: {e.stderr}")
        sys.exit(1)

def main():
    print("🎮 RETRO GAMES API - BUILD AUTOMATIZADO")
    print("=" * 50)
    
    # 1. Limpar build anterior
    print("🧹 Limpando builds anteriores...")
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    os.makedirs("dist", exist_ok=True)
    
    # 2. Instalar dependências
    run_command("python -m pip install --upgrade pip", "Atualizando pip")
    run_command("python -m pip install -r requirements.txt", "Instalando dependências")
    
    # 3. Executar testes
    print("🧪 Executando testes...")
    try:
        # Iniciar API em background
        api_process = subprocess.Popen([
            sys.executable, "-m", "uvicorn", 
            "retro_games.main:app", "--port", "8000"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Aguardar API inicializar
        import time
        time.sleep(3)
        
        # Executar testes
        subprocess.run([sys.executable, "test_simple.py"], check=True)
        print("✅ Testes - OK")
        
        # Parar API
        api_process.terminate()
        api_process.wait()
        
    except subprocess.CalledProcessError:
        print("❌ Testes falharam")
        if 'api_process' in locals():
            api_process.terminate()
        sys.exit(1)
    
    # 4. Gerar documentação
    print("📚 Gerando documentação...")
    with open("dist/API_DOCS.md", "w", encoding="utf-8") as f:
        f.write("""# Retro Games API - Documentação

## Endpoints Disponíveis:

### Jogos
- GET /games - Listar jogos (com filtros opcionais)
- POST /games - Criar novo jogo
- GET /games/{id} - Buscar jogo específico
- PUT /games/{id} - Atualizar jogo
- DELETE /games/{id} - Deletar jogo

### Utilitários
- GET /consoles - Listar consoles disponíveis
- GET /genres - Listar gêneros disponíveis

## Como executar:
```bash
uvicorn retro_games.main:app --reload
```

Acesse: http://localhost:8000
""")
    
    # 5. Criar pacote distribuível
    print("📦 Criando pacote distribuível...")
    
    # Copiar arquivos essenciais
    files_to_package = [
        "retro_games/",
        "templates/",
        "static/",
        "requirements.txt",
        "main.py",
        "README.md"
    ]
    
    # Criar estrutura do pacote
    package_dir = "dist/retro-games-api"
    os.makedirs(package_dir, exist_ok=True)
    
    for item in files_to_package:
        if os.path.exists(item):
            if os.path.isdir(item):
                shutil.copytree(item, f"{package_dir}/{item}", dirs_exist_ok=True)
            else:
                shutil.copy2(item, f"{package_dir}/{item}")
    
    # Criar script de instalação
    with open(f"{package_dir}/install.bat", "w") as f:
        f.write("""@echo off
echo 🎮 Instalando Retro Games API...
pip install -r requirements.txt
echo ✅ Instalação concluída!
echo 🚀 Execute: python main.py
pause
""")
    
    with open(f"{package_dir}/run.bat", "w") as f:
        f.write("""@echo off
echo 🎮 Iniciando Retro Games API...
python main.py
""")
    
    # 6. Criar arquivo ZIP
    print("🗜️ Compactando pacote...")
    with zipfile.ZipFile("dist/retro-games-api.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_path = os.path.relpath(file_path, "dist")
                zipf.write(file_path, arc_path)
    
    # 7. Gerar relatório de build
    print("📋 Gerando relatório...")
    with open("dist/BUILD_REPORT.txt", "w") as f:
        f.write(f"""RETRO GAMES API - RELATÓRIO DE BUILD
{'=' * 40}

✅ Dependências instaladas
✅ Testes executados com sucesso
✅ Documentação gerada
✅ Pacote criado: retro-games-api.zip

ARTEFATOS GERADOS:
- retro-games-api.zip (pacote completo)
- retro-games-api/ (diretório descompactado)
- API_DOCS.md (documentação)
- BUILD_REPORT.txt (este relatório)

COMO USAR O PACOTE:
1. Extrair retro-games-api.zip
2. Executar install.bat
3. Executar run.bat

Build concluído com sucesso! 🎉
""")
    
    print("\n🎉 BUILD CONCLUÍDO COM SUCESSO!")
    print("📁 Artefatos gerados em: dist/")
    print("📦 Pacote principal: dist/retro-games-api.zip")
    print("📋 Relatório: dist/BUILD_REPORT.txt")

if __name__ == "__main__":
    main()