import pandas as pd
import random
from datetime import datetime, timedelta

def adjust_time(time_range, variation_minutes=15):
    """Adjusts the start and end times of the time range within a variation."""
    start, end = time_range.split(" - ")
    start_hour, start_minute = map(int, start.split(":"))
    end_hour, end_minute = map(int, end.split(":"))

    # Adjust start and end by a random variation (up to ±variation_minutes)
    start_minute += random.randint(-variation_minutes, variation_minutes)
    end_minute += random.randint(-variation_minutes, variation_minutes)

    # Ensure minute values are between 0 and 59 and adjust the hour if necessary
    if start_minute < 0:
        start_hour -= 1
        start_minute += 60
    elif start_minute >= 60:
        start_hour += 1
        start_minute -= 60

    if end_minute < 0:
        end_hour -= 1
        end_minute += 60
    elif end_minute >= 60:
        end_hour += 1
        end_minute -= 60

    # Handle wrap-around for hours
    start_hour %= 24
    end_hour %= 24

    start_time = f"{start_hour:02}:{start_minute:02}"
    end_time = f"{end_hour:02}:{end_minute:02}"

    return f"{start_time} - {end_time}", start_time, end_time  # Return the adjusted time and also start and end times

def generate_schedule(template):
    schedule = {}
    previous_end_time = None

    for time_range, activity in template.items():
        adjusted_time, start_time, end_time = adjust_time(time_range)
        
        # If it's the first activity, initialize previous_end_time
        if previous_end_time is None:
            previous_end_time = start_time

        # If there is a previous end time, adjust the current start time
        if previous_end_time:
            start_time = previous_end_time

        # Update previous_end_time to be the current end time
        previous_end_time = end_time

        # Add the activity to the schedule with the adjusted times
        schedule[f"{start_time} - {end_time}"] = activity

    # Adjust the last activity's end time to match the start time of the first activity
    first_start_time = list(schedule.keys())[0].split(" - ")[0]
    last_activity_key = list(schedule.keys())[-1]
    last_end_time = previous_end_time

    # Update last activity to connect with the first
    if last_end_time != first_start_time:
        activity = schedule[last_activity_key]
        # Set the last activity's end time to match the first activity's start time
        new_end_time = first_start_time
        schedule[f"{last_activity_key.split(' - ')[0]} - {new_end_time}"] = activity
        del schedule[last_activity_key]  # Remove the old last activity

    return schedule


