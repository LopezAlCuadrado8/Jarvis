import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('listening')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)
        
    try:
        print('recognizing')
        query = r.recognize_google(audio, language='es')
        print(f"user said: {query}")
    except Exception as e:
        return "no"
    
    return query.lower()

text = takecommand()

speak (text)