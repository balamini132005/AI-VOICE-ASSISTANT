# 🤖 AI Voice Assistant (JARVIS)

An AI-powered desktop voice assistant built using **Python**. The assistant listens for a wake word, understands voice commands, responds using text-to-speech, and performs different desktop tasks such as opening applications, searching Wikipedia, telling jokes, and providing the current time.

The project uses **Tkinter** for the graphical user interface, **SpeechRecognition** for voice input, and **pyttsx3** for voice output.

---

## 📌 Project Overview

The AI Voice Assistant works like a personal desktop assistant. It continuously listens for the wake word **"Alexa"** and starts interacting with the user when the wake word is detected.

The assistant can:

* 🎤 Recognize voice commands
* 🔊 Respond using text-to-speech
* 🖥️ Open desktop applications
* ❌ Close running applications
* 🕐 Tell the current time
* 🔎 Search Wikipedia
* 😂 Tell jokes
* 👋 Greet the user based on the time of day
* 🛑 Stop the program using a voice command

---

## 🎯 Objectives

* Develop a simple AI-based voice assistant using Python.
* Implement speech recognition and text-to-speech.
* Automate common desktop operations using voice commands.
* Create a graphical user interface using Tkinter.
* Integrate external services such as Wikipedia and YouTube.
* Provide a hands-free interaction system.

---

## 🛠️ Technologies Used

| Technology        | Purpose                              |
| ----------------- | ------------------------------------ |
| Python            | Main programming language            |
| Tkinter           | Graphical User Interface             |
| SpeechRecognition | Speech-to-text conversion            |
| pyttsx3           | Text-to-speech                       |
| PIL / Pillow      | Image handling                       |
| PyWhatKit         | YouTube playback                     |
| Wikipedia         | Wikipedia search                     |
| PyJokes           | Generate jokes                       |
| Threading         | Background voice processing          |
| OS                | System operations                    |
| Subprocess        | Opening and controlling applications |
| Datetime          | Time and greeting functionality      |

The imported libraries and modules are directly used in the provided project code.

---

## ✨ Features

### 🎤 1. Voice Recognition

The assistant uses a microphone to capture the user's voice and Google's speech recognition service to convert speech into text.

Example:

```text
User: Alexa
Assistant: Hi Sir, how can I help you?
```

---

### 👋 2. Automatic Greeting

The assistant checks the current time and provides an appropriate greeting:

```text
Good morning sir
Good afternoon sir
Good night sir
```

The greeting is generated based on the current hour.

---

### 🖥️ 3. Open Applications

The assistant can open several applications using voice commands.

Examples include:

```text
Open Chrome
Open Microsoft Edge
Open Notepad
Open Calculator
Open PowerPoint
Open Excel
Open Spotify
Open WhatsApp
Open Gmail
Open VLC
Open Settings
Open Microsoft Store
```

The application-opening functionality uses `subprocess`, PowerShell commands, and PyWhatKit depending on the requested application.

---

### ❌ 4. Close Applications

The assistant can also close supported applications using voice commands.

Example:

```text
Close Chrome
Close Notepad
Close Excel
Close Spotify
Close WhatsApp
```

The project uses Windows process commands to close applications.

---

### 🕐 5. Tell Current Time

You can ask:

```text
What is the time?
```

The assistant retrieves the current system time and speaks it aloud.

---

### 🔎 6. Wikipedia Search

The assistant can search Wikipedia using a voice command.

Example:

```text
Wikipedia Artificial Intelligence
```

It retrieves a short Wikipedia summary and reads the result aloud.

---

### 😂 7. Tell Jokes

The assistant uses the `pyjokes` library to generate and speak a joke.

Example:

```text
Tell me a joke
```

The assistant responds with a generated joke.

---

### 🛑 8. Stop the Assistant

The assistant can be stopped using a voice command containing:

```text
Stop
```

It then announces that the program is stopping and exits.

---

## 🔄 System Workflow

```text
              ┌──────────────────┐
              │   Start Program  │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │  Listen for      │
              │  Wake Word       │
              └────────┬─────────┘
                       ↓
                "Alexa" Detected
                       ↓
              ┌──────────────────┐
              │     Greeting     │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │ Listen to Command│
              └────────┬─────────┘
                       ↓
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
     Open/Close      Wikipedia      Other
     Application      Search        Commands
        ↓              ↓              ↓
        └──────────────┼──────────────┘
                       ↓
              ┌──────────────────┐
              │ Voice Response   │
              └────────┬─────────┘
                       ↓
                Listen Again
```

