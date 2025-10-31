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
module_version = "0.0.1" #basic single target port scanner

module_description = "This is Hermes the messanger of the gods. He checks the network packets and scans targets."

# functions
def verify():
    #this will call horai and register with it 
    return

def start_hermes():
    print(disclamer)
    # entry route however could we just pull scan_target staright away.
    
    pass

def scan_target(target):
    target = target.strip()
    if target == "":
        print("ERROR")
        return {
            "Route": module_name,
            "Status": "ERROR",
            "Message": "No target given",
        }
    #check for ports being present #
    host, sep, port = target.partition(":")
    if host and port:
        print (host, port)
        if host.count(":") > 1 or port.startswith(":"):
            print("IPv6 not supported in v0.0.1")
            return {"Route": module_name, "Status": "ERROR", "Message": "IPv6 not supported in v0.0.1"}
        return
    elif host and sep and not port:
        print("ERROR")
        return {
            "Route": module_name,
            "Status": "ERROR",
            "Message": "No port given but : given",
        }

def report_back(result):
    return h.received_from_module(result)
    
