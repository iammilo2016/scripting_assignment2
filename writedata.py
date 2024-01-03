import json
import pwd
import grp
import subprocess
import sys

def get_machine_name():     # defines a function named get_machine_name. This function will be used to get the machine name
    return subprocess.getoutput("hostname")

def get_users_and_groups():     # defines a function named get_users_and_groups. This function will be used to get the users and groups on the system
    users = {}
    for p in pwd.getpwall():   # loops through all users on the system
        username = p.pw_name
        groups = [g.gr_name for g in grp.getgrall() if username in g.gr_mem] # loops through all groups on the system and checks if the user is a member of the group
        users[username] = groups
    return users

def get_cpuinfo(): # defines a function named get_cpuinfo. This function will be used to get the CPU information on the system
    with open("/proc/cpuinfo", "r") as f:
        lines = f.readlines()
    cpuinfo = {}    # initializes an empty dictionary
    for line in lines: # loops through each line in the file
        if "vendor_id" in line or "model name" in line or "cache size" in line:
            key, value = line.split(":")
            cpuinfo[key.strip()] = value.strip()
    return cpuinfo

def get_services_status():  # defines a function named get_services_status. This function will be used to get the status of all services on the system
    output = subprocess.getoutput("systemctl list-units --type=service") # runs the shell command systemctl list-units --type=service
    services = {}   #  initializes an empty dictionary 
    for line in output.split("\n")[1:]: # splits the output string into lines, skips the first line
        parts = line.split()
        if len(parts) > 4:
            services[parts[0]] = parts[3]
    return services

def write_data_to_file(): #write the collected system information to a file.
    data = {                                                 #get data from the functions defined above and store it in a dictionary
        "Machine Name": get_machine_name(),
        "Users and Groups": get_users_and_groups(),
        "CPU Info": get_cpuinfo(),
        "Services Status": get_services_status()
    }

    try:                                    #error handling
        with open("Project_2.json", "w") as f:
            json.dump(data, f, indent=4)        #writes the data dictionary to the file in JSON format
        print("----------System Inforamtion is wrriten to Project_2.json successfully!!!------------")    
    except Exception as e:
        print(f"Error writing data to file: {e}", file=sys.stderr)

def main():
    write_data_to_file()

if __name__ == "__main__":
    main()
