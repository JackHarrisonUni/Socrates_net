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
import modules.plato as p 
import modules.lyceum as l
import modules.hermes as h

import shlex
import datetime as dt

#import other modules as they are developed



### handshake request variables

### Request Variables

class Horai:
    def __init__(self, dev_mode = False, paranoid_mode = True):
        # CORE IDENTITY
        self.module_name = "Horai"
        self.module_version = "0.0.4"
        self.module_description = "Horai the gate gaurd to olympus. She will validate all commands and destroy those that do not live up to her standards"

        # INTERNAL STATES
        self.registry = {}
        self.blacklist = {}
        self.trust = {}
        self.transient_challenges = {}

        # MODES
        self.dev = dev_mode
        self.para = paranoid_mode
        self.mode = self.set_mode()
        
        # MODULES
        self.p = p
        self.l = l
        self.h = h


    # METHODS
    def set_mode(self):
        if self.dev:
            mode = False
        elif self.para:
            mode = True
        
        else:
            mode = False
        
        return mode

    def set_dev(self, bool):
        self.dev = bool
        self.set_para(not bool)
        return self.set_mode()
    
    def set_para(self, bool):
        self.para = bool
        self.set_dev(not bool)
        return self.set_mode()

    def log_lyceum(self, data):
        try:
            response = self.l.create_log(data)
            return (response)
        except Exception as e:
            return {
                "Route": self.module_name,
                "From": "Lyceum",
                "Status": "ERROR",
                "Message": f"Cannot connect to Lyceum: {e}"
            }
        
    def use_plato(self, plato_command): 
        try:
            input_type, input_data = plato_command
            result = self.p.reasoning_engine(input_data, input_type)
            return result
        except ValueError:
            self.l.create_log()
            return 

    def use_lyceum(self, lyceum_command):
        try:
            self.l.main(lyceum_command)
            return
        except Exception as e:
            return e

    def process_command(self, payload):
        try:
            if not command:
                return {
                    "Route": self.module_name,
                    "Status": "ERROR",
                    "Message": "Empty command."
                }
            token = payload.get("Token",)[1:]
            command = payload.get("Raw")

            ### ROUTING
            first = shlex.split(command)[0]
            if first == "-Plato":
                ### Route to plato
                try: 
                    result = self.use_plato(token)
                    if isinstance(result, dict):
                        log = {
                            "Route": self.module_name,
                            "From": "Plato",
                            "Status": result.get("Status", "OK"),
                            "Time_Stamp": dt.datetime.now()
                        }
                        wrapped = {
                            "Route": self.module_name,
                            "From": "Plato",
                            "Status": result.get("Status", "OK"),
                            "Message": result.get("Result", ""),
                            "Meta": result.get("Meta", {})
                        }
                    else:
                        log = {
                            "Route": self.module_name,
                            "From": "Plato",
                            "Status": "OK",
                            "Time_Stamp": dt.datetime.now()
                        }
                        wrapped = {
                            "Route": self.module_name,
                            "From": "Plato",
                            "Status": "OK",
                            "Message": str(result),
                        }
                    
                    return {
                        "Log":log,
                        "Wrapped": wrapped
                        }
                
                except Exception as e:
                    self.log_lyceum( {
                            "Route": self.module_name,
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
                    response = self.h.start_hermes()
                    
                    log = {
                        "Route": self.module_name,
                        "From": "Hermes",
                        "Status": response.get("Status", "OK"),
                        "Time_Stamp": dt.datetime.now()
                    }
                    wrapped = {
                        "Route": self.module_name,
                        "From": "Hermes",
                        "Status": "OK",
                        "Message": f"{response.get('Result')}"
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
                    self.use_lyceum(token)
                    self.log_lyceum({
                        "Route": self.module_name,
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
                    self.log_lyceum({
                        "Route": self.module_name,
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
                self.log_lyceum({
                        "Route": self.module_name,
                        "From": self.module_name,
                        "Status": "ERROR",
                        "Time_Stamp": dt.datetime.now()
                    })
                return{
                    "Route": self.module_name,
                    "Status": "ERROR",
                    "Message": f"No Module found for command {first}"
                }

            else:
                return {
                    "Route": self.module_name,
                    "Status": "OK",
                    "Message": f"Echo from {self.module_name}: {command}"
                }

        except Exception as e:
            self.log_lyceum({
                        "Route": self.module_name,
                        "From": self.module_name,
                        "Status": "ERROR",
                        "Time_Stamp": dt.datetime.now()
                    })
            return {
                "Route": self.module_name,
                "Status": "ERROR",
                "Message": str(e)
            }
                    
    def validate_payload(self, payload):
        required = ["Source", "Raw", "Token"]
        return all(k in payload for k in required)

    def normalize_tokens(self, tokens):
        if not tokens: return []
        cleaned = [t.strip() for t in tokens if t and t.strip()]
        return cleaned

    def received_from_module(self, data):
        try:
            route = data.get("Route")
            if route in ["Horai","Lyceum"]:
                return {
                    "Status": "OK",
                    "Message": f"{route} message ignored to prevent recursion"
                }
            response = self.l.save_log(data)
            return response
        
        except Exception as e:
            return {
                "Status": "ERROR",
                "Route": "Horai",
                "Message": f"Failed to process module data: {e}"
            }

    ### Main Flow Management Logic
    def the_gates(self, payload):

        if not self.validate_payload(payload):
            self.log_lyceum({
                        "Route": self.module_name,
                        "From": self.module_name,
                        "Status": "ERROR",
                        "Time_Stamp": dt.datetime.now()
                    })
            return {
                "Route": self.module_name,
                "Status": "ERROR",
                "Message": "Malformed payload"
            }
        
        token = self.normalize_tokens(payload.get("Token", []))
        if not token:
            self.log_lyceum({
                        "Route": self.module_name,
                        "From": self.module_name,
                        "Status": "ERROR",
                        "Time_Stamp": dt.datetime.now()
                    })
            return {
                "Route": self.module_name,
                "Status": "ERROR",
                "Message": "Empty or invalid args"
            }
        

        response = self.process_command(payload)

        if "Log" in response and "Wrapped" in response:
            self.log_lyceum(response.get("Log"))
            return response.get("Wrapped")
        else:
            return response
        

### TODO add blacklist functionality with lyceum audit record 