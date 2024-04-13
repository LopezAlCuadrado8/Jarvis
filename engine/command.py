import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()

speak("india is my country, all indians are my brothers and sisters")