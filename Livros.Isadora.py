from flask import Flask, jsonify
import os

app = Flask(-__name__)

livros = [
    {"id": 1, "livros": "Haikyuu"},
    {"id": 2, "livros": "Heartstopper"},
    {"id": 3, "livros": "Tudo é Rio "},
    {"id": 4, "livros": "A Biblioteca da Meia-Noite"},
    
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