from flask import Flask, jsonify
import os

app = Flask(-__name__)

filmes = [
    {"id": 1, "filmes": "Haikyuu"},
    {"id": 2, "filmes": "Heartstopper"},
    {"id": 3, "filmes": "Rio "},
    {"id": 4, "filmes": "A casa monstro"},
    
]

@app.route("/filmes", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de livros - Acesse /filmes"})

@app.route("/", methods=["GET"])
def listar_filmes():
    return jsonify(filmes)

if __name__ == "_main_":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)
