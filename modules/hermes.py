### Hermes packet and message scanner
disclamer="""
DISCLAMER: 
Only scan authorised targets. The creator of this tool has no legal or ethical responsability to how you use this tool.
"""
### Imports
import shlex
import modules.horai as h

### Global variables
module_name = "Hermes"
module_version = "0.0.1"
author = "ZeroCypher"
module_description = "This is Hermes the messanger of the gods. He checks the network packets and scans targets."

scan_types = ["-s"]


# functions
def verify():
    #this will call horai and register with it 
    return

def validate_types(types):
    return all(k in types for k in scan_types)

def validate_host(host):
    host_parts = host.split(".")
    if host_parts > 4:
        return False
    for i in host_parts:
        try:
            part = int(host_parts[i])
            if part > 255 or part < 0:
                return False
        except Exception:
            return False
    return True # this needs to be implimented properly by checking host against a regex

def start_hermes(command):
    print(disclamer)
    if not command:
        return{
            "Route": module_name,
            "Status": "ERROR",
            "Message": "No command."
        }
    
    first = command[0]
    match first:
        case "-Scan":
            scan_target(command[1], command[1:])
        case _:
            return {
                "Route": module_name,
                "Status": "Error",
                "Message": "Command not found."
            }
        
    return {
        "Route": module_name,
        "Status": "OK",
        "Message": "Up and running ..."
    }

def scan_target(types, target):
    try:
        target = target.strip()
        if target == "":
            print("ERROR")
            return {
                "Route": module_name,
                "Status": "ERROR",
                "Message": "No target given.",
            }
        
        host, sep, port = target.partition(":")
        if host and port:
            if host.count(":") > 1 or port.startswith(":"):
                print("IPv6 not supported in v0.0.1")
                return {"Route": module_name, "Status": "ERROR", "Message": "IPv6 not supported in v0.0.1"}
            
        elif host and sep and not port:
            print("ERROR")
            return {
                "Route": module_name,
                "Status": "ERROR",
                "Message": "No port given but port seporater given given.",
            }
        
        try:
            port = int(port)
        except Exception as e:
            return {
                "Route": module_name,
                "Status": "Error",
                "Message": "Port type NaN."
            }
        
        port_valid = validate_types(types)
        if not port_valid:
            return {
                "Route": module_name,
                "Status": "ERROR",
                "Message": "Scan types not valid."
            }
        
        # validate host
        host_valid = validate_host(host)
        if not host_valid:
            print ("ERROR")
            return{
                "Route": module_name,
                "Status": "ERROR",
                "Message": "invalid host."
            }

    except Exception as e:
        return {
            "Route": module_name,
            "Status": "Error",
            "Message": str(e)
        }

def report_back(command):
    result = start_hermes(command)
    return h.received_from_module(result)
    
