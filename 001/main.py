import random

def get_input(prompt, options=None):
    """
    Display a prompt to the user and get their input.

    If options are provided, display them as a numbered list and prompt the user to select one.

    Args:
        prompt (str): The prompt message to display to the user.
        options (list of str, optional): A list of options for the user to choose from. Defaults to None.

    Returns:
        str: The user's input or the selected option from the list.
    """
    # If options are provided
    if options:
        print(prompt)
        # List out the options
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        # Ask user which option they choose
        choice = int(input("Select an option: ")) - 1
        # return the options string
        return options[choice]
    else:
        # If no options provided, return whatever user inputs
        return input(prompt)

def generate_workout_routine(goal, level, days, time, equipment, preferences):
    """
    Generate a workout routine based on user inputs.

    Args:
        goal (str): The user's fitness goal (e.g., "Build muscle").
        level (str): The user's fitness level (e.g., "Beginner").
        days (int): The number of days per week the user can work out.
        time (str): The amount of time the user can spend on each workout session.
        equipment (str): The specific equipment the user has access to (e.g., "Dumbbells").
        preferences (str): Any specific preferences or restrictions the user has.

    Returns:
        list of list of str: A list of workout routines for each day.
    """
    exercises = {
        "Build muscle": ["Push-ups", "Pull-ups", "Squats", "Deadlifts", "Bench press", "Bicep curls"],
        "Lose weight": ["Running", "Cycling", "Jump rope", "Burpees", "Mountain climbers"],
        "Increase endurance": ["Running", "Cycling", "Swimming", "Rowing", "Jump rope"],
        "Improve flexibility": ["Yoga", "Stretching", "Pilates", "Tai chi"]
    }

    equipment_exercises = {
        "None": ["Bodyweight squats", "Push-ups", "Lunges", "Planks"],
        "Dumbbells": ["Dumbbell press", "Dumbbell rows", "Dumbbell squats"],
        "Barbell": ["Barbell squats", "Deadlifts", "Barbell rows"],
        "Resistance bands": ["Band pull-aparts", "Band rows", "Band squats"],
        "Kettlebells": ["Kettlebell swings", "Goblet squats", "Kettlebell deadlifts"],
        "Gym access": ["Treadmill", "Elliptical", "Leg press", "Cable machines"]
    }

    routine = []
    for _ in range(days):
        daily_routine = []
        if preferences.lower() != "none":
            daily_routine.append(preferences)
        else:
            daily_routine.append(random.choice(exercises[goal]))
        
        if equipment != "None":
            daily_routine.append(random.choice(equipment_exercises[equipment]))
        else:
            daily_routine.append(random.choice(exercises[goal]))

        routine.append(daily_routine)

    return routine

def main():
    """
    Main function to interact with the user, gather inputs, and generate a customized workout routine.

    Asks the user a series of questions about their fitness goals, level, available workout days, session duration, equipment, and preferences.
    Generates and displays a workout routine based on the user's inputs.
    """
    print("Welcome to the Workout Routine Generator!")
    
    goal = get_input("What is your fitness goal?", ["Build muscle", "Lose weight", "Increase endurance", "Improve flexibility"])
    level = get_input("What is your fitness level?", ["Beginner", "Intermediate", "Advanced"])
    days = int(get_input("How many days per week can you work out?", ["1", "2", "3", "4", "5", "6", "7"]))
    time = get_input("How much time can you spend on each workout session?", ["30 minutes", "45 minutes", "60 minutes", "90 minutes"])
    equipment = get_input("Do you have any specific equipment?", ["None", "Dumbbells", "Barbell", "Resistance bands", "Kettlebells", "Gym access"])
    preferences = get_input("Do you have any specific preferences or restrictions? (e.g., No running, Prefer HIIT, etc.)")
    
    routine = generate_workout_routine(goal, level, days, time, equipment, preferences)
    
    print("\nYour customized workout routine:")
    for i, day_routine in enumerate(routine, 1):
        print(f"Day {i}:")
        for exercise in day_routine:
            print(f" - {exercise}")
        print()

if __name__ == "__main__":
    main()
