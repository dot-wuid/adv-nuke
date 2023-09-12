import json
import os

# Function to get user input
def get_user_input():
    input_data = {}
    input_data['name'] = input("Enter value for Name: ")
    input_data['dscacc'] = input("Enter value for Discord Account Name: ")
    input_data['token'] = input("Enter value for Bot Token: ")
    input_data['botname'] = input("Enter value for Bot Name: ")
    input_data['userid'] = input("Auto Update (t/f): ")
    return input_data

# Function to save data to a JSON file
def save_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Define the file path in the Appdata folder
file_path = os.path.expanduser("~/Appdata/local/welcome/nuked_by_dot_wuid.json")

# Get user input
user_data = get_user_input()

# Save user input to JSON file
save_to_json(user_data, file_path)

print(f"Data saved to {file_path}")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("[1] ~ View Config")
print("[2] ~ Keylogger")
print("[3] ~ TOS")
print("[0] ~ Exit")
sub = input(":")
if sub == "1":
    import webbrowser
    webbrowser.open_new_tab(file_path)
if sub == "0":
    print('a')
if sub == "2":
    print("Downloading Keylogger.")
    print("WE DONT RECOMMEND YOU USE THIS...")
    webbrowser.open_new_tab("https://gist.github.com/patilswapnilv/7338783")
elif sub == "3":
    print("Loading Adv-Nuker TOS")
    toshere = """TOS
    Adv Nuker Isnt made To cause any harm to Others,
    We Do Not Support Nuking Servers,
    This Bot is Completely Harmless, And just For Fun."""
    print(toshere)
    a = input(':')
else:
    print("INVAILD")
