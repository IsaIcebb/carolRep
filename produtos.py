from flask import Flask, jsonify
import os

app = Flask(-__name__)

produtos = [
    {"id": 1, "produtos": "Haikyuu","autor": "Haruichi Furudado"},
    {"id": 2, "produtos": "Heartstopper","autor": "Alice Oseman"},
    {"id": 3, "produtos": "Tudo é Rio ","autor": "Carla Madeira"},
    {"id": 4, "produtos": "A Biblioteca da Meia-Noite","autor": "Mattb Haig"},
    
]

@app.route("/livros", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de livros - Acesse /livros"})

@app.route("/", methods=["GET"])
def listar_livros():
    return jsonify(livros)

if __name__ == "_main_":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0", port=port)
