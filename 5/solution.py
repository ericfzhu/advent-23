def parse_input(input_text):
    lines = input_text.strip().split('\n')
    seeds = []
    maps = []
    current_map = None

    # Parsing the input
    for line in lines:
        if line.startswith("seeds:"):
            # Parse seeds
            seed_values = line.split()[1:]
            for i in range(0, len(seed_values), 2):
                start = int(seed_values[i])
                length = int(seed_values[i + 1])
                seeds.extend(range(start, start + length))
        elif line.endswith("map:"):
            # Start a new map
            if current_map is not None:
                maps.append(current_map)
            current_map = []
        else:
            # Parse map lines
            map_values = list(map(int, line.split()))
            if map_values:
                current_map.append(map_values)

    # Add the last map
    if current_map is not None:
        maps.append(current_map)

    return seeds, maps

def apply_maps(seeds, maps):
    for map_ in maps:
        new_seeds = []
        for seed in seeds:
            mapped = False
            for x, y, z in map_:
                if y <= seed < y + z:
                    new_seeds.append(x + (seed - y))
                    mapped = True
                    break
            if not mapped:
                new_seeds.append(seed)
        seeds = new_seeds
    return seeds



file_path = '5/input.txt'
with open(file_path, 'r') as file:
    input_text = file.read()

seeds, maps = parse_input(input_text)
final_locations = apply_maps(seeds, maps)

# Finding the lowest location
lowest_location = min(final_locations)
print(lowest_location)