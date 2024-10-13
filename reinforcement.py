import numpy as np
import random

# Activity lists and user schedule (as previously defined)
# ... [Include the previously defined activities and user_schedule here] ...
import pickle  # Assuming you use pickle to save/load your model

# Load the pre-trained schedule model
with open('schedule_model.pkl', 'rb') as f:
    schedule_model = pickle.load(f)

# Define activity categories
study_activities = [
    'Study',
    'Group study sessions',
    'Online courses',
    'Research projects',
    'Reviewing class notes'
]

workout_activities = [
    'Workout',
    'Morning jogging or running',
    'Strength training',
    'Yoga or Pilates',
    'HIIT workouts'
]

gaming_activities = [
    'Gaming',
    'Multiplayer online games',
    'Casual mobile games',
    'Streaming games',
    'Game design or development'
]

socializing_activities = [
    'Socializing',
    'Coffee with friends',
    'Outdoor games with friends',
    'Attending events or parties',
    'Participating in local clubs or groups'
]

meal_activities = [
    'Meal',
    'Cooking new recipes',
    'Meal prep for the week',
    'Eating out with friends',
    'Having a picnic'
]

sleep_activities = [
    'Sleep',
    'Napping',
    'Sleep hygiene practices',
    'Relaxation before bed'
]

relaxing_activities = [
    'Relaxing',
    'Reading a book',
    'Listening to music',
    'Meditation or mindfulness',
    'Watching TV or movies'
]

cycling_activities = [
    'Cycling',
    'Mountain biking',
    'Leisure cycling',
    'Road cycling',
    'Joining cycling clubs'
]

commute_activities = [
    'Commute',
    'Listening to podcasts',
    'Reading or studying',
    'Relaxing music during travel',
    'Planning the day ahead'
]

# Full list of activities categorized
activities = {
    'Study Activities': study_activities,
    'Workout Activities': workout_activities,
    'Gaming Activities': gaming_activities,
    'Socializing Activities': socializing_activities,
    'Meal Activities': meal_activities,
    'Sleep Activities': sleep_activities,
    'Relaxing Activities': relaxing_activities,
    'Cycling Activities': cycling_activities,
    'Commute Activities': commute_activities
}

# User's current schedule
user_schedule = {
    '22:00 - 06:00': 'Sleep',
    '06:00 - 06:30': 'Flexible Time',
    '06:30 - 07:00': 'Daily Routine',
    '07:00 - 07:30': 'Meals',
    '07:30 - 08:00': 'Commute',
    '08:00 - 12:30': 'Study',
    '12:30 - 13:00': 'Meals',
    '13:00 - 16:30': 'Study',
    '16:30 - 17:00': 'Commute',
    '17:00 - 18:00': 'Flexible Time',
    '18:00 - 19:00': 'Study',
    '19:00 - 20:00': 'Flexible Time',
    '20:00 - 20:30': 'Meals',
    '20:30 - 22:00': 'Flexible Time'
}

# Function to retrieve flexible time slots indices
def find_flexible_time_indices(schedule):
    return [index for index, activity in enumerate(schedule.values()) if activity == 'Flexible Time']

# Function to retrieve time slots
def retrieve_time_slots(schedule):
    return list(schedule.keys())

# Reinforcement Learning for Schedule Optimization
def optimize_schedule(user_schedule, activities):
    flexible_indices = find_flexible_time_indices(user_schedule)
    time_slots = retrieve_time_slots(user_schedule)

    # Example preferences for activities in Flexible Time
    preferred_activities = workout_activities + relaxing_activities + socializing_activities

    # Modify flexible time slots with random selections from preferred activities
    for index in flexible_indices:
        # Randomly select an activity from the preferred activities
        selected_activity = random.choice(preferred_activities)
        
        # Update the schedule with the new activity
        time_slot = time_slots[index]
        user_schedule[time_slot] = selected_activity

    return user_schedule

# Example of optimizing the user schedule
optimized_schedule = optimize_schedule(user_schedule, activities)

# Find flexible time slots in user schedule
flexible_time_slots = find_flexible_time_indices(user_schedule)

# Initialize Q-table for Q-learning
Q = np.zeros((len(flexible_time_slots), len(activities)))

