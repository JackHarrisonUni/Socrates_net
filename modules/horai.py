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
import plato as p 
import lyceum as l
import hermes as h
import shlex
import datetime as dt

#import other modules as they are developed

### Global Variables for Horai.py
module_name = "Horai"
# module_version = "0.0.2"
module_version = "0.0.3" # stable logging pipeline
# module_version = "0.0.4" pipping for commands enabled
# module_version = "0.0.5" basic level security functionality for traffic
# module version = "1.0.0" security for tarffic and hacndshakes with encyrption for sensative network data
module_description = "Horai the gate gaurd to olympus. She will validate all commands and destroy those that do not live up to her standards"

### handshake request variables

### Request Variables

module_commands = ["-Plato", "-Lyceum", "-Hermes"]
pipping_commands = ["|", ">", ">>"]

### Functions For Horai.py

### CHANGE THE PRINT LINES TO Lyceum LOGS
#   LyceumLog = {
#       "Route": module 
#       "Status": status_code
#       "TimeStamp": datetime
#       "Message": message
#   }


def log_lyceum(data):
    try:
        response = l.create_log(data)
        return (response)
    except Exception as e:
        return {
            "Route": module_name,
            "From": "Lyceum",
            "Status": "ERROR",
            "Message": f"Cannot connect to Lyceum: {e}"
        }
    
def use_plato(plato_command): 
    try:
        input_type, input_data = plato_command
        result = p.reasoning_engine(input_data, input_type)
        return result
    except ValueError:
        l.create_log()
        return 

def use_lyceum(lyceum_command):
    try:
        l.main(lyceum_command)
        return
    except Exception as e:
        return e

def process_command(payload):
    try:
        token = payload.get("Token",)[1:]
        command = payload.get("Raw")

        ### ROUTING
        first = shlex.split(command)[0]
        if first == "-Plato":
            ### Route to plato
            try: 
                result = use_plato(token)
                if isinstance(result, dict):
                    log = {
                        "Route": module_name,
                        "From": "Plato",
                        "Status": result.get("Status", "OK"),
                        "Time_Stamp": dt.datetime.now()
                    }
                    wrapped = {
                        "Route": module_name,
                        "From": "Plato",
                        "Status": result.get("Status", "OK"),
                        "Message": result.get("Result", ""),
                        "Meta": result.get("Meta", {})
                    }
                else:
                    log = {
                        "Route": module_name,
                        "From": "Plato",
                        "Status": "OK",
                        "Time_Stamp": dt.datetime.now()
                    }
                    wrapped = {
                        "Route": module_name,
                        "From": "Plato",
                        "Status": "OK",
                        "Message": str(result),
                    }
                return {
                    "Log":log,
                    "Wrapped": wrapped
                    }
            
            except Exception as e:
                log_lyceum( {
                        "Route": module_name,
                        "From": "Plato",
                        "Status": "ERROR",
                        "Time_Stamp": dt.datetime.now()
                    })
                return {
                    "Route": "Plato",
                    "Status": "ERROR",
                    "Message": f"Failed to route: {e}"
                }
        
        elif first == "-Hermes":
            try:
                response = h.start_hermes()
                
                log = {
                    "Route": module_name,
                    "From": "Hermes",
                    "Status": response.get("Status", "OK"),
                    "Time_Stamp": dt.datetime.now()
                }
                wrapped = {
                    "Route": module_name,
                    "From": "Hermes",
                    "Status": "OK",
                    "Message": f"{response.get("Result")}"
                }
                return {
                    "Log": log, 
                    "Wrapped": wrapped
                }
            
            except Exception as e:
                
                return {
                    "Route": "Hermes",
                    "Status": "Error",
                    "Message": f"Failed to route: {e}"
                }

        elif first == "-Lyceum":
            try:
                use_lyceum(token)
                log_lyceum({
                    "Route": module_name,
                    "From": "Lyceum",
                    "Status": "OK",
                    "Time_Stamp": dt.datetime.now()
                })
                return {
                    "Route": "Lyceum",
                    "Status": "OK",
                    "Message": "Command routed to Lyceum"
                }
            except Exception as e:
                log_lyceum({
                    "Route": module_name,
                    "From": "Lyceum",
                    "Status": "ERROR",
                    "Time_Stamp": dt.datetime.now()
                })
                return {
                    "Route": "Lyceum",
                    "Status": "ERROR",
                    "Message": f"Failed to route: {e}"
                }

        elif first.startswith("-"):
            log_lyceum({
                    "Route": module_name,
                    "From": module_name,
                    "Status": "ERROR",
                    "Time_Stamp": dt.datetime.now()
                })
            return{
                "Route": module_name,
                "Status": "ERROR",
                "Message": f"No Module found for command {first}"
            }
        

        else:
            return {
                "Route": module_name,
                "Status": "OK",
                "Message": f"Echo from {module_name}: {command}"
            }

    except Exception as e:
        log_lyceum({
                    "Route": module_name,
                    "From": module_name,
                    "Status": "ERROR",
                    "Time_Stamp": dt.datetime.now()
                })
        return {
            "Route": module_name,
            "Status": "ERROR",
            "Message": str(e)
        }

def dev_link():
    log_lyceum({
                    "Route": module_name,
                    "From": "DEV",
                    "Status": "OK",
                    "Time_Stamp": dt.datetime.now()
                })
                
def validate_payload(payload):
    required = ["Source", "Raw", "Token"]
    return all(k in payload for k in required)

def normalize_tokens(tokens):
    if not tokens: return []
    cleaned = [t.strip() for t in tokens if t and t.strip()]
    return cleaned

def recived_from_module(data):
    try:
        if data.get("Route") == "Lyceum":
            return {
                "Status": "OK",
                "Message": "Lyceum message ignored to prevent recursion"
            }
        
        response = l.save_log(data)
        return response
    
    except Exception as e:
         return {
            "Status": "ERROR",
            "Route": "Horai",
            "Message": f"Failed to process module data: {e}"
        }

### Main Flow Management Logic
def the_gates(payload):

    if not validate_payload(payload):
        log_lyceum({
                    "Route": module_name,
                    "From": module_name,
                    "Status": "ERROR",
                    "Time_Stamp": dt.datetime.now()
                })
        return {
            "Route": module_name,
            "Status": "ERROR",
            "Message": "Malformed payload"
        }
    
    token = normalize_tokens(payload.get("Token", []))
    if not token:
        log_lyceum({
                    "Route": module_name,
                    "From": module_name,
                    "Status": "ERROR",
                    "Time_Stamp": dt.datetime.now()
                })
        return {
            "Route": module_name,
            "Status": "ERROR",
            "Message": "Empty or invalid args"
        }
    

    response = process_command(payload)

    if all(response in ["Log", "Wrapped"]):
        return response.get("Wrapped")
    else:
        return response
    

### TODO add blacklist functionality with lyceum audit record 