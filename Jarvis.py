import tkinter as tk
from PIL import Image, ImageTk
import threading
import speech_recognition as sr
import pyttsx3
import os
import datetime
import subprocess
import sys
import pywhatkit
import wikipedia
import pyjokes

# Initialize TTS and recognizer
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
recognizer = sr.Recognizer()

# Setup GUI
root = tk.Tk()
root.title("AI VOICE ASSISTANT")

image = Image.open("C:\\Users\\Balamurugan\\OneDrive\\Pictures\\mini.jpg")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack()

status_label = tk.Label(root, text='Initializing....', font=("italic", 14))
status_label.pack()

def update_status(message):
    def update():
        status_label.config(text=message)
    root.after(0, update)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        speak('Good morning sir')
        update_status('Good morning sir')
    elif 12 <= current_hour < 18:
        speak('Good afternoon sir')
        update_status('Good afternoon sir')
    else:
        speak('Good night sir')
        update_status('Good night sir')

def open_software(software_name):
    try:
        if 'chrome' in software_name:
            update_status("Opening Chrome....")
            speak('Opening Chrome....')
            subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
        elif 'microsoft edge' in software_name:
            update_status("Opening Microsoft Edge....")
            speak('Opening Microsoft Edge....')
            subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])
        elif 'notepad' in software_name:
            update_status("Opening Notepad....")
            speak('Opening Notepad....')
            subprocess.Popen(['notepad.exe'])
        elif 'calculator' in software_name:
            update_status("Opening Calculator....")
            speak('Opening Calculator....')
            subprocess.Popen(['calc.exe'])
        elif 'play' in software_name:
            update_status("Opening YouTube....")
            speak("Opening YouTube....")
            pywhatkit.playonyt(software_name)
        elif 'settings' in software_name:
            update_status("Opening Settings....")
            speak("Opening Settings....")
            subprocess.run('powershell -command "Start-Process ms-settings:"', shell=True)
        elif 'powerpoint' in software_name:
            update_status("Opening PowerPoint....")
            speak("Opening PowerPoint....")
            subprocess.Popen([r"C:\Program Files\Microsoft Office\root\Office16\powerpnt.exe"])
        elif 'spotify' in software_name:
            update_status("Opening Spotify....")
            speak("Opening Spotify....")
            subprocess.run('powershell -command "Start-Process spotify:"', shell=True)
        elif 'microsoft store' in software_name:
            update_status("Opening Microsoft Store....")
            speak("Opening Microsoft Store....")
            subprocess.run('powershell -command "Start-Process ms-windows-store:"', shell=True)
        elif 'gmail' in software_name:
            update_status("Opening Gmail....")
            speak("Opening Gmail....")
            subprocess.run('powershell -command "Start-Process \'https://mail.google.com\'"', shell=True)
        elif 'vlc app' in software_name:
            update_status("Opening VLC....")
            speak("Opening VLC....")
            subprocess.run('powershell -command "Start-Process \\"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe\\""', shell=True)
        elif 'excel' in software_name:
            update_status("Opening Excel....")
            speak("Opening Excel....")
            subprocess.Popen([r"C:\Program Files\Microsoft Office\root\Office16\excel.exe"])
        elif 'whatsapp' in software_name:
            update_status("Opening WhatsApp....")
            speak("Opening WhatsApp....")
            subprocess.run('powershell -command "Start-Process whatsapp:"', shell=True)
        elif 'weather' in software_name:
            update_status("Opening Weather....")
            speak("Opening Weather....")
            subprocess.run('powershell -command "Start-Process \'https://www.weather.com\'"', shell=True)
        else:
            update_status(f"I could not find the software {software_name}")
            speak(f"I could not find the software {software_name}")
    except Exception as e:
        update_status(f"Error: {e}")

