from flask import Flask, jsonify
import os

app = Flask(__name__)

livros = [
    {"id": 1, "livros": "Haikyuu","autor": "Haruichi Furudado"},
    {"id": 2, "livros": "Heartstopper","autor": "Alice Oseman"},
    {"id": 3, "livros": "Tudo é Rio ","autor": "Carla Madeira"},
    {"id": 4, "livros": "A Biblioteca da Meia-Noite","autor": "Mattb Haig"},
    
]

@app.route("/livros", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de livros - Acesse /livros"})

@app.route("/", methods=["GET"])
def listar_livros():
    return jsonify(livros)

if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)
