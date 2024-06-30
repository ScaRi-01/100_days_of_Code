import os

def clear():
    # Clear the terminal screen based on OS
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Linux/Mac
        _ = os.system('clear')