def close_software(software_name):
    try:
        task_map = {
            'chrome': 'chrome.exe',
            'microsoft edge': 'msedge.exe',
            'notepad': 'notepad.exe',
            'calculator': 'calculator.exe',
            'powerpoint': 'powerpnt.exe',
            'excel': 'excel.exe',
        }

        if software_name in task_map:
            update_status(f"Closing {software_name}....")
            speak(f"Closing {software_name}....")
            os.system(f"taskkill /f /im {task_map[software_name]}")
        elif 'settings' in software_name:
            update_status("Closing Settings....")
            speak("Closing Settings....")
            subprocess.run('powershell -command "Stop-Process -Name SystemSettings"', shell=True)
        elif 'spotify' in software_name:
            update_status("Closing Spotify....")
            speak("Closing Spotify....")
            subprocess.run('powershell -command "Stop-Process -Name Spotify"', shell=True)
        elif 'microsoft store' in software_name:
            update_status("Closing Microsoft Store....")
            speak("Closing Microsoft Store....")
            subprocess.run('powershell -command "Stop-Process -Name WinStore.App"', shell=True)
        elif 'whatsapp' in software_name:
            update_status("Closing WhatsApp....")
            speak("Closing WhatsApp....")
            subprocess.run('powershell -command "Stop-Process -Name WhatsApp"', shell=True)
        elif 'vlc app' in software_name:
            update_status("Closing VLC....")
            speak("Closing VLC....")
            subprocess.run('powershell -command "Stop-Process -Name vlc"', shell=True)
        else:
            update_status(f"No open software named {software_name}")
            speak(f"No open software named {software_name}")
    except Exception as e:
        update_status(f"Error: {e}")

def wikipedia_search(query):
    try:
        speak(f"Searching Wikipedia for {query}...")
        result = wikipedia.summary(query, sentences=2)
        update_status(f"Wikipedia result: {result}")
        speak(result)
    except wikipedia.exceptions.PageError:
        update_status("No result found on Wikipedia")
        speak("No result found on Wikipedia")

def tell_joke():
    joke = pyjokes.get_joke()
    update_status(f"Joke: {joke}")
    speak(joke)
    speak("Hahahahahaaa!")

def listen_for_wake_word():
    with sr.Microphone() as source:
        update_status("Listening for wake word....")
        while True:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recorded_audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(recorded_audio, language='en_us').lower()
                if 'alexa' in text:
                    update_status("Wake word detected!")
                    greet_user()
                    update_status("Hi Sir, how can I help you?")
                    speak("Hi Sir, how can I help you?")
                    return True
            except Exception:
                update_status("I could not understand. Please try again.")
                speak("I could not understand. Please try again.")

def cmd():
    with sr.Microphone() as source:
        update_status("Clearing background noise... please wait!")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        update_status("Ask me anything...")
        recorded_audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recorded_audio, language='en_us').lower()
        update_status(f"Your message: {text}")

        if 'stop' in text:
            update_status("Stopping the program. Goodbye!")
            speak("Stopping the program. Goodbye!")
            sys.exit()
        elif 'open' in text:
            software_name = text.replace('open', '').strip()
            open_software(software_name)
        elif 'close' in text:
            software_name = text.replace('close', '').strip()
            close_software(software_name)
        elif 'time' in text:
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            update_status(f"The time is {current_time}")
            speak(current_time)
        elif 'what is your name' in text:
            update_status("My name is JARVIS, your artificial intelligence.")
            speak("My name is JARVIS, your artificial intelligence.")
        elif 'wikipedia' in text:
            search_query = text.replace('wikipedia', '').strip()
            wikipedia_search(search_query)
        elif 'joke' in text:
            tell_joke()
        else:
            update_status("Sorry, I didn’t catch that.")
            speak("Sorry, I didn’t catch that.")
    except sr.UnknownValueError:
        update_status("Sorry, I could not understand your speech.")
        speak("Sorry, I could not understand your speech.")
    except Exception as ex:
        update_status(f"Error: {ex}")
        speak("An error occurred.")

def main():
    if listen_for_wake_word():
        while True:
            cmd()

# Start in separate thread to allow GUI mainloop
thread = threading.Thread(target=main)
thread.start()

root.mainloop()
