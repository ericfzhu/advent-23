import re

# Function to convert numbers in word form to digits
def word_to_digit(text):
    word_to_num = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    for word, num in word_to_num.items():
        text = re.sub(r'\b' + word + r'\b', num, text, flags=re.IGNORECASE)
    return text

# Function to process each line of the file
def process_line(line):
    # Replace words with digits
    line = word_to_digit(line)

    # Find all single digit numbers
    numbers = re.findall(r'\b\d\b', line)

    if numbers:
        # Take the first and last number and concatenate them
        return int(numbers[0] + numbers[-1])
    else:
        return 0

# Read the file and process each line
def process_file(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            total += process_line(line)
    return total

# File path
file_path = '1/input.txt'

# Process the file
print(process_file(file_path))