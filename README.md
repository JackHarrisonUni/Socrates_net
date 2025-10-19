```
  █████████                                         █████                        ██████   █████           █████   
 ███░░░░░███                                       ░░███                        ░░██████ ░░███           ░░███    
░███    ░░░   ██████   ██████  ████████   ██████   ███████    ██████   █████     ░███░███ ░███   ██████  ███████  
░░█████████  ███░░███ ███░░███░░███░░███ ░░░░░███ ░░░███░    ███░░███ ███░░      ░███░░███░███  ███░░███░░░███░   
 ░░░░░░░░███░███ ░███░███ ░░░  ░███ ░░░   ███████   ░███    ░███████ ░░█████     ░███ ░░██████ ░███████   ░███    
 ███    ░███░███ ░███░███  ███ ░███      ███░░███   ░███ ███░███░░░   ░░░░███    ░███  ░░█████ ░███░░░    ░███ ███
░░█████████ ░░██████ ░░██████  █████    ░░████████  ░░█████ ░░██████  ██████  ██ █████  ░░█████░░██████   ░░█████ 
 ░░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░░      ░░░░░░░░    ░░░░░   ░░░░░░  ░░░░░░  ░░ ░░░░░    ░░░░░  ░░░░░░     ░░░░░  
                                                                                                          
```

> “An examined network is a secure network.”  
_A Python Network Security & Intrusion Detection Toolkit_

---

## Overview
**Socrates.Net** is a modular **Python-based network security suite** designed to help identify anomalies, analyze packets, and simulate basic intrusion detection.  

This project follows Edge Hill University’s *Red Thread* development structure — expanding weekly with new features as programming concepts are introduced.

---

## Features (Planned / In Development)
- **socrates.py**         Central orchestrator
- **plato.py**            Logic and reasoning structures
- **lyceum.py**           Knowledge store (files/logs)
- **epictetus.py**        Error handler
- **sentinel.py**         Monitoring/logging
- **hermes.py**           Network or message module

---

## Update Notes
- **Module layout** changes to layout for how mudules interact
  - module now must go through Horai to be exicuted 
  - all commands given to socrates will go through Horai for validation
  - any request to Horai must be valid for it to be executed

- **Horai Updates** Horai is now a gatekeeper and validator as well as the main security body of the program
  - Modules must perform a handshake with Horai for requests
  - requests must have valid id and key for validation
  - intent should be validated and so should scope
  - anything outside of scope or intent should be terminated and trust revoked 
  - revokation of trust could be temp or perma depending on serverity of transgretion

- **Socrates update** Socrates is just the mouth piece of the system handing requests over from the user and voiceing what he is told
 - only uses commands of ui or ux inhancement all others go through horai

---

Licensed under the MIT License by Socrates
Feel free to use, learn from, and adapt this project — credit appreciated.
