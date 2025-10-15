### Variables for Socrates.net
Ascii_Banner = r"""
  /$$$$$$                                           /$$                            /$$   /$$             /$$    
 /$$__  $$                                         | $$                           | $$$ | $$            | $$    
| $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$   | $$$$| $$  /$$$$$$  /$$$$$$  
|  $$$$$$  /$$__  $$ /$$_____/ /$$__  $$|____  $$|_  $$_/   /$$__  $$ /$$_____/   | $$ $$ $$ /$$__  $$|_  $$_/  
 \____  $$| $$  \ $$| $$      | $$  \__/ /$$$$$$$  | $$    | $$$$$$$$|  $$$$$$    | $$  $$$$| $$$$$$$$  | $$    
 /$$  \ $$| $$  | $$| $$      | $$      /$$__  $$  | $$ /$$| $$_____/ \____  $$   | $$\  $$$| $$_____/  | $$ /$$
|  $$$$$$/|  $$$$$$/|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$$ /$$$$$$$//$$| $$ \  $$|  $$$$$$$  |  $$$$/
 \______/  \______/  \_______/|__/      \_______/   \___/   \_______/|_______/|__/|__/  \__/ \_______/   \___/  
"""

version = "0.0.1"
author = "Socrates"
description = "A modular cybersecurity suit inpired by Philosophy and Logic. " # describe what the socrates suit does
menu = """
[1] --- plato.py ---------  Logic and reasoning structures ---
[2] --- lyceum.py --------  Knowledge store (files/logs) -----
[3] --- epictetus.py -----  Error handler --------------------
[4] --- sentinel.py ------  Monitoring/logging ---------------
[5] --- hermes.py --------  Network or message module --------
[6] --- athena.py -------   Kill and exit --------------------

Please select a module to load:     """



### Boot sequance
print(f"{Ascii_Banner}\n\n\nVersion: {version} | Author: {author}\nDescription: {description}")
tool_Selected = input(menu)
print(f"You have selected option {tool_Selected}. Loading module...")