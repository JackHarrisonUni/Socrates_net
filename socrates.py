### socrates.py - Main file for Socrates.net
### IMPORTS AND MODULES For Socrates.py
import os
import plato
#import lyceum
#import epictetus
#import other modules as they are developed



### GLOBAL VARIABLES FOR SOCRATES.PY
Ascii_Banner = r"""
  /$$$$$$                                           /$$                            /$$   /$$             /$$    
 /$$__  $$                                         | $$                           | $$$ | $$            | $$    
| $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$   | $$$$| $$  /$$$$$$  /$$$$$$  
|  $$$$$$  /$$__  $$ /$$_____/ /$$__  $$|____  $$|_  $$_/   /$$__  $$ /$$_____/   | $$ $$ $$ /$$__  $$|_  $$_/  
 \____  $$| $$  \ $$| $$      | $$  \__/ /$$$$$$$  | $$    | $$$$$$$$|  $$$$$$    | $$  $$$$| $$$$$$$$  | $$    
 /$$  \ $$| $$  | $$| $$      | $$      /$$__  $$  | $$ /$$| $$_____/ \____  $$   | $$\  $$$| $$_____/  | $$ /$$
|  $$$$$$/|  $$$$$$/|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$$ /$$$$$$$//$$| $$ \  $$|  $$$$$$$  |  $$$$/
 \______/  \______/  \_______/|__/      \_______/   \___/   \_______/|_______/|__/|__/  \__/ \_______/   \___/  
"""

# version = "0.0.1" Skeliton version
# version = "0.0.2" Added plato module interaction
version = "0.0.3" # Added clear command and improved plato module interaction
author = "Socrates"
description = "A modular cybersecurity suite inspired by Philosophy and Logic. " # describe what the socrates suit does

alive = True


### GLOBAL FUNCTIONS FOR SOCRATES.PY
def use_plato(plato_command):
    try:
      input_type, input_data = plato_command.split(" ", 1)
      result = plato.reasoning_engine(input_data, input_type)
      print(f"Reasoning Engine Output: {result}")
    except ValueError:
      print("Invalid command format. Please use -Plato --help for options.")

### BOOT SEQUENCE
print(f"{Ascii_Banner}\n\n\nVersion: {version} | Author: {author}\nDescription: {description}")
while alive:
    command = input("user@socrates: Socrates.net> ")
    if command.lower() in ["exit", "quit", "q"]:
        alive = False
        print("Shutting down Socrates.net...")
    elif command.lower() == "-modules":
        print("Available modules: \n -Plato: Logic and reasoning structures\n -Lyceum: Knowledge store (files/logs)\n -Epictetus: Error handler")
    


    ### MODULE INTERACTIONS
    ### PLATO MODULE 
    elif command.startswith("-Plato"):
        if len(command.split()) != 1:
          if command.split()[1] == "--help" or command.split()[1] == "-h" or command.split()[1] == "-?":
              print(f"Plato Module Help:\n -t \"some text\" : Process text input through reasoning engine\n -p \"file_path\" : Process file path input through reasoning engine")
              continue
          elif len(command.split()) < 3:
              print("Please provide an argument for the Plato module. Type '-Plato --help' for options.")
              continue
          elif len(command.split()) > 3:
              print("Too many arguments provided. Type '-Plato --help' for options.")
              continue
          elif len(command.split()) == 3:
              plato_command = command.split(" ", 1)[1] 
              use_plato(plato_command)
              continue
        else:    
            print(f"Loaded module: {plato.module_name} v{plato.module_version}\nDescription: {plato.module_description}\n\n")
            plato_command = input("user@socrates: Socrates.net/Plato>")
            plato_command = plato_command
            use_plato(plato_command)
            continue
    
    ### LYCEUM MODULE

    ### EPICTETUS MODULE

    ### GENERAL HELP
    elif command.lower() in ["--help", "-h", "-?"]:
        print("Available commands: \n --help/-h/-? : Show this help message\n -exit/quit/q : Exit the program\n -modules : List available modules")
    elif command.lower() in ["clear", "cls"]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Ascii_Banner}\n\n\nVersion: {version} | Author: {author}\nDescription: {description}")
    else:
        print(f"Command '{command}' not recognized. Type 'help' for a list of commands.")

### Future expansions will include loading and interfacing with other modules like Plato, Lyceum, and Epictetus.
