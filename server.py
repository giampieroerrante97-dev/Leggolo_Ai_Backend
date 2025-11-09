from flask import Flask, request, jsonify
from flask_cors import CORS # aggiunta importante
import requests
from langdetect import detect
import os

app = Flask(__name__) 
CORS(app) # abilitia richiesta dal frontend


HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

@app.route("/")
def home():
    return jsonify({"message": "Leggolo AI Backend è attivo 🚀"})

@app.route("/generate", methods=["POST"])
@app.route("/genera", methods=["POST"])
def generate_text():
    data = request.json
    text = data.get("text", "")
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
    result = response.json()
    return jsonify(result)

@app.route("/detect-language", methods=["POST"])
@app.route("/traduci", methods=["POST"])
def detect_language():
    data = request.json
    text = data.get("text", "")
    lang = detect(text)
    return jsonify({"language": lang})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Se Render non imposta PORT, usa 10000
    app.run(host="0.0.0.0", port=port)





