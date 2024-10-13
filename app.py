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
try:
    model = joblib.load('q_table.pkl')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def index():
    return "API is live!"

@app.route('/api/schedule', methods=['POST'])
def generate_schedule():
    # Get data from the request
    data = request.json
    
    # Validate required fields
    required_fields = ['gender', 'age', 'occupation', 'height', 'weight', 'wake_time', 'sleep_time']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Extract parameters from the data
    gender = data.get('gender')
    age = data.get('age')
    occupation = data.get('occupation')
    height = data.get('height')
    weight = data.get('weight')
    wake_time = data.get('wake_time')
    sleep_time = data.get('sleep_time')
    routine_type = data.get('routine_type')
    current_daily_routine_feel = data.get('current_daily_routine_feel')
    schedule_commitment = data.get('schedule_commitment')
    free_time_activities = data.get('free_time_activities')
    screen_time = data.get('screen_time')
    feel_eod = data.get('feel_eod')
    physical_health_goals = data.get('physical_health_goals')
    mental_health_goals = data.get('mental_health_goals')
    mental_health_factors = data.get('mental_health_factors')
    physical_health_factors = data.get('physical_health_factors')
    visit_healthcare_professional = data.get('visit_healthcare_professional')
    smoke = data.get('smoke')
    alcohol = data.get('alcohol')
    fitness_level = data.get('fitness_level')
    exercise_freq = data.get('exercise_freq')
    workout_duration = data.get('workout_duration')
    physical_activity_pref = data.get('physical_activity_pref')
    exercise_time_pref = data.get('exercise_time_pref')
    stress_freq = data.get('stress_freq')
    meditation_freq = data.get('meditation_freq')
    cope_with_stress = data.get('cope_with_stress')
    hobbies_freq = data.get('hobbies_freq')
    self_reflection_enjoy = data.get('self_reflection_enjoy')
    spend_time_outdoors = data.get('spend_time_outdoors')
    activity_pref = data.get('activity_pref')
    in_out_activities = data.get('in_out_activities')
    break_during_work = data.get('break_during_work')
    self_care = data.get('self_care')

    # Create a DataFrame or suitable structure for prediction if your model requires it
    input_data = pd.DataFrame({
        'gender': [gender],
        'age': [age],
        'occupation': [occupation],
        'height': [height],
        'weight': [weight],
        'wake_time': [wake_time],
        'sleep_time': [sleep_time],
        'routine_type': [routine_type],
        'current_daily_routine_feel': [current_daily_routine_feel],
        'schedule_commitment': [schedule_commitment],
        'free_time_activities': [free_time_activities],
        'screen_time': [screen_time],
        'feel_eod': [feel_eod],
        'physical_health_goals': [physical_health_goals],
        'mental_health_goals': [mental_health_goals],
        'mental_health_factors': [mental_health_factors],
        'physical_health_factors': [physical_health_factors],
        'visit_healthcare_professional': [visit_healthcare_professional],
        'smoke': [smoke],
        'alcohol': [alcohol],
        'fitness_level': [fitness_level],
        'exercise_freq': [exercise_freq],
        'workout_duration': [workout_duration],
        'physical_activity_pref': [physical_activity_pref],
        'exercise_time_pref': [exercise_time_pref],
        'stress_freq': [stress_freq],
        'meditation_freq': [meditation_freq],
        'cope_with_stress': [cope_with_stress],
        'hobbies_freq': [hobbies_freq],
        'self_reflection_enjoy': [self_reflection_enjoy],
        'spend_time_outdoors': [spend_time_outdoors],
        'activity_pref': [activity_pref],
        'in_out_activities': [in_out_activities],
        'break_during_work': [break_during_work],
        'self_care': [self_care]
    })

    # Predict schedule using your model
    if model:
        try:
            predicted_schedule = model.predict(input_data)
        except Exception as e:
            return jsonify({'error': f'Prediction failed: {str(e)}'}), 500
    else:
        return jsonify({'error': 'Model not loaded properly'}), 500

    # Prepare the response
    response = {
        'message': 'Schedule generated successfully!',
        'predicted_schedule': predicted_schedule.tolist()  # Convert to list if needed
    }

    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
