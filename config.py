import json
import os

# Function to get user input
def get_user_input():
    input_data = {}
    input_data['name'] = input("Enter value for Name: ")
    input_data['dscacc'] = input("Enter value for Discord Account Name: ")
    input_data['token'] = input("Enter value for Bot Token: ")
    input_data['botname'] = input("Enter value for Bot Name: ")
    input_data['userid'] = input("User ID :")
    return input_data

# Function to save data to a JSON file
def save_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Define the file path in the Documents folder
file_path = os.path.expanduser("~/Appdata/local/AN.json")

# Get user input
user_data = get_user_input()

# Save user input to JSON file
save_to_json(user_data, file_path)

print(f"Data saved to {file_path}")
sub = input(":")
