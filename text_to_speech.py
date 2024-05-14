import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', 'sapi5')
    engine.setProperty("rate", "rate-70")
    engine.say(text)
    engine.runAndWait()

                
