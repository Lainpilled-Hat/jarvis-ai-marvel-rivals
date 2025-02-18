import speech_recognition as sr
import time
import pyttsx3
from pynput.keyboard import Controller, Key

keyboard = Controller()
engine = pyttsx3.init()

time.sleep(1)

# engine.say("Typing A")
# engine.runAndWait()
# keyboard.press('A')
# keyboard.release('A')
def contains_word(word):
    return text.contains(word)
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something!")
    audio = r.listen(source)
    try:
            text = r.recognize_google(audio)
            print("You said " + text)
            if text.contains("Jarvis"):
                lines = text.split()
                if any(contains_word(keyword)) for keyword in ["send", "chat", "in chat", "text", "match", "maths", "math", "teen", ]:
                    target_team = None
                    if contains_word("team") or contains_word("teen"):


    except sr.UnknownValueError:
        print("I couldn't understand you, ma'am")
    except sr.RequestError as e:
        print("could not request results from google; {0}".format(e))

def send_message(message, team):
 pass