def generate_user_profile():
    gender = ['Male', 'Female', 'Non-binary', 'Prefer not to say']
    age = []  # You can specify age ranges or leave it empty for free text.
    occupation = ['Student', 'Working professional', 'Homemaker', 'Freelancer', 'Unemployed', 'Retired']
    height = []  # You can specify height ranges or leave it empty for free text.
    weight = []  # You can specify weight ranges or leave it empty for free text.
    wake_time = []  # Add any other specific times as needed
    sleep_time = []  # Add any other specific times as needed
    routine_type = ['Structured', 'Flexible', 'No preference']
    current_daily_routine_feel = ['Very satisfied', 'Satisfied', 'Neutral', 'Unsatisfied', 'Very unsatisfied']
    schedule_commitment = ['Always', 'Mostly', 'Sometimes', 'Rarely', 'Never']
    free_time_activities = ['Relaxing at home', 'Socializing with friends', 'Exercising or sports', 
                            'Creative hobbies', 'Cinema', 'Gaming']
    screen_time = ['0-2 hours', '2-4 hours', '4-6 hours', '6-8 hours', '8-10 hours', '10+ hours']
    feel_eod = ['Energized', 'Tired but satisfied', 'Exhausted', 'Stressed', 
                          'Demotivated', 'Calm']
    physical_health_goals = ['Weight loss', 'Weight gain', 'Muscle building', 'None']
    mental_health_goals = ['Stress reduction', 'Better focus/mental clarity', 'Improved sleep', 'None']
    mental_health_factors = ['Stress Management', 'Mood Regulation', 'Focus and Attention', 'Energy and Motivation', 'Sleep and Rest', 'None']

    physical_health_factors = ['Chronic Pain', 'Fatigue', 'Mobility Issues', 'Heart or Blood Pressure Conditions', 'Respiratory Issues', 'None']

    visit_healthcare_professional = ['Regularly (Monthly)', 'Occasionally (A few times a year)', 
                                  'Rarely (Once a year or less)', 'Never']
    smoke = ['Never', 'Occasionally', '1-2 times a week', '3-5 times a week', 'Regularly']
    alcohol = ['Never', 'Occasionally (socially or less than once a month)', 
                                      '1-2 times a month', '1-2 times a week', 'Regularly']
    fitness_level = ['Beginner', 'Intermediate', 'Advanced']
    exercise_freq = ['Daily', '3-5 times a week', '1-2 times a week', 'Rarely or never']
    workout_duration = ['Less than 30 minutes', '30-60 minutes', 'More than 60 minutes']
    physical_activity_pref = ['Running or jogging', 'Strength training', 'Yoga or Pilates', 
                                    'Walking or hiking', 'Team sports']
    exercise_time_pref = ['Morning', 'Afternoon', 'Evening', 'No specific preference']
    stress_freq = ['Daily', 'A few times a week', 'Rarely', 'Never']
    meditation_freq = ['Daily', 'A few times a week', 'Rarely', 'Never']
    cope_with_stress = ['Meditation', 'Physical exercise', 'Talking with friends or family', 
                            'Journaling or writing']

    hobbies_freq = ['Daily', 'A few times a week', 'Rarely', 'Never']
    self_reflection_enjoy = ['Yes', 'No', 'Sometimes']
    spend_time_outdoors = ['Daily', 'A few times a week', 'Rarely', 'Never']
    activity_pref = ['Physical exercise', 'Meditation or mindfulness', 
                                      'Journaling or reflection', 'Social activities', 
                                      'Creative activities']
    in_out_activities = ['Indoor', 'Outdoor', 'No preference']
    break_during_work = ['I take regular breaks', 'I sometimes forget to take breaks', 
                        'I rarely take breaks', 'I don\'t like taking breaks']
    self_care = ['Daily', 'A few times a week', 'Rarely', 'Never']




    age = random.randint(13, 75)

    # Determine occupation based on age
    if age < 20 or (20 <= age <= 30 and random.choice([True, False])):  
        occupation = 'Student'
    elif age < 50:  # If age is between 20 and 49
        occupations = ['Working professional', 'Homemaker', 'Freelancer', 'Unemployed']
        occupation = random.choice(occupations)
    elif 50 <= age <= 60:
        occupations = ['Working professional', 'Homemaker', 'Freelancer', 'Unemployed','Retired']
        occupation = random.choice(occupations)
    else:  # Age 60 or older
        occupation = 'Retired'

    profile = {
        'gender': random.choice(gender),
        'age': age,  
        'occupation': occupation,
        'height': random.randint(100, 250),  # Height in cm
        'weight': random.randint(30, 200),    # Weight in kg
        'wake_time': f"{random.randint(3, 12):02d}:{random.randint(0, 59):02d}",
        'sleep_time': f"{random.randint(17, 23) if random.randint(0, 1) == 0 else random.randint(0, 3):02d}:{random.randint(0, 59):02d}",
        'routine_type': random.choice(routine_type),
        'current_daily_routine_feel': random.choice(current_daily_routine_feel),
        'schedule_commitment' : random.choice(schedule_commitment),
        'free_time_activities' : random.choice(free_time_activities),
        'screen_time' : random.choice(screen_time),
        'feel_eod' : random.choice(feel_eod),
        'physical_health_goals' : random.choice(physical_health_goals),
        'mental_health_goals': random.choice(mental_health_goals),
        'mental_health_factors' : random.choice(mental_health_factors),
        'physical_health_factors' : random.choice(physical_health_factors),
        'visit_healthcare_professional' : random.choice(visit_healthcare_professional),
        'smoke' : random.choice(smoke),
        'alcohol' : random.choice(alcohol),
        'fitness_level' : random.choice(fitness_level),
        'exercise_freq' : random.choice(exercise_freq),
        'workout_duration' : random.choice(workout_duration),
        'physical_activity_pref' : random.choice(physical_activity_pref),
        'exercise_time_pref' : random.choice(exercise_time_pref),
        'stress_freq' : random.choice(stress_freq),
        'meditation_freq' : random.choice(meditation_freq),
        'cope_with_stress' : random.choice(cope_with_stress),
        'hobbies_freq' : random.choice(hobbies_freq),
        'self_reflection_enjoy' : random.choice(self_reflection_enjoy),
        'spend_time_outdoors' : random.choice(spend_time_outdoors),
        'activity_pref' : random.choice(activity_pref),
        'in_out_activities' : random.choice(in_out_activities),
        'break_during_work' : random.choice(break_during_work),
        'self_care' : random.choice(self_care)
    }
    
    return profile

