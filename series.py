from flask import Flask, jsonify
import os

app = Flask(__name__)

series = [
    {"id": 1, "series": "MIB","temporada": "2"},
    {"id": 2, "series": "Gilmore Girls","temporada": "8"},
    {"id": 3, "series": "Bluey","temporada": "3"},
    {"id": 4, "series": "Game of Thrones","temporada": "13"},
    
]

@app.route("/series", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de produtos - Acesse /series"})

@app.route("/", methods=["GET"])
def listar_series():
    return jsonify(series)

if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)
