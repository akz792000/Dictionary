import json

# Function to find the missing ID from 1 to 3000
def find_missing_id(ids):
    all_ids = set(range(1, 3001))  # Create a set of all IDs from 1 to 3000
    ids_set = set(ids)  # Convert the list of IDs to a set
    missing_ids = all_ids - ids_set  # Find the missing IDs
    return missing_ids

# Load JSON data
with open('../File_0.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract all IDs from the JSON data
ids = [item['id'] for item in data]

# Find the missing ID(s)
missing_ids = find_missing_id(ids)

# Print the missing ID(s)
print("Missing ID(s):", missing_ids)