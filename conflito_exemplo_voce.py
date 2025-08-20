# VOCÊ deve alterar a linha 108 do retro_games/main.py de:
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# PARA:
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=True, log_level="info")