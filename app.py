# api.py
'''import os
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
    app.run(host="0.0.0.0", port=port) '''



import os
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = joblib.load('schedule_model.pkl')

@app.route('/')
def index():
    return "API is live!"

@app.route('/api/schedule', methods=['POST'])
def generate_schedule():
    # Get data from the request
    data = request.json
    
    # Extract parameters from the data (assuming data structure matches your model's input requirements)
    gender = data.get('gender')
    age = data.get('age')
    occupation = data.get('occupation')
    physical_health_goals = data.get('physical_health_goals')
    mental_health_goals = data.get('mental_health_goals')
    fitness_level = data.get('fitness_level')
    exercise_freq = data.get('exercise_freq')

    # Create a DataFrame or suitable structure for prediction if your model requires it
    input_data = pd.DataFrame({
        'gender': [gender],
        'age': [age],
        'occupation': [occupation],
        'physical_health_goals': [physical_health_goals],
        'mental_health_goals': [mental_health_goals],
        'fitness_level': [fitness_level],
        'exercise_freq': [exercise_freq]
    })

    # Generate the schedule using your model
    predicted_schedule = model.predict(input_data)

    # Prepare the response
    response = {
        'message': 'Schedule generated successfully!',
        'predicted_schedule': predicted_schedule.tolist()  # Convert to list if needed
    }

    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)

