# modules/command_center.py
from modules import ai_chat, emotion_detector, file_organizer
import os

def handle_command(command):
    if "organize files" in command:
        folder = os.path.expanduser("~/Downloads")
        file_organizer.organize(folder)
        return "Files organized."

    elif "detect emotion" in command:
        emotion_detector.detect_emotion()
        return "Emotion detection started."

    else:
        return ai_chat.get_ai_response(command)