# main.py
from modules.voice_engine import speak, listen
from modules.facial_login_cv import facial_login
from modules.command_center import handle_command

if facial_login():
    speak("Hello, I’m ready. How can I help you today?")
    while True:
        command = listen()
        if "exit" in command:
            speak("Goodbye!")
            break
        elif command:
            response = handle_command(command)
            speak(response)