The voice-processing functions run in a separate thread so the Tkinter GUI can continue running.

---

## 📂 Project Structure

```text
AI-Voice-Assistant/
│
├── main.py
├── README.md
├── requirements.txt
└── assets/
    └── mini.jpg
```

> Rename `main.py` to whatever your actual Python file is called.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd AI-Voice-Assistant
```

### 2. Install Required Libraries

```bash
pip install tkinter
pip install pillow
pip install SpeechRecognition
pip install pyttsx3
pip install pywhatkit
pip install wikipedia
pip install pyjokes
```

For microphone support, you may also need:

```bash
pip install PyAudio
```

---

## 📄 Requirements.txt

Create a file named `requirements.txt`:

```text
Pillow
SpeechRecognition
pyttsx3
pywhatkit
wikipedia
pyjokes
PyAudio
```

> Tkinter is normally included with standard Python installations on Windows, so it generally does not need to be installed through pip.

---

## ▶️ How to Run

Run the Python file:

```bash
python main.py
```

The application will open the **AI VOICE ASSISTANT** GUI.

The assistant then listens for the wake word:

```text
Alexa
```

After detecting it, you can give commands.

---

## 🗣️ Example Voice Commands

| Voice Command       | Action                  |
| ------------------- | ----------------------- |
| `Alexa`             | Activate assistant      |
| `Open Chrome`       | Opens Google Chrome     |
| `Open Notepad`      | Opens Notepad           |
| `Open Calculator`   | Opens Calculator        |
| `Open YouTube`      | Plays requested content |
| `Open Spotify`      | Opens Spotify           |
| `Open WhatsApp`     | Opens WhatsApp          |
| `Close Chrome`      | Closes Chrome           |
| `What is the time?` | Gives current time      |
| `Wikipedia Python`  | Searches Wikipedia      |
| `Tell me a joke`    | Tells a joke            |
| `Stop`              | Stops the assistant     |

These commands correspond to the command-handling logic implemented in the provided code.

---

## 🖥️ GUI

The project uses **Tkinter** to create the desktop interface.

The GUI includes:

* Assistant title
* Assistant image
* Status display
* Voice interaction running in the background

The application initializes the Tkinter window and displays an image using Pillow.

---

## ⚠️ Important Notes

This project currently contains **Windows-specific application paths**, for example paths to Chrome, Microsoft Edge, PowerPoint, and Excel.

Therefore:

* The application is primarily designed for **Windows**.
* Application paths may need to be changed depending on your computer.
* A working microphone is required.
* Internet access is required for Google speech recognition and Wikipedia-related functionality.
* The image path in the code should be changed to the location of your own image.

For example, replace:

```python
C:\Users\Balamurugan\OneDrive\Pictures\mini.jpg
```

with your own image path.

---

## 🔮 Future Enhancements

Possible improvements include:

* 🤖 Integration with OpenAI/Gemini APIs
* 🌐 Web search capability
* 📧 Sending emails using voice commands
* 📱 WhatsApp message automation
* 📰 News updates
* 🌦️ Weather information
* 📅 Calendar and reminders
* 🔐 Voice authentication
* 🧠 Natural Language Processing
* 🏠 Smart home control
* 🎵 Improved music control
* 💻 Cross-platform support

---

## 📚 Learning Outcomes

Through this project, you can learn:

* Python programming
* Speech recognition
* Text-to-speech systems
* GUI development with Tkinter
* Multithreading
* API/service integration
* Desktop automation
* Exception handling
* Python library integration

---

## 👨‍💻 Author

**Balamurugan U**

B.E. Computer Science and Engineering
Artificial Intelligence & Machine Learning
Jerusalem College of Engineering

---

## ⭐ Conclusion

This **AI Voice Assistant (JARVIS)** project demonstrates how Python can be used to build an interactive desktop assistant that understands voice commands and performs useful tasks.

It combines **speech recognition, text-to-speech, GUI development, desktop automation, Wikipedia search, YouTube playback, and joke generation** into a single application.
