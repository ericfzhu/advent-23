
import re
file_path = 'input.txt'
# Read the file and process each line
with open(file_path, 'r') as file:
    file_lines = file.readlines()

# Parsing the file content and calculating the minimum number of each color required for each game

def parse_game_data(game_data):
    """
    Parses a line of game data and returns the minimum number of each color required.

    Args:
    game_data (str): A string containing color and number pairs separated by commas and semicolons.

    Returns:
    dict: A dictionary with colors as keys and their minimum required numbers as values.
    """
    color_counts = {}
    combinations = game_data.split(';')
    
    for combo in combinations:
        colors = combo.split(',')
        for color in colors:
            number, color_name = color.strip().split()
            number = int(number)

            if color_name not in color_counts:
                color_counts[color_name] = number
            else:
                color_counts[color_name] = max(color_counts[color_name], number)

    return color_counts

def calculate_power(color_counts):
    """
    Calculates the power of a set of cubes, which is the product of the numbers of red, green, and blue cubes.

    Args:
    color_counts (dict): A dictionary with colors as keys and their numbers as values.

    Returns:
    int: The product of the numbers of red, green, and blue cubes.
    """
    power = 1
    for color in ['red', 'green', 'blue']:
        power *= color_counts.get(color, 1)
    return power

# Process each game and calculate the total sum
total_power = 0

for line in file_lines:
    game_data = line.split(':')[1].strip()  # Extracting the part of the line after 'Game x:'
    color_counts = parse_game_data(game_data)
    game_power = calculate_power(color_counts)
    total_power += game_power

total_power

print(total_power)