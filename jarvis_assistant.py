import pyttsx3
import webbrowser
import datetime
import speech_recognition as sr
import wikipedia
import sys
import time
import pyautogui
import subprocess
import random

# import openai
# Needed only if you are using OpenAI's developer API

from rich.console import Console
import shutil
#research webdriver package


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
console = Console()

def speak(audio):
    """ Provides an audio output to the user """
    engine.say(audio)
    engine.runAndWait()

def center(text):
    """ Provides the text after left padding it as per the terminal size"""
    terminal_width = shutil.get_terminal_size().columns
    indentation = (terminal_width - len(text)) // 2
    return(" " * indentation + text)


def wishme():
    """ Welcomes a user to the program """
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        console.print(center("Good Morning Sir!"), style = "color(13)")
        speak("Good Morning Sir!")
    elif hour>=12 and hour<17:
        console.print(center("Good Afternoon Sir!"), style = "color(13)")
        speak("Good Afternoon Sir!")
    else:
        console.print(center("Good Evening Sir!"), style = "color(13)")
        speak("Good Evening Sir!")

    console.print(center("I am Jarvis. How may I assist you?"), style = "color(13)")
    speak("I am Jarvis. How may I assist you?")


def closer():
    """ Terminates the Voice assistant """
    console.print(center("Thank You!"), style = "color(13)")
    speak("Thank You!")
    sys.exit()


def takecommand():
    """ Takes microphone input from the user and returns string """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        console.print(center("Listening....."), style = "color(51)")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    
    try:
        console.print(center("Recognizing...."), style = "color(51)")
        query = r.recognize_google(audio, language = 'en-in')
        console.print(center("User said: "+ query.title()), style = "bold red")
    except Exception as e:
        # console.print(e)
        console.print(center("Please say that again."), style = "bold red")
        return "None"
    return query


def reinitiate():
    """ Asks the user for a new input after completing the given task"""
    console.print(center("How can I help you further?"), style = "color(13)")
    speak("How can I help you further?")


if __name__ == "__main__":
    wishme()
    while True: 
        query = takecommand().lower()


        if query == 'exit' or query in 'terminate' or 'stop' in query:
            closer()
            

        elif 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 2)
            speak(center("According to Wikipedia,"))
            if len(results) > shutil.get_terminal_size().columns:
                for i in range(0, len(results), shutil.get_terminal_size().columns):
                    console.print(center(results[i:i+shutil.get_terminal_size().columns]))
            speak(results)
            reinitiate()


        elif 'open youtube' in query:
            console.print("What would you like to watch?")
            speak("What would you like to watch?")
            search = takecommand().lower()
            console.print("Opening Youtube....")
            speak("Opening Youtube....")
            webbrowser.open("youtube.com")
            time.sleep(5)
            pyautogui.write('/')
            time.sleep(1)
            pyautogui.write(search, interval = 0.1)
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(2)
            closer()

    
        elif 'open Google' in query:
            webbrowser.open("google.com")
            console.print("Opening Google...")
            speak("Opening Google...")
            time.sleep(1.5)
            closer()
        

        elif 'play music' in query or 'spotify' in query:
            console.print("What song would you like to listen to?")
            speak("What song would you like to listen to?")
            song = takecommand().lower()
            console.print("Opening Spotify....")
            speak("Opening Spotify....")
            subprocess.run('spotify.exe', shell=True, check=True)
            time.sleep(7)
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(1.5)
            pyautogui.write(song, interval = 0.1)
            time.sleep(2)
            # the below command might need modification based on the user's Spotify version
            # An alternative solution might be to allow the user to open spotify but then the user can manually 
            # find and play the song of their choice 
            for key in ['enter', 'pagedown', 'tab', 'enter', 'enter', 'enter']:
                pyautogui.press(key)
                time.sleep(0.2)
            time.sleep(1)
            closer()

        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime('%H%M%S')
            speak(f"Sir, the time is {strtime[:2]} hours, {strtime[2:4]} minutes")
            console.print(f"Sir, the time is {strtime}")
            reinitiate()

        # Avoid using the below conditional as 
        # 1) it would require the user to change the hotkeys
        # 2) and there is a chance that the Assistant might send the message to the wrong person 
        # or might even send a wrong message
        # Allowing such a preliminary (mostly hardcoded) assistant to access Whatsapp is never a good idea

        # elif 'send message' in query or 'whatsapp' in query:
        #         console.print("Who will be the recipient?")
        #         speak("Who will be the recipient?")
        #         recipient = takecommand().lower()
        #         console.print("What will be the message?")
        #         speak("What will be the message?")
        #         msg = takecommand().title()
        #         console.print("Opening Whatsapp....")
        #         speak("Opening Whatsapp....")
        #         pyautogui.hotkey('winleft', '3')
        #         time.sleep(15)
        #         pyautogui.write(recipient, interval = 0.1)
        #         time.sleep(0.5)
        #         pyautogui.press('enter')
        #         time.sleep(1.5)
        #         pyautogui.write(msg, interval = 0.1)
        #         console.print("Press enter to send")
        #         speak("Press enter to send")
        #         time.sleep(1)
        #         closer()


        elif 'joke' in query:
            f = open(r"jokes.txt", "r", encoding='utf-8')
            jokes = f.readlines()
            f.close()
            number = random.randint(0, len(jokes)-1)
            l = jokes[number].split("<>")
            console.print(l[0].strip())
            speak(l[0])
            time.sleep(0.1)
            console.print(l[1].strip())
            speak(l[1])
            closer()

        # the below conditional needs to be completed by adding in a ChatGPT (or any other AI)'s developer API
        # the user can then give commands like "Using Artificial Intelligence, suggest me names for X"
        # Avoid directly inputting your API, I would suggest writing your API into a text/CSV file, and reading it
        # directly from the file 

        # Refer https://platform.openai.com/docs/api-reference/introduction?lang=python
        # to understand how to use OpenAI's developer API
        elif "ai" in query or "artificial intelligience" in query:
            pass

        # All the other conditions for now are being handled by this else loop
        # Futher advancements can be made on the project by adding more elif(s) or 
        # deciding a better method of handling the else cases 
        else:
            console.print("Sorry sir, I cannot help you with that")
            speak("Sorry sir, I cannot help you with that")
            reinitiate()