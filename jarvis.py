import speech_recognition as sr
import time
import pyttsx3
from pynput.keyboard import Controller, Key

keyboard = Controller()
engine = pyttsx3.init()

time.sleep(1)

engine.say("Typing A")
engine.runAndWait()
keyboard.press('A')
keyboard.release('A')
def speech_Rec():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source)

        try:
            print("You said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("I couldn't understand you, ma'am")
        except sr.RequestError as e:
            print("could not request results from google; {0}".format(e))