def create_schedule(user_profile):
    profile_occ = user_profile['occupation']
    template = {}

    if profile_occ == 'Student':
        template['22:00 - 06:00'] = 'Sleep/Rest'  # Sleep from 23:00 to 07:00, spanning across midnight
        template['06:00 - 06:30'] = 'Flexible Time'
        template['06:30 - 07:00'] = 'Daily Routine'
        template['07:00 - 07:30'] = 'Meals'  # Breakfast
        template['07:30 - 08:00'] = 'Commute/Travel'
        template['08:00 - 12:30'] = 'Work/Study'
        template['12:30 - 13:00'] = 'Meals'  # Lunch
        template['13:00 - 16:30'] = 'Work/Study'
        template['16:30 - 17:00'] = 'Commute/Travel'
        template['17:00 - 18:00'] = 'Flexible Time'
        template['18:00 - 19:00'] = 'Work/Study'
        template['19:00 - 20:00'] = 'Flexible Time'
        template['20:00 - 20:30'] = 'Meals'  # Dinner
        template['20:30 - 22:00'] = 'Flexible Time'

    elif profile_occ == 'Working professional':
        template['23:00 - 07:00'] = 'Sleep/Rest' 
        template['07:00 - 07:30'] = 'Daily Routine'
        template['07:30 - 08:00'] = 'Meals'  # Breakfast
        template['08:00 - 08:30'] = 'Commute/Travel'
        template['08:30 - 12:30'] = 'Work'
        template['12:30 - 13:00'] = 'Meals'  # Lunch
        template['13:00 - 17:00'] = 'Work'
        template['17:00 - 17:30'] = 'Commute/Travel'
        template['17:30 - 19:00'] = 'Flexible Time'
        template['19:00 - 20:30'] = 'Work'
        template['20:30 - 21:00'] = 'Meals'  # Dinner
        template['21:00 - 23:00'] = 'Flexible Time'

    elif profile_occ == 'Homemaker':
        template['23:00 - 06:00'] = 'Sleep/Rest' 
        template['06:00 - 07:00'] = 'Household Chores'
        template['07:00 - 07:30'] = 'Meals'  # Breakfast
        template['07:30 - 13:30'] = 'Household Chores'
        template['13:30 - 14:00'] = 'Meals'  # Lunch
        template['14:00 - 14:30'] = 'Household Chores'
        template['14:30 - 16:00'] = 'Flexible Time'
        template['16:00 - 17:00'] = 'Household Chores'
        template['17:00 - 18:00'] = 'Leisure/Hobbies'
        template['18:00 - 20:00'] = 'Household Chores'
        template['20:00 - 20:30'] = 'Meals'  # Dinner
        template['20:30 - 23:00'] = 'Flexible Time'

    elif profile_occ == 'Freelancer':
        template['23:00 - 07:00'] = 'Sleep/Rest' 
        template['07:00 - 07:30'] = 'Daily Routine'
        template['07:30 - 08:00'] = 'Household Chores'
        template['08:00 - 11:00'] = 'Work'
        template['11:00 - 12:30'] = 'Flexible Time'
        template['12:30 - 13:00'] = 'Meals'  # Lunch
        template['13:00 - 16:30'] = 'Flexible Time'
        template['16:30 - 18:00'] = 'Work'
        template['18:00 - 19:00'] = 'Leisure/Hobbies'
        template['19:00 - 20:00'] = 'Flexible Time'
        template['20:00 - 20:30'] = 'Meals'  # Dinner
        template['20:30 - 23:00'] = 'Flexible Time'

    elif profile_occ == 'Unemployed':
        template['01:00 - 10:00'] = 'Sleep/Rest'  
        template['10:00 - 10:30'] = 'Daily Routine'
        template['10:30 - 11:00'] = 'Meals'  # Breakfast
        template['11:00 - 12:00'] = 'Job Search'
        template['12:00 - 13:00'] = 'Flexible Time'
        template['13:00 - 13:30'] = 'Meals'  # Lunch
        template['13:30 - 17:00'] = 'Flexible Time'
        template['17:00 - 20:00'] = 'Leisure/Hobbies'
        template['20:00 - 20:30'] = 'Meals'  # Dinner
        template['20:30 - 21:00'] = 'Family Time'
        template['21:00 - 01:00'] = 'Flexible Time'

    elif profile_occ == 'Retired':
        template['23:00 - 06:30'] = 'Sleep/Rest'  
        template['06:30 - 07:00'] = 'Leisure/Hobbies'
        template['07:00 - 08:00'] = 'Flexible Time'
        template['08:00 - 08:30'] = 'Daily Routine'
        template['08:30 - 09:00'] = 'Leisure/Hobbies'
        template['09:00 - 10:00'] = 'Household Chores'
        template['10:00 - 11:00'] = 'Leisure/Hobbies'
        template['11:00 - 13:00'] = 'Flexible Time'
        template['13:00 - 13:30'] = 'Meals'  # Lunch
        template['13:30 - 14:30'] = 'Leisure/Hobbies'
        template['14:30 - 16:00'] = 'Sleep/Rest'
        template['16:00 - 17:00'] = 'Leisure/Hobbies'
        template['17:00 - 18:00'] = 'Flexible Time'
        template['18:00 - 18:30'] = 'Leisure/Hobbies'
        template['18:30 - 20:00'] = 'Social Time'  # Friends time
        template['20:00 - 20:30'] = 'Meals'  # Dinner
        template['20:30 - 23:00'] = 'Flexible Time'

    # Generate a schedule with slight variations for this profile
    schedulevar = generate_schedule(template)
    return schedulevar

