import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action (send):
      user_data = send

      if "What is your name " in user_data :
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"

      elif "hello" in user_data or "hye" in user_data :
        text_to_speech.text_to_speech("Hey , sir How i can help you")
        return "Hey , sir How i can help you"

      elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return "good morning sir"

      elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :" , (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time



      elif "shutdown" in user_data:
       text_to_speech.text_to_speech("Ok sir")
       return "Ok sir"

      elif "play music" in user_data :
       webbrowser.open("https://open.spotify.com/")
       text_to_speech.text_to_speech("Opening spotify , enjoy your songs")
       return "Opening spotify , enjoy your songs"


      elif "play youtube" in user_data :
       webbrowser.open("https://youtube.com/")
       text_to_speech.text_to_speech("Opening youtube , enjoy your time")
       return "Opening youtube , enjoy your time"


      elif "open google" in user_data :
       webbrowser.open("https://google.com")
       text_to_speech.text_to_speech("Opening google")
       return "Opening google"
      

      elif "Weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

      else:
       text_to_speech.text_to_speech("I am not able to understand")
       return "I am not able to understand"
 