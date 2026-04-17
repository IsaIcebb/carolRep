from flask import Flask, jsonify
import os

app = Flask(__name__)

alunos = [
    {"id": 1, "alunos": "Isadora Moreti","curso": "Desenvolvimento de Sistemas"},
    {"id": 2, "alunos": "Rita Silva","curso": "Serviço Jurídico"},
    {"id": 3, "alunos": "Cássia Eller ","curso": "Infonet"},
    {"id": 4, "alunos": "Renata Moretto","curso": "IF"},
    
]

@app.route("/alunos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de alunos - Acesse /alunos"})

@app.route("/", methods=["GET"])
def listar_alunos():
    return jsonify(livros)

if __name__ == "_main_":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)