def categorize_time_slot(time_slot):
    # Split the time slot into start and end times
    start_time, end_time = time_slot.split(' - ')
    
    # Convert time strings to hours for easier comparison
    start_hour = int(start_time.split(':')[0])
    end_hour = int(end_time.split(':')[0])
    
    # Define time categories based on hour ranges
    if 5 <= start_hour < 12:  # Early morning and morning
        return 'Morning'
    elif 12 <= start_hour < 17:  # Afternoon
        return 'Afternoon'
    elif 17 <= start_hour < 21:  # Evening
        return 'Evening'
    else:  # Night
        return 'Night'

def find_original_flexible_time_slots(template):
  flexible_time_slots = []  # Initialize an empty list to store flexible time slots

  # Loop through the template dictionary
  for time_slot, activity in template.items():
      if activity == 'Flexible Time':  # Check if the activity is 'Flexible Time'
          flexible_time_slots.append(time_slot)  # Append the time slot to the list

  return flexible_time_slots  # Return the list of flexible time slots

def find_flexible_time_slots(template):
    """
    Find and return a list of time slots designated as 'Flexible Time' from the given template.
    If a time slot exceeds one hour, it is broken down into one-hour segments.

    Parameters:
    - template (dict): A dictionary where keys are time slots and values are associated activities.

    Returns:
    - List: A list of time slots that are labeled as 'Flexible Time', with long slots broken into hourly segments.
    """
    flexible_time_slots = []  # Initialize an empty list to store flexible time slots

    for time_slot, activity in template.items():
        if activity == 'Flexible Time':  # Check if the activity is 'Flexible Time'
            start_time_str, end_time_str = time_slot.split(' - ')
            start_time = datetime.strptime(start_time_str, "%H:%M")  # Convert to datetime
            end_time = datetime.strptime(end_time_str, "%H:%M")  # Convert to datetime

            # Check the duration of the time slot
            current_time = start_time
            while current_time < end_time:
                next_time = current_time + timedelta(hours=1)
                # Ensure the next time does not exceed the end time
                if next_time > end_time:
                    next_time = end_time
                # Format the time slots back to strings
                formatted_slot = f"{current_time.strftime('%H:%M')} - {next_time.strftime('%H:%M')}"
                flexible_time_slots.append(formatted_slot)  # Append the formatted time slot
                current_time = next_time  # Move to the next time segment

    return flexible_time_slots  # Return the list of flexible time slots

