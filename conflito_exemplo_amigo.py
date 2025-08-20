# SEU AMIGO deve alterar a linha 108 do retro_games/main.py de:
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# PARA:
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9000, debug=True)