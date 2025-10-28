### Lyceum Log manager fopr socrates.net



# Imports for lyceum

module_name = "Lyceum"
module_version = "0.0.1" #basic take in function
# module_version = "0.0.2" # fully functional stores
# module_version = "0.0.3" # head and tail function
# module_version = "1.0.0" # fully functional basic store and retreve function with security
module_description = "Logging and stores for Socrates.Net"
# Functions for lyceum
def validate_payload(payload):
    required = ["Route", "Status", "Message", "Time_stamp"]
    return all(k in payload for k in required)

def create_log(data):
    try:
        valid = validate_payload(data)
        if data and valid:
            response = {
                        "Route": module_name,
                        "Status": "OK",
                        "Logged": True,
                        "Message": "System log updated"
                        }
            return response
    except Exception as e:
        return (
            {
            "Status": "ERROR",
            "Logged": False,
            "Message": e

        })