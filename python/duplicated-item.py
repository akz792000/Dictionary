import json
from collections import defaultdict

# Function to read and parse the JSON file
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Function to find and print IDs of duplicated "de" values
def find_duplicates(data):
    de_dict = defaultdict(list)

    # Iterate over each item and store IDs based on "de" value
    for item in data:
        de_dict[item['de']].append(item['id'])

    # Print IDs that have duplicated "de" values
    for de_value, ids in de_dict.items():
        if len(ids) > 1:
            print(f'Duplicated "de" value: {de_value}')
            print(f'IDs: {ids}\n')

# Path to your JSON file
file_path = '../File_2.json'

# Read and parse the JSON file
data = read_json_file(file_path)

# Find and print IDs of duplicated "de" values
find_duplicates(data)