# Create a dict with: name, age, list of 3 skills, a nested dict (address with city + state)

import json

data = {
    'name':'John Doe',
    'age':30,
    'skills':['Python', 'JavaScript', 'SQL'],
    'address':{
        'city':'New York',
        'state':'NY'
    }
}

# Convert it to JSON string

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

# Convert JSON string back to dict
json_obj = json.loads(json_str)
print(json_obj)
print(type(json_obj))

# Save it to a file

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)


# Read it back and print the result
with open('data.json', 'r') as f:
    data_loaded = json.load(f)
    print(data_loaded)
    print(type(data_loaded))


# Using the same data.json file:

# Load the JSON file
with open('data.json', 'r') as f:
    data_loaded = json.load(f)

# Add a new key:
# "experience": 5
data_loaded['experience'] = 5

with open('data.json', 'w') as f:
    # Save the updated JSON back into the same file
    json.dump(data_loaded, f, indent=4)

# Load again

with open('data.json', 'r') as f:
    # Print the final dictionary
    final_dict = json.load(f)
    print(final_dict)


with open('data.json', 'r') as f:
    data_loaded = json.load(f)

data_loaded['projects'] = [{'title' : 'AI App', 'year' : 2024},
                           {'title' : 'Website', 'year' : 2023}]

with open('data.json', 'w') as f:
    json.dump(data_loaded, f, indent=4)

with open('data.json', 'r') as f:
    data_loaded = json.load(f)
    print(data_loaded)


# Load the JSON

with open('data.json', 'r') as f:
    data_loaded = json.load(f)


# Append "Machine Learning" to the skills list
data_loaded['skills'].append('Machine Learning')
# Save it back
with open('data.json', 'w') as f:
    json.dump(data_loaded, f, indent=4)

# Load again and print
with open('data.json', 'r') as f:
    data_loaded = json.load(f)
    print(data_loaded)