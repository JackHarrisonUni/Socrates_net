### socrates.py - Main file for Socrates.net
### IMPORTS AND MODULES For Socrates.py
import os
import sys
import datetime
import random
import shlex
import horai

#import lyceum
#import epictetus
#import other modules as they are developed



### GLOBAL VARIABLES FOR SOCRATES.PY
module_name = "Socrates"
# version = "0.0.1" Skeliton version
# version = "0.0.2" Added plato module interaction
version = "0.0.3" # Added clear command and improved plato module interaction
author = "Socrates"
description = "A modular cybersecurity suite inspired by Philosophy and Logic. " # describe what the socrates suit does

alive = True
signature = f"Socrates v{version}"
helpMessage =  """
Available commands:
--help/-h/-? : Show this help message
-exit/quit/q/Ctrl C : Exit the program
clear/cls : Clear and reload banner
-modules : List available modules
"""

DEV_BOOT = "--dev-boot" in sys.argv      




### GLOBAL FUNCTIONS FOR SOCRATES.PY
def load_banner():
    Ascii_Banner_path = (random.choice(
        ["Ascii_Banners/Socrates/Socrates_Banner0.txt",
        "Ascii_Banners/Socrates/Socrates_Banner1.txt",]
        ))
    
    with open(Ascii_Banner_path, 'r') as f:
        Ascii_Banner = f.read()
        return Ascii_Banner
    
def shutdown_Socrates():
    global alive
    alive = False
    print("Shutting down Socrates.net...")

def tokenize_command(command): ### For Piping and Redirecting
    try:
        tokens = shlex.split(command)
        return tokens
    except ValueError as e:
        print(f"Error tokenizing command: {e}")
        return False



### Commands for Socrates
def send_to_Horai(info):
    return horai.the_gates(info)

def dev_boot():
    print(f"[{module_name}] Developer boot initiated - Contacting Horai")
    try:
        horai.dev_link()
        print(f"[{module_name}] Horai Acknowledged. Developer link activaed.")
    except Exception as e:
        print(f"[{module_name}] Developer boot failed: {e}")

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
    Ascii_Banner = load_banner()
    print(f"{Ascii_Banner}\n\n\nVersion: {version} | Author: {author}\nDescription: {description}")

def help_command():
    print(helpMessage)


### BOOT SEQUENCE
Ascii_Banner = load_banner()
### HORAI MODULE INITIALIZATION
### horai is silently loaded for now as it will handle flow management and security in the future

print(f"{Ascii_Banner}\n\n\nVersion: {version} | Author: {author}\nDescription: {description}")
while alive:
    try:
        command = input("user@socrates: Socrates.net> ")
        timestamp = datetime.datetime.now()
        tokens = tokenize_command(command)
        source = signature
        raw = command
        stdin = []
        meta = {}

        if tokens:
            if tokens[0] in ["--help", "-h", "?"]:
                help_command()
                continue

            elif tokens[0] in ["-exit", "exit", "quit", "q"]:
                shutdown_Socrates()

            elif tokens[0] in ["clear", "cls"]:
                clearConsole()
                continue

            elif tokens[0] == "--dev-boot":
                dev_boot()
            
            else:
                envelope = {
                    "Source": source,
                    "Raw": raw,
                    "Token": tokens,
                    "Time_stamp": timestamp,
                    "Stdin": stdin,
                    "Meta": meta
                } 

                response = send_to_Horai(envelope)
                if response:
                    print(f"[{module_name}] response :{response}")
           

    except KeyboardInterrupt:
        shutdown_Socrates()


### END OF SOCRATES.PY
