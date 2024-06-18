import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recongnizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
  
  
def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open brave" in c.lower():
        webbrowser.open("https://brave.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
  
if __name__ == "__main__":
    speak("Initializing Jarvis")
    
   
    while True:
        r = sr.Recognizer()
        try:
            # Obtain Audio from the Microphone
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2, phrase_time_limit=1, )
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Boss")
                with sr.Microphone() as source:
                    print("Jarvice Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    processCommand(command)
                    
                 
        except Exception as e:
                print(e)