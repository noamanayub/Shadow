import pyttsx3
import time

def speak(text, delay=10):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    time.sleep(delay)
    
if __name__ == "__main__":
    speak("Hello Shadow, What can I help you with?", delay=0)
    input_text = input("Your request: ")
    speak("Okay, if you need any help, feel free to ask.", delay=0)
    input_text = input("Your request: ")
    speak("Its my pleasure, to assist you", delay=0)