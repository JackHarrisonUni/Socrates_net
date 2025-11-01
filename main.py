import random
from modules import socrates as socrates


author = "ZeroCypher"
description = "Socrates.Net is a suite of network security tools developed in python."

version = "0.9.0"
def load_banner():
    Ascii_Banner_path = (random.choice(
        ["Ascii_Banners/Socrates/Socrates_Banner0.txt",
        "Ascii_Banners/Socrates/Socrates_Banner1.txt",]
        ))
    
    with open(Ascii_Banner_path, 'r') as f:
        Ascii_Banner = f.read()
        return Ascii_Banner
    
socrates.main(load_banner,version, author, description)