# Parameters for Q-learning
alpha = 0.1    # Learning rate
gamma = 0.9    # Discount factor
epsilon = 0.1  # Exploration factor

# Define rewards based on your goals
# Initialize rewards based on individual parameters
def get_dynamic_rewards(gender, age, occupation, physical_health_goals, mental_health_goals, fitness_level, exercise_freq):
    # Base rewards dictionary
    base_rewards = {
        'Study': 2, 
        'Workout': 10,   # High reward for workout
        'Gaming': -1,    
        'Socializing': 3,  
        'Meal': 5,
        'Sleep': 8,
        'Relaxing': 4,
        'Cycling': 8,
        'Commute': 1
    }
    
    # Modify rewards based on user characteristics
    if physical_health_goals == 'Weight loss':
        base_rewards['Workout'] += 5  # Increased reward for working out
    elif physical_health_goals == 'Muscle building':
        base_rewards['Workout'] += 3   # Moderate increase for muscle building goals
    
    if mental_health_goals == 'Stress reduction':
        base_rewards['Relaxing'] += 3  # Higher reward for relaxation activities
    
    if fitness_level == 'Beginner':
        base_rewards['Workout'] -= 2   # Decrease reward for workout for beginners
    
    if exercise_freq in ['Rarely or never', '1-2 times a week']:
        base_rewards['Workout'] -= 5   # Decrease reward if exercise frequency is low
    
    # Additional adjustments can be made based on other parameters
    
    return base_rewards

gender = 'Male'
age =  20
occupation = 'Student'
height = 170
weight = 80
wake_time = '08:00'
sleep_time = '23:00'
routine_type = 'Flexible'
current_daily_routine_feel = 'Neutral'
schedule_commitment = 'Sometimes'
free_time_activities = 'Gaming'
screen_time = '2-4 hours'
feel_eod = 'Demotivated'
physical_health_goals = 'Weight loss'
mental_health_goals = 'Stress reduction'
mental_health_factors = 'Stress Management'
physical_health_factors = 'Fatigue'
visit_healthcare_professional = 'Occasionally (A few times a year)'
smoke = 'Never'
alcohol = 'Never'
fitness_level = 'Intermediate'
exercise_freq = 'Rarely or never'
workout_duration = 'More than 60 minutes'
physical_activity_pref = 'Strength training'
exercise_time_pref = 'Morning'
stress_freq = 'A few times a week'
meditation_freq = 'Rarely'
cope_with_stress = 'Talking with friends or family'
hobbies_freq = 'Rarely'
self_reflection_enjoy = 'Sometimes'
spend_time_outdoors = 'Daily'
activity_pref = 'Creative activities'
in_out_activities = 'Indoor'
break_during_work = 'I take regular breaks'
self_care = 'A few times a week'

rewards = get_dynamic_rewards(gender, age, occupation, physical_health_goals, mental_health_goals, fitness_level, exercise_freq)

# Now, use this dynamic rewards dictionary in the Q-learning training


# Choose action using epsilon-greedy strategy
def choose_action(state):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice(len(activities))  # Explore
    else:
        return np.argmax(Q[state, :])  # Exploit

# Get reward for the chosen activity
def get_reward(action):
    return rewards[activities[action]]

# Training the agent
num_episodes = 1000  # Simulate 1000 days for training

for episode in range(num_episodes):
    for i in range(len(flexible_time_slots)):
        state = i  # Current flexible time slot
        
        # Choose action for the current flexible time slot
        action = choose_action(state)
        
        # Get reward based on chosen activity
        reward = get_reward(action)
        
        # Next state (circular transition)
        next_state = (state + 1) % len(flexible_time_slots)
        
        # Update Q-value
        Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state, :]) - Q[state, action])

with open('q_table.pkl', 'wb') as f:
    pickle.dump(Q, f)

# After training, update the user schedule with optimal activities
for i, slot in enumerate(flexible_time_slots):
    state = i
    best_action = np.argmax(Q[state, :])  # Get best activity for each flexible slot
    time_slot = retrieve_time_slots(user_schedule)[slot]
    user_schedule[time_slot] = activities[best_action]  # Update schedule with best action

# Print the optimized schedule
print("Optimized Schedule:")
for time_slot, activity in user_schedule.items():
    print(f"{time_slot}: {activity}")

