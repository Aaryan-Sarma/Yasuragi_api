# api.py
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "API is live!"

@app.route('/api/schedule', methods=['POST'])
def generate_schedule():
    # Get data from the request
    data = request.json

    # Placeholder response (this is where your ML model will be integrated later)
    response = {
        'message': 'This is a placeholder response. Your ML model will generate a personalized schedule based on the input.',
        'input_received': data
    }

    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
