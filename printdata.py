import json

def print_data():
    """
    Prints machine name, users and groups, CPU info, and services status
    from a JSON file named 'Project_2.json'.
    """
    try:        # Try to open the JSON file and load the data
        with open("Project_2.json", "r") as json_file: # Open the JSON file
            data = json.load(json_file)
    except FileNotFoundError:   # If the file is not found, print an error
        print("Error: JSON file not found.")
        return

    print(f"Machine Name: {data['Machine Name']}\n")  # Print the machine name
    print("Users and Groups:") # Print the users and groups
    for user, groups in data["Users and Groups"].items():   # loop to Print each user
        print(f"{'':<5}{user}: {', '.join(groups)}")    

    print("\nCPU Info:")
    for key, value in data["CPU Info"].items():     # Print the CPU info
        print(f"{'':<5}{key}: {value}")

    print("\nServices Status:")
    for service, status in data["Services Status"].items(): # Print the services status
        print(f"{'':<5}{service}: {status}")

print_data()
