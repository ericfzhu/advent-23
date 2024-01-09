
import re
file_path = 'input.txt'
with open(file_path, 'r') as file:
    input_cards = file.readlines()

# Removing any trailing whitespace or newlines
input_cards = [card.strip() for card in input_cards]

# Process the input cards
total_input_cards = 0
input_copies = [1] * len(input_cards)

def count_matching_numbers(card):
    left, right = card.split('|')
    left_numbers = set(left.split())
    right_numbers = set(right.split())
    return len(left_numbers.intersection(right_numbers))

for i in range(len(input_cards)):
    matches = count_matching_numbers(input_cards[i])
    total_input_cards += input_copies[i]  # Add the number of copies of the current card
    # Update the number of copies for the next y cards
    for j in range(i+1, min(i+1+matches, len(input_cards))):
        input_copies[j] += input_copies[i]

print(total_input_cards)
