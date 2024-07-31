from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Define the API key and endpoint
API_KEY = os.getenv('GEMINI_API_KEY')
ENDPOINT = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    headers = {
        'Content-Type': 'application/json',
    }
    params = {
        'key': API_KEY
    }
    response = requests.post(
        ENDPOINT,
        headers=headers,
        params=params,
        json=data
    )
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
