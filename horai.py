# Horai.py - flow management and zero-trust gatekeeper for Socrates.net

# Rsponasbility (High-Level):
#   - Accept initional REGISTER request from modules.
#   - Issue OlympusChallenge Object (challeng ID + Token)
#   - Verify module proofs and issue short-lived session tokens (session id + scope + expiry)
#   - Maintain an in-memory registery of active session tokens.
#   - Enforce session rules: per-command key rotation, scope enforment, revokation, lyceum logging
#   - Opperate in PARANOID mode: scilently drop unregistered callers; verbose resons only in --dev mode


#   - YOU GOT DISTRACTED WITH SEC STUFF SO YOU DELETED IT ALL AND NOW YOU ARE FOCUSED ONLY ON LOGIC FOR NOW


### IMPORTS AND MODULES For Horai.py
import plato 
import shlex
#import other modules as they are developed

### Global Variables for Horai.py
module_name = "Horai"
module_version = "0.0.2"
module_description = "flow management module for Socrates.net"

### handshake request variables

### Request Variables

general_comands = ["exit", "quit", "q", "clear", "cls", "--help", "-h", "-?"]
module_commands = ["-Plato"]
pipping_commands = ["|", ">", ">>"]

# ### Functions For Horai.py



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
        command = info["Raw"]
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


def dev_link():
    print(f"[{module_name}] Running in devloper link mode")
    test_message = {"Type": "DEV_REGISTER", "Message": "Hello developer"}
    print(f"[{module_name}] Sent handshake: {test_message}")
                




### Main Flow Management Logic
def the_gates(envelope):
    """
    envelope = {
        "Source": source,
        "Raw": raw,
        "Token": tokens,
        "Time_stamp": timestamp,
        "Stdin": stdin,
        "Meta": meta
        } 
    """

    ### temp dev code for horai entry point
    command = envelope.get("Raw", "")
    print(f"[{module_name}] Command recived: {command}")

    response = {
        "Route", module_name,
        "Status", "Ok",
        "Message", f"Echo from {module_name}: {command}"
    }

    return response
    






### TODO add blacklist functionality with lyceum audit record 