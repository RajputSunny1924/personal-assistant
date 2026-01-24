import speech_recognition as sr
import webbrowser
import pyttsx3
import pyautogui
import musiclibrary
import jokes
from simpleeval import simple_eval
import datetime
import time
import os

current_voice = 0   # 0 = male, 1 = female
r= sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    global current_voice
    try:
        engine = pyttsx3.init('sapi5')   # fresh engine every time
        engine.setProperty('rate', 170)
        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[current_voice].id)

        engine.say(str(text))
        engine.runAndWait()
    except Exception as e:
        print("Speak Error:", e)

def wishme():
    hour = datetime.datetime.now().hour
    if hour <= 12:
        speak("Good morning sir")
    elif hour <= 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("you said:", command)
            return command.lower()
        except:
            return"none"

def processcommand(c):
    global current_voice

    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "close google" in c.lower():
        speak("google")
        pyautogui.hotkey("ctrl","w")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "close facebook" in c.lower():
        speak("facebook")
        pyautogui.hotkey("ctrl","w")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "close youtube" in c.lower():
        speak("youtube")
        pyautogui.hotkey("ctrl","w")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "close instagram" in c.lower():
        speak("instagram")
        pyautogui.hotkey("ctrl","w")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif "close whatsapp" in c.lower():
        speak("whatsapp")
        pyautogui.hotkey("ctrl","w")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "close chatgpta" in c.lower():
        speak("chatgpt")
        pyautogui.hotkey("ctrl","w")
    elif "open gmail" in c.lower():
        webbrowser.open("https://mail.google.com")
    elif "close gmail" in c.lower():
        speak("gmail")
        pyautogui.hotkey("ctrl","w")
    elif "open twitter" in c.lower():
        webbrowser.open("https://twitter.com")
    elif "close twitter" in c.lower():
        speak("twitter")
        pyautogui.hotkey("ctrl","w")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "close linkedin" in c.lower():
        speak("linkedin")
        pyautogui.hotkey("ctrl","w")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "close github" in c.lower():
        speak("github")
        pyautogui.hotkey("ctrl","w")
    elif "open stackoverflow" in c.lower():
        webbrowser.open("https://stackoverflow.com")
    elif "close stackoverflow" in c.lower():
        speak("stackoverflow")
        pyautogui.hotkey("ctrl","w")
    elif "open maps" in c.lower():
        webbrowser.open("https://maps.google.com")
    elif "close maps" in c.lower():
        speak("maps")
        pyautogui.hotkey("ctrl","w")
    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com")
    elif "close spotify" in c.lower():
        speak("spotify")
        pyautogui.hotkey("ctrl","w")
    elif "open netflix" in c.lower():
        webbrowser.open("https://netflix.com")
    elif "close netflix" in c.lower():
        speak("netflix")
        pyautogui.hotkey("ctrl","w")
    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.in")
    elif "close amazon" in c.lower():
        speak("amazon")
        pyautogui.hotkey("ctrl","w")
    elif "open flipkart" in c.lower():
        webbrowser.open("https://flipkart.com")
    elif "close flipkart" in c.lower():
        speak("flipkart")
        pyautogui.hotkey("ctrl","w")
    
    elif "activate female voice" in c.lower():
        current_voice = 1
        speak("female voice activated")
    
    elif "activate male voice" in c.lower():
        current_voice = 0
        speak("male voice activated")

    elif "your name" in c.lower():
        speak("My name is Jarvis, your personal assistant")
    elif "how are you" in c.lower():
        speak("I am always perfect when you talk to me")
    elif "do you love me" in c.lower():
        speak("yes i love you so much sunny")

    elif "who made you" in c.lower():
        speak("sunny singh rajput made me")
    elif "shutdown" in c:
        speak("Shutting down the system")
        os.system("shutdown /s /t 5") 
    elif "restart" in c:
        speak("Restarting the system")
        os.system("shutdown /r /t 5")

    elif "calculate" in c.lower():
        try:
            question = c.lower().replace("calculate", "").strip()
            question = question.replace("plus", "+").replace("minus", "-")
            question = question.replace("into", "*").replace("multiply", "*")
            question = question.replace("divide", "/").replace("by", "/")

            result = simple_eval(question)
            speak(f"The result is {result}")
        except:
            speak("Sorry, I could not calculate that.")

    elif "time" in c.lower():
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"what is time {time}")

    elif "date" in c.lower():
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"what is date today {date}")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "joke" in c.lower():
        joke = jokes.get_joke()
        speak(joke)

    elif "open notepad" in c.lower():
        os.startfile("notepad.exe")
    elif "open camera" in c.lower():
        os.system("start microsoft.windows.camera:")
    elif "open calculator" in c.lower():
        os.startfile("calc.exe")
    elif "open command prompt" in c.lower():
        os.system("start cmd")
    elif "open file explorer" in c.lower():
        os.system("explorer")

    elif "volume up" in c.lower():
        pyautogui.press("volumeup")

    elif "volume down" in c.lower():
        pyautogui.press("volumedown")

    elif "mute" in c.lower():
        pyautogui.press("volumemute")

active = False
while True:
    command = takecommand()

    if command == "none":
        continue

    if not active:
        if "hello jarvis" in command:
            speak("Jarvis is active")
            wishme()
            active = True
        continue

    # jarvis is active now → bar-bar commands sunega
    if "stop jarvis" in command or "exit" in command:
        speak("Jarvis deactivated")
        active = False
        continue

    processcommand(command)
    time.sleep(0.5)

