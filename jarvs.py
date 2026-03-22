# python libraries
import speech_recognition as sr
import webbrowser
import pyttsx3
import pyautogui
import pygetwindow as gw
import jarvis_web.jokes as jokes
from simpleeval import simple_eval
import pywhatkit
import datetime
import time
import os

# ---------------- OOP SECURITY SYSTEM ----------------
class JarvisSecurity:
    def __init__(self, password, max_attempts=3):
        self.password = password
        self.max_attempts = max_attempts
        self.attempts = 0

    def verify(self):
        speak("Please speak the voice password")
        
        while self.attempts < self.max_attempts:
            user_pass = takec()

            if user_pass == "none":
                # User didn't say anything, don't count as an attempt
                speak("I didn't hear anything. Please say the password.")
                continue

            if self.password in user_pass:
                speak("Access granted")
                self.attempts = 0
                return True
            else:
                self.attempts += 1
                remaining = self.max_attempts - self.attempts
                speak(f"Wrong password. {remaining} attempts remaining")

        # after 3 wrong attempts
        speak("Maximum attempts reached. Jarvis is now locked")
        return False

# whatsapp contacts
contacts = {
    "vishal": "+91 85917 91384", 
    "sunny": "+91 7350288505",
    "lalit": "+91 99749 57619",
    "vaishali di": "+91 93097 10981",
}

# male/female voice
current_voice = 0  
r = sr.Recognizer()
engine = pyttsx3.init()
security = JarvisSecurity("open system")

# whatsapp message sending
def send_whatsapp_message(name, message):
    if name in contacts:
        number = contacts[name]
        speak(f"Sending message to {name}")
        pywhatkit.sendwhatmsg_instantly(number, message, 10)
        speak("Message sent successfully")
    else:
        speak("Sorry, I don't have this contact saved.")

# jarvis speaking function
def speak(text):
    global current_voice
    try:
        engine = pyttsx3.init('sapi5')  
        engine.setProperty('rate', 170)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[current_voice].id)
        engine.say(str(text))
        engine.runAndWait()
    except Exception as e:
        print("Speak Error:", e)

# jarvis intro
jarvis_intro = "I am Jarvis, your personal voice assistant. I can open websites, play music, tell jokes, give time and date, perform simple calculations, control system tasks, remember things, and send WhatsApp messages to your contacts. How can I help you today?"

def focus_youtube():
    try:
        for w in gw.getAllTitles():
            if "youtube" in w.lower():
                win = gw.getWindowsWithTitle(w)[0]
                win.activate()
                time.sleep(1)
                return True
        return False
    except:
        return False

# greeting function
def wishme():
    hour = datetime.datetime.now().hour
    if hour <= 12:
        speak("Good morning sir")
    elif hour <= 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

# taking command from user
def takec():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            c = r.recognize_google(audio)
            print("you said:", c)
            return c.lower()
        except:
            return "none"

