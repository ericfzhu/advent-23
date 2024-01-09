# It appears that there is an issue with parsing the seeds section. I will adjust the code to correctly handle the format.

def parse(example):
    # Splitting the example into sections
    sections = example.strip().split("\n\n")
    seeds_section = sections[0].split("\n")[0].split(":")[1].strip()
    seeds = [int(n) for n in seeds_section.split()]

    # Parsing the map sections
    maps = []
    for section in sections[1:]:
        lines = section.strip().split("\n")[1:]
        map_data = []
        for line in lines:
            if line.strip():
                map_data.append(tuple(map(int, line.strip().split())))
        maps.append(map_data)

    return seeds, maps

def convert_numbers(seeds, maps):
    ranges = []
    for i in range(0, len(seeds), 2):
        start, length = seeds[i], seeds[i+1]
        ranges.extend(range(start, start + length))

    for map_data in maps:
        new_ranges = []
        for number in ranges:
            converted = False
            for dest_start, src_start, length in map_data:
                if src_start <= number < src_start + length:
                    new_number = dest_start + (number - src_start)
                    new_ranges.append(new_number)
                    converted = True
                    break
            if not converted:
                new_ranges.append(number)
        ranges = new_ranges

    return min(ranges)

file_path = 'input.txt'

with open(file_path, 'r') as file:
    input_txt = file.read()

# Parse the example and process it
seeds, maps = parse(input_txt)
result = convert_numbers(seeds, maps)
result

