# RESOLUÇÃO DO CONFLITO - substitua a linha 108 por:
if __name__ == "__main__":
    # Configuração híbrida: melhor dos dois commits
    uvicorn.run(
        app, 
        host="127.0.0.1",  # Sua alteração
        port=8000,         # Padrão mantido
        reload=True,       # Sua alteração  
        log_level="debug"  # Inspirado na alteração do amigo
    )