def create_target_schedule(user_profile):
  template = create_schedule(user_profile)
  template_initial = template.copy()
  flexible_time_slots = find_flexible_time_slots(template)
  # rules to modify schedule
  morning_exercise = [
        'Morning jogging or running',
        'Sunrise yoga or Pilates',
        'Bodyweight exercises (pushups, squats)'
    ]
    
  afternoon_exercise = [
        'Strength training or weight lifting',
        'Group sports (tennis, basketball)',
        'Cycling in the afternoon'
    ]
    
  evening_exercise = [
        'Evening walk or light jogging',
        'Strength training or HIIT workout',
        'Dance classes or aerobic workout'
    ]
    
  no_pref_exercise = [
        'Anytime flexibility exercises',
        'Walking or jogging whenever convenient',
        'At-home strength exercises'
    ]
    
  mental_health_activities = [
        'Mindfulness or Journaling',
        'Art therapy or creative expression',
        'Reading for pleasure or relaxation'
    ]
    
  social_hobbies = [
        'Coffee with friends or socializing',
        'Outdoor games or group activities',
        'Join a local hobby group or club'
    ]

  relaxation_activities = [
        'Gentle stretching or yoga',
        'Meditation or mindfulness practice',
        'Listening to calming music or podcasts'
    ]

  creative_hobbies = [
        'Drawing or sketching',
        'Writing a short story or journaling',
        'Crafting or DIY projects'
    ]
  
  self_care_activities = [
        'Night-time skincare routine',
        'Reading a book',
        'Journaling about your day'
    ]
    
  winding_down_activities = [
        'Listening to soothing music',
        'Practicing deep breathing exercises',
        'Doing light stretching or yoga'
    ]
 
  light_entertainment = [
        'Watching a relaxing movie or series',
        'Playing a light video game',
        'Enjoying a casual hobby like drawing or crafting'
    ]

  for time_slots in flexible_time_slots:
    if categorize_time_slot(time_slots) == 'Morning':
        # Integrate Physical Health Goals
        if user_profile['physical_health_goals'] == 'Weight loss':
            if 'Chronic Pain' not in user_profile['physical_health_factors']:
                template[time_slots] = morning_exercise[0]  # Morning jogging or running
            else:
                template[time_slots] = 'Gentle morning yoga: Focus on low-impact movements to aid mobility without aggravating pain.'

        elif user_profile['physical_health_goals'] == 'Weight gain':
            if user_profile['exercise_time_pref'] == 'Morning':
                template[time_slots] = morning_exercise[1]  # Sunrise yoga or Pilates
            else:
                template[time_slots] = "High-Protein Breakfast: Prioritize meals with protein to support muscle gain."

        elif user_profile['physical_health_goals'] == 'Muscle building':
            if user_profile['exercise_time_pref'] == 'Morning':
                template[time_slots] = morning_exercise[2]  # Bodyweight exercises
            else:
                template[time_slots] = "Balanced Breakfast: Include a mix of protein and carbs to fuel muscle growth."

        else:  # None
            if user_profile['mental_health_goals'] == 'Stress reduction':
                if user_profile['mental_health_factors'] == 'Stress Management':
                    template[time_slots] = "Guided Morning Meditation: Focus on relaxation techniques to set a positive tone for the day."
                else:
                    template[time_slots] = "Mindful Morning Walk: Connect with nature to enhance mental clarity."

        # Mental Health Goals
        if user_profile['mental_health_goals'] == 'Better focus/mental clarity':
            if user_profile['mental_health_factors'] == 'Focus and Attention':
                template[time_slots] = "Brain-Boosting Activities: Engage in puzzles or light reading to stimulate mental clarity."
            else:
                template[time_slots] = "Organized Morning Routine: Plan the day with a focus on priorities to enhance productivity."

        elif user_profile['mental_health_goals'] == 'Improved sleep':
            if user_profile['mental_health_factors'] == 'Sleep and Rest':
                template[time_slots] = "Morning Stretching: Light stretches to wake the body gently."
            else:
                template[time_slots] = "Relaxing Morning Routine: Take time for a slow breakfast and reflection to start the day calmly."

        # Physical Health Factors
        if 'Fatigue' in user_profile['physical_health_factors']:
            template[time_slots] = "Gentle Morning Activities: Opt for a slow-paced routine, focusing on hydration and light movement."
        
        elif 'Mobility Issues' in user_profile['physical_health_factors']:
            template[time_slots] = "Adaptive Morning Exercises: Focus on seated or low-impact exercises to promote mobility without strain."
        
        elif 'Heart or Blood Pressure Conditions' in user_profile['physical_health_factors']:
            template[time_slots] = "Heart-Healthy Morning Routine: Start the day with light cardio and a balanced breakfast to support heart health."
        
        elif 'Respiratory Issues' in user_profile['physical_health_factors']:
            template[time_slots] = "Breathing Exercises: Engage in breathing techniques to enhance lung capacity and promote relaxation."

    if categorize_time_slot(time_slots) == 'Afternoon':
        # Prioritize based on Physical Health Goals
        if user_profile['physical_health_goals'] == 'Weight loss':
            template[time_slots] = random.choice(afternoon_exercise)  # Strength training or weight lifting
            if user_profile['physical_health_factors'] == 'Fatigue':
                template[time_slots] += " with a focus on low-intensity exercises to avoid overexertion."

        elif user_profile['physical_health_goals'] == 'Weight gain':
            template[time_slots] = afternoon_exercise[1]  # Group sports (tennis, basketball)
            if user_profile['physical_health_factors'] == 'Mobility Issues':
                template[time_slots] += " with modifications to accommodate your mobility needs."

        elif user_profile['physical_health_goals'] == 'Muscle building':
            template[time_slots] = afternoon_exercise[2]  # Cycling in the afternoon
            if user_profile['physical_health_factors'] == 'Chronic Pain':
                template[time_slots] += " at a comfortable pace, focusing on endurance rather than intensity."

        else:  # None
            # Focus on Mental Health Goals
            if user_profile['mental_health_goals'] == 'Stress reduction':
                template[time_slots] = mental_health_activities[0]  # Mindfulness or Journaling
                if user_profile['mental_health_factors'] == 'Mood Regulation':
                    template[time_slots] += " combined with breathing exercises for better relaxation."

            elif user_profile['mental_health_goals'] == 'Better focus/mental clarity':
                template[time_slots] = mental_health_activities[1]  # Art therapy or creative expression
                if user_profile['mental_health_factors'] == 'Focus and Attention':
                    template[time_slots] += " followed by a structured planning session to enhance productivity."

            elif user_profile['mental_health_goals'] == 'Improved sleep':
                template[time_slots] = mental_health_activities[2]  # Reading for pleasure
                if user_profile['mental_health_factors'] == 'Energy and Motivation':
                    template[time_slots] += " to relax your mind and prepare for a restful evening."

            else:  # None
                template[time_slots] = social_hobbies[0]  # Coffee with friends
                if user_profile['mental_health_factors'] == 'None':
                    template[time_slots] += ": Casual conversations to uplift your mood."

    if categorize_time_slot(time_slots) == 'Evening':
        # Prioritize based on Physical Health Goals
        if user_profile['physical_health_goals'] == 'Weight loss':
            template[time_slots] = evening_exercise[0]  # Evening walk or light jogging
            if user_profile['physical_health_factors'] == 'Fatigue':
                template[time_slots] += " at a leisurely pace to maintain energy levels."

        elif user_profile['physical_health_goals'] == 'Weight gain':
            template[time_slots] = evening_exercise[1]  # Strength training or HIIT workout
            if user_profile['physical_health_factors'] == 'Mobility Issues':
                template[time_slots] += " with adaptive exercises focusing on upper body strength."

        elif user_profile['physical_health_goals'] == 'Muscle building':
            template[time_slots] = evening_exercise[2]  # Dance classes or aerobic workout
            if user_profile['physical_health_factors'] == 'Chronic Pain':
                template[time_slots] += " ensuring modifications for any discomfort."

        else:  # None
            # Focus on Mental Health Goals
            if user_profile['mental_health_goals'] == 'Stress reduction':
                template[time_slots] = relaxation_activities[0]  # Gentle stretching or yoga
                if user_profile['mental_health_factors'] == 'Stress Management':
                    template[time_slots] += " to help release the day's tension."

            elif user_profile['mental_health_goals'] == 'Better focus/mental clarity':
                template[time_slots] = relaxation_activities[1]  # Meditation or mindfulness practice
                if user_profile['mental_health_factors'] == 'Focus and Attention':
                    template[time_slots] += " followed by a review of your day's achievements to foster clarity."

            elif user_profile['mental_health_goals'] == 'Improved sleep':
                template[time_slots] = relaxation_activities[2]  # Listening to calming music
                if user_profile['mental_health_factors'] == 'Sleep and Rest':
                    template[time_slots] += " before starting your nighttime routine."

            else:  # None
                template[time_slots] = creative_hobbies[0]  # Drawing or sketching
                if user_profile['mental_health_factors'] == 'None':
                    template[time_slots] += ": A creative outlet to unwind before bed."

    if categorize_time_slot(time_slots) == 'Night':
        # Prioritize based on Mental Health Goals
        if user_profile['mental_health_goals'] == 'Improved sleep':
            template[time_slots] = winding_down_activities[1]  # Practicing deep breathing exercises
            if user_profile['mental_health_factors'] == 'Sleep and Rest':
                template[time_slots] += " to ease into a restful state before bed."

        elif user_profile['mental_health_goals'] == 'Stress reduction':
            template[time_slots] = winding_down_activities[0]  # Listening to soothing music
            if user_profile['mental_health_factors'] == 'Mood Regulation':
                template[time_slots] += " while reflecting on positive moments from your day."

        else:  # None
            # Focus on Self-Care Activities
            template[time_slots] = self_care_activities[0]  # Night-time skincare routine
            if user_profile['mental_health_factors'] == 'None':
                template[time_slots] += ": A calming way to signal your body that it's time to wind down."

        # Prioritize based on Physical Health Factors
        if user_profile['physical_health_factors'] == 'Chronic Pain':
            template[time_slots] += " with gentle stretching to alleviate tension before sleep."

        elif user_profile['physical_health_factors'] == 'Fatigue':
            template[time_slots] = light_entertainment[0]  # Watching a relaxing movie
            if user_profile['physical_health_goals'] == 'None':
                template[time_slots] += ": Something enjoyable to help relax your mind."
  myKeys = list(template.keys())
  myKeys.sort()

  # Sorted Dictionary
  sd = {i: template[i] for i in myKeys}
  sd_cleaned = {time_slot: activity for time_slot, activity in sd.items() if activity != 'Flexible Time'}
  return template_initial, sd_cleaned

# Generate a dataset with a specified number of user profiles and their schedules
def create_dataset_with_schedules(num_profiles):
    dataset = []
    for _ in range(num_profiles):
        user_profile = generate_user_profile()
        initial_schedule, modified_schedule = create_target_schedule(user_profile)
        dataset.append({**user_profile, 'user_schedule': initial_schedule,'generated_schedule': modified_schedule})
    
    return pd.DataFrame(dataset)

# Create a dataset with 10000 user profiles and their personalized schedules
user_profiles_df = create_dataset_with_schedules(10000)

# Display the first few rows of the dataset
print(user_profiles_df.head())

# Save the dataset to a CSV file
user_profiles_df.to_csv('user_profiles_with_schedules.csv', index=False)