# processing the command
def processc(c):
    global current_voice

    # opening and closing websites
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
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "close chat gpta" in c.lower():
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
    elif "open map" in c.lower():
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

    # play on youtube
    elif "play" in c.lower():
        query = c.lower().replace("play", "").replace("on youtube","").strip()
        if query != "":
            speak(f"Playing {query} on YouTube")
            pywhatkit.playonyt(query)
        else:
            speak("What should I play?")

    # youtube search
    elif "youtube" in c.lower() and "search" in c.lower():
        query = c.lower().replace("search","").replace("on youtube","").replace("youtube","").strip()
        speak(f"Searching YouTube for {query}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    # google search
    elif "google" in c.lower() and "search" in c.lower():
        query = c.lower().replace("search","").replace("on google","").replace("google","").strip()
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # youtube controls
    elif "stop" in c or "resume" in c:
        if focus_youtube():
            pyautogui.press("space")
            speak("Done")
    elif "next video" in c:
        if focus_youtube():
            pyautogui.hotkey("shift","n")
            speak("Playing next video")
    elif "previous video" in c:
        if focus_youtube():
            pyautogui.hotkey("shift","p")
            speak("Playing previous video")
    elif "mute" in c:
        if focus_youtube():
            pyautogui.press("m")
            speak("Video muted")
    elif "volume up youtube" in c:
        if focus_youtube():
            pyautogui.press("up")
    elif "volume down youtube" in c:
        if focus_youtube():
            pyautogui.press("down")
    elif "full screen" in c:
        if focus_youtube():
            pyautogui.press("f")
    elif "exitfull screen" in c:
        if focus_youtube():
            pyautogui.press("f")
    elif "forward video" in c:
        if focus_youtube():
            pyautogui.press("l")
    elif "backward video" in c:
        if focus_youtube():
            pyautogui.press("j")
    elif "skip ad" in c:
        if focus_youtube():
            pyautogui.press("tab")
            time.sleep(0.5)
            pyautogui.press("enter")
            speak("Skipping advertisement")

    # voice change
    elif "activate female voice" in c.lower():
        current_voice = 1
        speak("female voice activated")
    elif "activate male voice" in c.lower():
        current_voice = 0
        speak("male voice activated")

    # personal
    elif "your name" in c.lower():
        speak("My name is Jarvis, your personal assistant")
    elif "how are you" in c.lower():
        speak("I am always perfect when you talk to me")
    elif "do you love me" in c.lower():
        speak("yes i love you so much sunny")
    elif "who made you" in c.lower():
        speak("sunny singh rajput made me")
    elif "jarvis" in c.lower():
        speak("yeah")

    # system control
    elif "shutdown" in c:
        speak("Shutting down the system")
        os.system("shutdown /s /t 5")
    elif "restart" in c:
        speak("Restarting the system")
        os.system("shutdown /r /t 5")
    elif "what can you do" in c or "what are your features" in c:
        speak(jarvis_intro)

    # calculations
    elif "calculate" in c.lower():
        try:
            question = c.lower().replace("calculate", "").strip()
            question = question.replace("plus","+").replace("minus","-")
            question = question.replace("into","*").replace("multiply","*")
            question = question.replace("divide","/").replace("by","/")
            result = simple_eval(question)
            speak(f"The result is {result}")
        except:
            speak("Sorry, I could not calculate that.")

    # time and date
    elif "time" in c.lower():
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "date" in c.lower():
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"what is date today {date}")

    # jokes
    elif "joke" in c.lower():
        joke = jokes.get_joke()
        speak(joke)

    # system applications
    elif "open notepad" in c.lower():
        os.startfile("notepad.exe")
    elif "open camera" in c.lower():
        os.system("start microsoft.windows.camera:")
    elif "open calculator" in c.lower():
        os.startfile("calc.exe")
    elif "open c prompt" in c.lower():
        os.system("start cmd")
    elif "open file explorer" in c.lower():
        os.system("explorer")

    # volume control
    elif "volume up" in c.lower():
        pyautogui.press("volumeup")
    elif "volume down" in c.lower():
        pyautogui.press("volumedown")
    elif "mute" in c.lower():
        pyautogui.press("volumemute")

    # whatsapp message
    elif "send message to" in c.lower():
        try:
            parts = c.lower().split("send message to",1)[1].strip()
            name = parts.split(" ",1)[0]
            message = parts.split(" ",1)[1]
            send_whatsapp_message(name,message)
        except:
            speak("Please say like, send message to vishal hello bro")
    else:
        speak("i didnt understand that")

# main program
active = False
while True:
    c = takec()
    if c == "none":
        continue
    if not active:
        if "hello jarvis" in c:
            speak("Hello sir")
            if security.verify():
                wishme()
                active = True
            else:
                speak("Security lock activated. Exiting Jarvis")
                break
        continue

    # jarvis is active now
    if "stop jarvis" in c or "exit" in c:
        speak("Jarvis deactivated")
        active = False
        continue

    processc(c)
    time.sleep(0.1)