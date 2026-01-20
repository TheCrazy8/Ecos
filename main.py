import datetime
import sys
import os
import webbrowser

now = datetime.datetime.now()
namespace = os.getenv('USER', 'Guest')

def greet_user(name):
    return f"Hello, {name}! Today is {now.strftime('%Y-%m-%d')}.\n Welcome to the Hacking Tool!"

def modify_windows():
    try:
        modify_windows_specific_settings()
        return "Success"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error"

def modify_windows_specific_settings():
    # Placeholder for Windows-specific modifications
    print("You really thought...\nGet dunked on.")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return "Lol"

def main():
    print(greet_user(namespace))
    result = modify_windows()
    if result == "Error":
        print("Exiting due to incompatible OS.")
        return
    else:
        print("Modifications completed successfully.")
