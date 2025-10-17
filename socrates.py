### socrates.py - Main file for Socrates.net
### IMPORTS AND MODULES For Socrates.py
import os
import random
import shlex
import plato
#import lyceum
#import epictetus
#import other modules as they are developed



### GLOBAL VARIABLES FOR SOCRATES.PY
def load_banner():
    Ascii_Banner_path = (random.choice(["Ascii_Banners/Socrates/Socrates_Banner0.txt",
                                    "Ascii_Banners/Socrates/Socrates_Banner1.txt",]))
    with open(Ascii_Banner_path, 'r') as f:
        Ascii_Banner = f.read()
        return Ascii_Banner

# version = "0.0.1" Skeliton version
# version = "0.0.2" Added plato module interaction
version = "0.0.3" # Added clear command and improved plato module interaction
author = "Socrates"
description = "A modular cybersecurity suite inspired by Philosophy and Logic. " # describe what the socrates suit does
 
alive = True



### GLOBAL FUNCTIONS FOR SOCRATES.PY
def Shutdown_Socrates():
    global alive
    alive = False
    print("Shutting down Socrates.net...")

def use_plato(plato_command):
    try:
      input_type, input_data = plato_command.split(" ", 1)
      result = plato.reasoning_engine(input_data, input_type)
      print(f"Reasoning Engine Output: {result}")
    except ValueError:
      print("Invalid command format. Please use -Plato --help for options.")

### BOOT SEQUENCE
Ascii_Banner = load_banner()
print(f"{Ascii_Banner}\n\n\nVersion: {version} | Author: {author}\nDescription: {description}")
while alive:
    try:
      command = input("user@socrates: Socrates.net> ")
      if command.lower() in ["exit", "quit", "q"]:
          Shutdown_Socrates()

      elif command.lower() == "-modules":
          print("Available modules: \n -Plato: Logic and reasoning structures\n -Lyceum: Knowledge store (files/logs)\n -Epictetus: Error handler")
          continue
      
      ### MODULE INTERACTIONS
      ### PLATO MODULE 
      elif command.startswith("-Plato"):
          if len(shlex.split(command)) != 1:
            if shlex.split(command)[1] == "--help" or shlex.split(command)[1] == "-h" or shlex.split(command)[1] == "-?":
                print(plato.plato_help)
                continue
            elif len(shlex.split(command)) < 3:
                print("Please provide an argument for the Plato module. Type '-Plato --help' for options.")
                continue
            elif len(shlex.split(command)) > 3 and shlex.split(command) not in ["|", ">>", ">"]:
                print("Too many arguments provided. Type '-Plato --help' for options.")
                continue
            elif len(shlex.split(command)) == 3:
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
          print("Available commands: \n --help/-h/-? : Show this help message\n -exit/quit/q/Ctrl C : Exit the program\n -modules : List available modules")
      
      elif command.lower() in ["clear", "cls"]:
          os.system('cls' if os.name == 'nt' else 'clear')
          Ascii_Banner = load_banner()
          print(f"{Ascii_Banner}\n\n\nVersion: {version} | Author: {author}\nDescription: {description}")

      elif command. split() in ["|", ">>", ">"]:
          print("Piping and redirection not yet implemented. Please try again later.")
          continue
      
      else:
          print(f"Command '{command}' not recognized. Type 'help' for a list of commands.")
    except KeyboardInterrupt:
      Shutdown_Socrates()

### Future expansions will include loading and interfacing with other modules like Plato, Lyceum, and Epictetus.


### TESTING AREA
# use_plato('-t "Is this a question?"')
# use_plato('-p "/path/to/file.txt"')
# use_plato('-x "Invalid command"')
# use_plato('-Plato --help')
# use_plato('-Plato -h')
# use_plato('-Plato -?')
# use_plato('-Plato -t "What is the meaning of life?"')
# use_plato('-Plato -p "/invalid/path"')
# use_plato('-Plato -x "Invalid command"')


### END OF SOCRATES.PY
