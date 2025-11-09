from flask import Flask, request, jsonify
import requests
from langdetect import detect

app = Flask(__name__)

import os
HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

@app.route("/")
def home():
    return jsonify({"message": "Leggolo AI Backend è attivo 🚀"})

@app.route("/generate", methods=["POST"])
def generate_text():
    data = request.json
    text = data.get("text", "")
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
    result = response.json()
    return jsonify(result)

@app.route("/detect-language", methods=["POST"])
def detect_language():
    data = request.json
    text = data.get("text", "")
    lang = detect(text)
    return jsonify({"language": lang})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Se Render non imposta PORT, usa 5000
    app.run(host="0.0.0.0", port=port)

