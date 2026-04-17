from flask import Flask, jsonify
import os

app = Flask(__name__)

produtos = [
    {"id": 1, "produtos": "Creme de Cabelo","preço": "9 reais"},
    {"id": 2, "produtos": "Caneta preta","preço": "3 reais"},
    {"id": 3, "produtos": "Matizador Roxo","preço": "12 reais"},
    {"id": 4, "produtos": "Anel","preço": "14 reais"},
    
]

@app.route("/produtos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de produtos - Acesse /produtos"})

@app.route("/", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)
