### Horai.py - flow management for Socrates.net
### IMPORTS AND MODULES For Horai.py
import time
import plato 
import shlex
#import other modules as they are developed

### Global Variables for Horai.py
module_name = "Horai"
module_version = "0.0.1"
module_description = "flow management module for Socrates.net"

valid_source = ["Socrates", "Plato"]
valid_entrypoint = ["exit", "quit", "q", "clear", "cls", "--help", "-h", "-?", # General Commands
                    "-Plato" # Module Commands
                    ]

general_comands = ["exit", "quit", "q", "clear", "cls", "--help", "-h", "-?"]
module_commands = ["-Plato"]
pipping_commands = ["|", ">", ">>"]

### Functions For Horai.py
def task_queue_manager():
    pass  # Placeholder for future implementation of task queue management

def use_plato(plato_command):
    try:
        input_type, input_data = plato_command.split(" ", 1)
        print("Sending input data through reasoning engine...")
        result = plato.reasoning_engine(input_data, input_type)
        print(f"Reasoning Engine Output: {result}")
    except ValueError:
        print("Invalid command format. Please use -Plato --help for options.")

def process_command(info):
    try:
        command = info.raw
        tokens = shlex.split(command)
        if tokens[0] == "-Plato":
            if tokens[1] == "--help" or tokens[1] == "-h" or tokens[1] == "-?":
                print(plato.plato_help)
                
            elif len(tokens) < 3:
                print("Please provide an argument for the Plato module. Type '-Plato --help' for options.")
                

            elif len(tokens) > 3 and tokens[3] not in ["|", ">>", ">"]: ### check if the output of this needs to be redirected or printed out
                print("Too many arguments provided. Type '-Plato --help' for options.")
                

            elif len(tokens) == 3:
                plato_command = command.split(" ", 1)[1] 
                use_plato(plato_command)

        else:
            return print(f"Command '{command}' not recognized. Type 'help' for a list of commands.")
    except Exception as e:
        return e

                




### Main Flow Management Logic
def the_gates(info):
    invalid_response ={"Route": "Socrates", "Status": "Invalid"}
    source = info.Source
    raw = info.Raw
    token = info.Token
    time_stamp = info.Time_stamp
    stdin = info.Stdin
    
    if source in valid_source:
        if len(token) == 0:
            return invalid_response
        elif len(token) == 1 and token[0] not in general_comands:
            return invalid_response
        elif len(token) == 3 and token[0] not in module_commands:
            return invalid_response
        elif len(token) > 3 and token not in pipping_commands:
            return invalid_response 
        elif len(token) > 3 and token[3] in pipping_commands:
            return invalid_response #for now invalid until fixed
        else:
            return
            
        

    
    module = "Socrates"
    return {"Route": module, "Status": "Invalid"}

