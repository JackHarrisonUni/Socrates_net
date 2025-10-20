# Horai.py - flow management and zero-trust gatekeeper for Socrates.net

# Rsponasbility (High-Level):
#   - Accept initional REGISTER request from modules.
#   - Issue OlympusChallenge Object (challeng ID + Token)
#   - Verify module proofs and issue short-lived session tokens (session id + scope + expiry)
#   - Maintain an in-memory registery of active session tokens.
#   - Enforce session rules: per-command key rotation, scope enforment, revokation, lyceum logging
#   - Opperate in PARANOID mode: scilently drop unregistered callers; verbose resons only in --dev mode


### IMPORTS AND MODULES For Horai.py
import plato 
import shlex
#import other modules as they are developed

### Global Variables for Horai.py
module_name = "Horai"
module_version = "0.0.1"
module_description = "flow management module for Socrates.net"
blacklist = {} # in memory blacklist for use by Horai only
registry = {}
TRUST_INIT = 0.0
TRUST_MAX = 1.0
TRUST_MIN = -1.0
TRUST_MINOR = -0.05
TRUST_MAJOR = -0.15
BLACKLIST_FLOOR = TRUST_MIN

### handshake request variables

### Request Variables
handshake_fields = ["Module_Name", "Module_Role", "Intent", "Duration", "OlympusKey_Request"]
allowed_intents = ["read-only", "read-write"]
allowed_duration = ["temporary", "persistent"]

valid_source = ["Socrates", "Plato"]
valid_entrypoint = ["exit", "quit", "q", "clear", "cls", "--help", "-h", "-?", # General Commands
                    "-Plato"] # Module Commands

transient_challenges = {} #challenge_id -> {challenge obj}

general_comands = ["exit", "quit", "q", "clear", "cls", "--help", "-h", "-?"]
module_commands = ["-Plato"]
pipping_commands = ["|", ">", ">>"]

### Functions For Horai.py
def handle_register(request):

    length = len(handshake_fields)
    ### KILL
    if request["Module_Name"] in blacklist:
        #log failure
        return
    if request["Module_Name"] in registry:
        registry[module_name]["Trust"] += TRUST_MINOR
        # handel request if stuff
        return
    

    for field in request.keys():
        if field not in handshake_fields:
            #log failure
            return
    if len(request) < length:
        #log failure
        return
    elif len(request) > length:
        #log failure
        return
    
    for required in handshake_fields:
        if required not in request:
            #log failure
            return
     
    ### DEEPER CHECK   
    if len(request) == length:
        #main loop for request validation
        for field, value in request.items():

            if field in handshake_fields:
                match field:
                    case "Module_Name":
                        if value not in valid_source:
                            #log failure
                            return
                        continue

                    case "Module_Role":
                        
                        continue

                    case "Intent":
                        if value not in allowed_intents:
                            #log failure
                            return
                        continue

                    case "Duration":
                        if value not in allowed_duration:
                            #log failure
                            return
                        continue

                    case "OlympusKey_Request":
                        if not value:
                            #log failure
                            return
                        continue
            else:
                # log failure
                return
    else:
        #log failure
        return

    ### Validity check on module
    return issue_challenge(request)

def issue_challenge(request):
    # give challenge
    ### HORAI ENTRY POINT
    # check trust, blacklist, intent, etc
    return _mint_olympus_challenge()

def verify_challenge(request):
    challenged_module_name = request.module
    provided_proof = request.proof

    if challenged_module_name not in transient_challenges:
        #log failure
        return
    
    issued_challenge = transient_challenges[challenged_module_name]
    if provided_proof != issued_challenge.proof:
        #remove some trust value from module
        #log failure
        return

    del transient_challenges[challenged_module_name]
    
    BL = blacklist[challenged_module_name]
    if BL and BL != 0:
        trust = BL * TRUST_MINOR
    else:
        trust = TRUST_INIT

    registry[challenged_module_name] = {"Trust": trust, }
    return

def _mint_olympus_challenge():
    #
    pass



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
    source = info["Source"]
    raw = info["Raw"]
    token = info["Token"]
    time_stamp = info["Time_stamp"]
    stdin = info["Stdin"]
    
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




### TODO add blacklist functionality with lyceum audit record 