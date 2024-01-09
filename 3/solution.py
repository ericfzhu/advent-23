
import re
file_path = 'input.txt'
# Read the file and process each line
with open(file_path, 'r') as file:
    file_content = file.readlines()

grid = [line.strip() for line in file_content]

# grid_from_file = [line.strip() for line in grid_from_file]

# Function to sum numbers next to symbols
def calculate_gear_ratios_refined(grid):
    # Function to find horizontally adjacent numbers around a cell
    def find_adjacent_numbers(x, y):
        numbers = []
        for dx in [-1, 0, 1]:
            nx = x + dx
            if 0 <= nx < len(grid):
                row = grid[nx]
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    ny = y + dy
                    if 0 <= ny < len(row) and row[ny].isdigit():
                        # Extract the complete number
                        start = ny
                        while start > 0 and row[start - 1].isdigit():
                            start -= 1
                        end = ny
                        while end + 1 < len(row) and row[end + 1].isdigit():
                            end += 1
                        # Add the number if it is not already in the list
                        number = int(row[start:end+1])
                        if number not in numbers:
                            numbers.append(number)
        return numbers

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '*':
                # Find horizontally adjacent numbers
                adjacent_numbers = find_adjacent_numbers(i, j)
                # If exactly two numbers, multiply them and add to total
                if len(adjacent_numbers) == 2:
                    total += adjacent_numbers[0] * adjacent_numbers[1]

    return total


print(calculate_gear_ratios_refined(grid))