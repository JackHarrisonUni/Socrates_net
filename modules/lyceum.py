### Lyceum Log manager fopr socrates.net



# Imports for lyceum
import os
import json
import datetime as dt

# Global vars
module_name = "Lyceum"
module_version = "0.0.2"
author = "ZeroCypher"
module_description = "Lyceum, the  stores of knowleged from time long past."

ARCHIVE_PATH = "Lyceum_Archives"
tail_leng = 10
head_leng = 10

# Functions for lyceum
def global_th_setter(type, num):
    message = f"{type} set to {num}"

    try:
        if type == "-head":
            global head_leng 
            head_leng = num
            
        elif type == "-tail":
            global tail_leng 
            tail_leng = num
        
        else: 
            return {
                "Status": "ERROR",
                "Route": module_name,
                "Message": "Value type not found."
            }
        
        return {
                "Status": "OK",
                "Route": module_name,
                "Message": message
            }
    except Exception as e:
        #throw error
        return

def validate_payload(payload):
    required = ["Route", "From", "Status", "Message", "Time_stamp"]
    return all(k in payload for k in required)

def get_todays_logpath():
    date = dt.datetime.now().strftime("%Y-%m-%d")
    return (f"{ARCHIVE_PATH}/{date}.log")

def save_log(log):
    try:
        file_path = get_todays_logpath()

        if not os.path.exists(ARCHIVE_PATH):
            os.makedirs(ARCHIVE_PATH)
        
        if "Time_stamp" not in log:
            log["Time_stamp"] = dt.datetime.now().isoformat()
            
        with open(file_path, "a") as f:
            f.write(json.dumps(log) + "\n")
            

        return {
            "Status": "OK",
            "Message": f"Log Created {file_path}",
        }
    except Exception as e: 
        return {
            "Status": "ERROR",
            "Message": f"Failed to create log: {e}"
            }

def create_log(data):
    timestamp = dt.datetime.now().isoformat()

    try:
        valid = validate_payload(data)
        if valid:
            # save data here
            response = {
                        "Route": module_name,
                        "Status": "OK",
                        "Logged": True,
                        "Message": "System log updated",
                        "Time_stamp": timestamp,
                        "Meta": data.get("Message",)
                        }
            save_log(data)
            return response
        elif not valid:
            response = {
                "Route": module_name,
                "Status": "ERROR",
                "Logged": False,
                "Message": "Payload not valid",
                "Time_stamp": timestamp
            }
            save_log(response)
            return response
    except Exception as e:
        save_log({
            "Route": module_name,
            "Status": "ERROR",
            "Logged": False,
            "Message": e,
            "Time_stamp": timestamp
        })
        return {
            "Route": module_name,
            "Status": "ERROR",
            "Logged": False,
            "Message": e,
            "Time_stamp": timestamp
        }
    
def main(command):
    try:
        length_command = len(command)
        if length_command == 1:
        #flesh this out
            match command[0]:
                case "-len":
                    #read file and count number of logs
                    save_log({
                        "Route": module_name,
                        "Status": "ERROR",
                        "Message": "Not implemented yet"
                    })
                    return
                case "-tail":
                    # return last tail_leng (defaul 10) commands
                    save_log({
                        "Route": module_name,
                        "Status": "ERROR",
                        "Message": "Not implemented yet"
                    })
                    return
                case "-head":
                    # return first head_leng (defaul 10) commands
                    save_log({
                        "Route": module_name,
                        "Status": "ERROR",
                        "Message": "Not implemented yet"
                    })
                    return
                case "-list":
                    # List entire log 
                    save_log({
                        "Route": module_name,
                        "Status": "ERROR",
                        "Message": "Not implemented yet"
                    })
                    return
                case _:
                    #throw ERROR
                    save_log({
                        "Route": module_name,
                        "Status": "ERROR",
                        "Message": "Malformed/Missing payload"
                    })
                    return
        elif length_command == 2:
            input_type, input_data, = command
            match input_type:
                case "-filter":
                    return
                case _:
                    #throw ERROR
                    save_log({
                        "Route": module_name,
                        "Status": "ERROR",
                        "Message": "Malformed/Missing payload"
                    })
                    return
        elif length_command == 3:
            input_type, input_data, value = command
            match input_type:
                case "-set":
                    types = ["-tail", "-head"]
                    if input_data in types:
                        global_th_setter(input_data, value)
                        
                    else:
                        #throw ERROR
                        save_log({
                        "Route": module_name,
                        "Status": "ERROR",
                        "Message": "Malformed/Missing payload"
                        })
                        return
                case _:
                    #throw ERROR
                    save_log({
                        "Route": module_name,
                        "Status": "ERROR",
                        "Message": "Malformed/Missing payload"
                    })
                    return
        else:
            #throw error 
            save_log({
                "Route": module_name,
                "Status": "ERROR",
                "Message": "Malformed/Missing payload"
            })               
            return
                
    except Exception as e:
        return str(e)

