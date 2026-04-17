from flask import Flask, jsonify
import os

app = Flask(__name__)

jogos = [
    {"id": 1, "jogos": "Minecraft","plataforma":"microsoft"},
    {"id": 2, "jogos": "genshin impact", "plataforma":"playstore"},
    {"id": 3, "jogos": "moranguinho ", "plataforma":"app store"},
    {"id": 4, "jogos": "Subway-surf", "plataforma":"app store"},
    
]

@app.route("/jogos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de livros - Acesse /jogos"})

@app.route("/", methods=["GET"])
def listar_jogos():
    return jsonify(jogos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)
