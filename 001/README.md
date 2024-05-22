# CLI Workout Routine Generator

This is a Python program that generates a customized workout routine based on user inputs.

## Features

- Generates workout routines tailored to different fitness goals
- Supports various fitness levels and available equipment
- Customizable based on user preferences and restrictions

## Prerequisites

- Python installed on your computer. You can download and install Python from [python.org](https://www.python.org/).

## How to Run the Program

1. **Clone the Repository or Download the Script**
   - Clone this repository or download the `workout_routine_generator.py` file to your local machine.

2. **Open a Terminal or Command Prompt**
   - Depending on your operating system:
     - **Windows**: Open Command Prompt or PowerShell.
     - **Mac/Linux**: Open Terminal.

3. **Navigate to the Directory Containing Your Python File**
   - Use the `cd` command to change the directory to where you saved the Python file. For example:
     ```sh
     cd path/to/your/directory
     ```

4. **Run the Program**
   - Run the Python script by typing:
     ```sh
     python workout_routine_generator.py
     ```
   - If you are using Python 3 and the above command doesn't work, try:
     ```sh
     python3 workout_routine_generator.py
     ```

## Example Interaction

When you run the program, it will ask you a series of questions. Here is an example of how the interaction might look:

```
Welcome to the Workout Routine Generator!

What is your fitness goal?

    Build muscle
    Lose weight
    Increase endurance
    Improve flexibility
    Select an option: 1

What is your fitness level?

    Beginner
    Intermediate
    Advanced
    Select an option: 2

How many days per week can you work out?

    1
    2
    3
    4
    5
    6
    7
    Select an option: 3

How much time can you spend on each workout session?

    30 minutes
    45 minutes
    60 minutes
    90 minutes
    Select an option: 3

Do you have any specific equipment?

    None
    Dumbbells
    Barbell
    Resistance bands
    Kettlebells
    Gym access
    Select an option: 2

Do you have any specific preferences or restrictions? (e.g., No running, Prefer HIIT, etc.)
Type your preferences or restrictions: None

Your customized workout routine:
Day 1:

    Push-ups
    Dumbbell press

Day 2:

    Pull-ups
    Dumbbell rows

Day 3:

    Squats
    Dumbbell squats

```


## Troubleshooting

- **Python not recognized**: If you get an error saying `python is not recognized as an internal or external command`, you may need to add Python to your system PATH or use `python3` instead of `python`.
- **Indentation Errors**: Ensure that the code is copied correctly with the right indentation, as Python is indentation-sensitive.
- **SyntaxError**: If you encounter a `SyntaxError`, check the following:
  - Ensure the code is copied correctly without missing any lines.
  - Make sure you are using a compatible Python version (preferably Python 3).
  - Verify that there are no typos or extraneous characters in the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.
