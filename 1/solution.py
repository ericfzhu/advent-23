import re
file_path = 'input.txt'
# Read the file and process each line
with open(file_path, 'r') as file:
    file_lines = file.readlines()
import re

def replace_numbers(s):
    """Replace all substrings of numbers with the digit surrounded by the word."""
    num_words = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    for word, digit in num_words.items():
        s = re.sub(f"{word}", f"{word}{digit}{word}", s)
    return s

def find_first_last_digit(s):
    """Find the first and last digit in the string."""
    digits = re.findall(r'\d', s)
    if digits:
        return int(digits[0]), int(digits[-1])
    return 0, 0

def process_strings(strings):
    """Process each string and sum up the values."""
    total_sum = 0
    for string in strings:
        modified_string = replace_numbers(string)
        first_digit, last_digit = find_first_last_digit(modified_string)
        total_sum += first_digit * 10 + last_digit
    return total_sum

# Example strings
example_strings = [
    "two1nine", "eightwothree", "abcone2threexyz", 
    "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"
]

# Process and calculate the sum
total_sum = process_strings(file_lines)
print(total_sum)
