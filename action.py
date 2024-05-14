import datetime
import webbrowser
import requests
import wikipedia
import pyttsx3
import time
from requests_html import HTMLSession


class Action:
    def __init__(self, user_input):
        self.user_input = user_input
        

    def handle_action(self):

         
        if "what is your name" in self.user_input:
           self.text_to_speech("My name is virtual assistant")
           return "My name is virtual assistant"

        elif "hello" in self.user_input or "hi" in self.user_input:
           self.text_to_speech("Hey, sir. How can I help you?")
           return "Hey, sir. How can I help you?"

        elif "search" in self.user_input:  # Example trigger for API search
            query = self.user_input.replace("search", "").strip()
            api_response = self.search_api(query)
            self.text_to_speech(api_response)
            return api_response
        
        elif "good morning" in self.user_input:
          return "Good morning, sir"
        
        elif "time" in self.user_input:
         current_time = datetime.datetime.now()
         time_str = f"Hour: {current_time.hour}, Minute: {current_time.minute}"
         self.text_to_speech(time_str)
         return time_str

        elif "shutdown" in self.user_input:
         return "Ok sir"

        elif "spotify" in self.user_input:
         webbrowser.open("https://open.spotify.com/")
         self.text_to_speech("Opening Spotify, enjoy your songs")
         return "Opening Spotify, enjoy your songs"
        
        elif "jio saavn" in self.user_input:
         webbrowser.open("https://www.jiosaavn.com/new-releases")
         self.text_to_speech.text_to_speech("Opening Jio Saavn, enjoy your songs")
         return "Opening Jio Saavn, enjoy your songs"
        
        elif "YouTube music" in self.user_input:
         webbrowser.open("https://music.youtube.com/")
         self.text_to_speech("Opening YouTube music, enjoy your songs")
         return "Opening YouTube music, enjoy your songs"
        
        elif "YouTube" in self.user_input:
         webbrowser.open("https://youtube.com/")
         self.text_to_speech("Opening YouTube, enjoy your time")
         return "Opening YouTube, enjoy your time"
        
        elif "Apple music" in self.user_input:
         webbrowser.open("https://music.apple.com/us/browse")
         self.text_to_speech("Opening Apple music, enjoy your time")
         return "Opening Apple music, enjoy your time"

        elif "Google" in self.user_input:
         webbrowser.open("https://google.com")
         self.text_to_speech("Opening Google")
         return "Opening Google"

        elif "weather" in self.user_input:
         ans = self.weather()
         self.text_to_speech(ans)
         return ans

        elif "not feeling well" in self.user_input:
         webbrowser.open("https://open.spotify.com/")
         self.text_to_speech("Listen to some songs to freshen up your mood")
         return "Listen to some songs to freshen up your mood"

        # elif "depressed" or "depression" in self.user_input:
        #  webbrowser.open("https://youtu.be/eAK14VoY7C0?si=WK1ULquYH__yrqrd")
        #  self.text_to_speech("Watch this video by Sandeep Maheshwari to overcome depression")
        #  return "Watch this video by Sandeep Maheshwari to overcome depression"
        
        elif "movie" in self.user_input:
         webbrowser.open("https://www.imdb.com/chart/top/?ref_=ext_shr_lnk")
         self.text_to_speech("here are your top rated movies")
         return "here are your top rated movies"
        
        elif "cook" in self.user_input:
         webbrowser.open("https://www.wikihow.com/Cook")
         self.text_to_speech("here is your recipe book")
         return "here is your recipe book"
        
        elif "news" in self.user_input:
         webbrowser.open("https://edition.cnn.com/")
         self.text_to_speech("here are some new updates")
         return "here are some new updates"
        
        elif "bored" in self.user_input:
         webbrowser.open("https://mashable.com/article/fun-websites-improve-skills")
         self.text_to_speech("here you can learn some new skills")
         return "here you can learn some new skills"
        
        elif "upset" in self.user_input:
         self.text_to_speech("i am sorry to hear that you are feeling upset.i am there to listen to you,you can share me anything")
         return "i am sorry to hear that you are feeling upset.i am there to listen to you,you can share me anything"
        
        elif "Sleep Schedule" in self.user_input:
         self.text_to_speech("1.Adjust your bedtime, but be patient\n 2.Do not take a nap, even if you feel tired \n 3.Do exercise regularly\n 4.Do not use phone before you go to sleep")
         return "1.Adjust your bedtime, but be patient\n 2.Do not take a nap, even if you feel tired \n 3.Do exercise regularly\n 4.Do not use phone before you go to sleep"
        
        elif "I am bored" in self.user_input:
         self.text_to_speech("Tell me, What's something that always makes you laugh?")
         return "Tell me, What's something that always makes you laugh?"
        
        elif "artificial intelligence" in self.user_input:
         self.text_to_speech(" I find it very fascinating! and i am very curious about ai .The advancements in AI have opened up so many possibilities across various fields.Also,I feel you should explore more about it")
         return " I find it very fascinating! and i am very curious about ai .The advancements in AI have opened up so many possibilities across various fields.Also,I feel you should explore more about it"
         
        elif "Tell me about a hobby or interest you're passionate about" in self.user_input:
         self.text_to_speech("i love talking to different people and know about them, explore them")
         return "i love talking to different people and know about them, explore them"
        
        elif "What's the most memorable book or movie you've experienced?" in self.user_input:
         self.text_to_speech(f"Oh, I've experienced so many amazing books and movies! It's hard to pick just one as the most memorable. But if I had to choose, I'd say {"The Shawshank Redemption"} is definitely up there. It's a powerful story about hope, friendship, and redemption. Have you seen it or read the book?")
         return "Oh, I've experienced so many amazing books and movies! It's hard to pick just one as the most memorable. But if I had to choose, I'd say The Shawshank Redemption is definitely up there. It's a powerful story about hope, friendship, and redemption. Have you seen it or read the book?"
        
        elif "book"in self.user_input:
         self.text_to_speech(f"I have so many favorite books, but one that really stands out to me is {"To Kill a Mockingbird"} by Harper Lee. It's a classic that explores important themes like justice, racism, and empathy. The characters are so well-written and the story is incredibly moving. Have you read it?")
         return "I have so many favorite books, but one that really stands out to me is To Kill a Mockingbird by Harper Lee. It's a classic that explores important themes like justice, racism, and empathy. The characters are so well-written and the story is incredibly moving. Have you read it?"
        
        elif "movie"in self.user_input:
         self.text_to_speech(f"Oh, I have so many favorite movies! It's hard to pick just one. But if I had to choose, I'd say {"The Lord of the Rings"} trilogy is definitely at the top of my list. The epic adventure, the stunning visuals, and the amazing characters make it a truly unforgettable cinematic experience. Have you seen any of the movies from {"The Lord of the Rings"} series?")
         return "Oh, I have so many favorite movies! It's hard to pick just one. But if I had to choose, I'd say The Lord of the Rings trilogy is definitely at the top of my list. The epic adventure, the stunning visuals, and the amazing characters make it a truly unforgettable cinematic experience. Have you seen any of the movies from The Lord of the Rings series?"
        
        elif "Share a challenging situation you've overcome recently"in self.user_input:
         self.text_to_speech("I recently had to manage multiple deadlines at work, but I managed to prioritize tasks and stay organized to meet all the requirements on time.How about you?Have you faced any challenging situations lately?")
         return "I recently had to manage multiple deadlines at work, but I managed to prioritize tasks and stay organized to meet all the requirements on time.How about you?Have you faced any challenging situations lately?"
        
        elif "travel"in self.user_input:
         self.text_to_speech("Oh, I absolutely love traveling! It's hard to pick just one favorite destination, but if I had to choose, I'd say Bali is definitely up there. The beautiful beaches, lush green landscapes, and vibrant culture make it such a magical place to visit. Plus, the food is absolutely delicious! Have you ever been to Bali or any other travel destination that you really enjoyed?")
         return "Oh, I absolutely love traveling! It's hard to pick just one favorite destination, but if I had to choose, I'd say Bali is definitely up there. The beautiful beaches, lush green landscapes, and vibrant culture make it such a magical place to visit. Plus, the food is absolutely delicious! Have you ever been to Bali or any other travel destination that you really enjoyed?"
        
        elif "dream"in self.user_input:
         self.text_to_speech("I dreamt of flying over a surreal landscape filled with floating islands and colorful creatures. It felt like a magical adventure!.Have you had any exciting or memorable dreams lately? ")
         return "I dreamt of flying over a surreal landscape filled with floating islands and colorful creatures. It felt like a magical adventure!.Have you had any exciting or memorable dreams lately?"
        
        elif "What's a skill or talent you're currently working on improving?"in self.user_input:
         self.text_to_speech("I'm working on improving my coding skills. Learning new programming languages and techniques is both challenging and rewarding.Additionally,i am also try to improve myself to answer your questions more efficiently")
         return "I'm working on improving my coding skills. Learning new programming languages and techniques is both challenging and rewarding.Additionally,i am also try to improve myself to answer your questions more efficiently"
        
        elif "Tell me about a meaningful friendship or relationship in your life"in self.user_input:
         self.text_to_speech("My friendship with my childhood friend has been incredibly meaningful. We've gone through many ups and downs together and always supported each other.")
         return "My friendship with my childhood friend has been incredibly meaningful. We've gone through many ups and downs together and always supported each other."
        
        elif "What's something that always makes you laugh?"in self.user_input:
         self.text_to_speech("Watching comedy sketches or stand-up specials never fails to make me burst into laughter. Watching them is such a great way to lighten the mood! what about you?")
         return "Watching comedy sketches or stand-up specials never fails to make me burst into laughter. Watching them is such a great way to lighten the mood! what about you?"
         
        elif "Share a piece of advice that has had a significant impact on you."in self.user_input:
         self.text_to_speech(f"{"Embrace change and challenges as opportunities for growth."} This advice has encouraged me to face new experiences with a positive mindset. Do you have any favorite advice or words of wisdom that have influenced you?")
         return "Embrace change and challenges as opportunities for growth.This advice has encouraged me to face new experiences with a positive mindset. Do you have any favorite advice or words of wisdom that have influenced you?"
        
        elif "What's your favorite type of music, and why does it resonate with you?"in self.user_input:
         self.text_to_speech("Oh, I love all kinds of music! It's hard to pick just one favorite type. I enjoy listening to pop, rock, and even some R&B. Music has a way of connecting with our emotions and making us feel alive. It can lift my spirits when I'm feeling down or help me celebrate when I'm happy. Plus, it's a great way to express myself and connect with others. What about you? What's your favorite type of music?")
         return "Oh, I love all kinds of music! It's hard to pick just one favorite type. I enjoy listening to pop, rock, and even some R&B. Music has a way of connecting with our emotions and making us feel alive. It can lift my spirits when I'm feeling down or help me celebrate when I'm happy. Plus, it's a great way to express myself and connect with others. What about you? What's your favorite type of music?"
        
        elif "Describe a memorable vacation you've been on and what made it special."in self.user_input:
         self.text_to_speech("Oh, I had an amazing vacation last year! I went to the Maldives, and it was absolutely breathtaking. The crystal-clear turquoise waters, white sandy beaches, and vibrant coral reefs made it a tropical paradise. It was like swimming in an aquarium!. Have you been on any unforgettable vacations?")
         return "Oh, I had an amazing vacation last year! I went to the Maldives, and it was absolutely breathtaking. The crystal-clear turquoise waters, white sandy beaches, and vibrant coral reefs made it a tropical paradise. It was like swimming in an aquarium!. Have you been on any unforgettable vacations?"
        
        elif "Share a meaningful quote or saying that inspires you."in self.user_input:
         self.text_to_speech(f"One quote that inspires me is {"The only way to do great work is to love what you do"} by Steve Jobs. It reminds me to pursue my passions and find fulfillment in my work. When we love what we do, it doesn't feel like work at all, and we can achieve great things. It's a reminder to follow our hearts and strive for excellence in everything we do. Is there a quote or saying that inspires you?")
         return "One quote that inspires me is The only way to do great work is to love what you do by Steve Jobs. It reminds me to pursue my passions and find fulfillment in my work. When we love what we do, it doesn't feel like work at all, and we can achieve great things. It's a reminder to follow our hearts and strive for excellence in everything we do. Is there a quote or saying that inspires you?"
        
        elif "What's your favorite type of cuisine, and do you enjoy cooking?"in self.user_input:
         self.text_to_speech("Oh, I absolutely love trying different types of cuisine! Indian cuisine holds a special place in my heart, with its rich flavors and diverse range of dishes.I adore Italian cuisine, especially pasta dishes and pizza. Cooking is a therapeutic activity for me, and experimenting with new recipes is always fun.How about you? Do you enjoy cooking or have a favorite type of cuisine?")
         return "Oh, I absolutely love trying different types of cuisine! Indian cuisine holds a special place in my heart, with its rich flavors and diverse range of dishes.I adore Italian cuisine, especially pasta dishes and pizza. Cooking is a therapeutic activity for me, and experimenting with new recipes is always fun.How about you? Do you enjoy cooking or have a favorite type of cuisine?"
        
        elif "What's something you do to unwind and relax after a long day?"in self.user_input:
         self.text_to_speech("After a long day, one of my favorite ways to unwind is to curl up with a good book. There's something so soothing about getting lost in a different world and letting my imagination roam free. It helps me relax, escape from the stresses of the day, and recharge for the next day.Also,I enjoy taking long walks in nature or listening to calming music to unwind and clear my mind. It helps me recharge and find inner peace. How about you? What do you like to do to unwind after a long day?")
         return "After a long day, one of my favorite ways to unwind is to curl up with a good book. There's something so soothing about getting lost in a different world and letting my imagination roam free. It helps me relax, escape from the stresses of the day, and recharge for the next day.Also,I enjoy taking long walks in nature or listening to calming music to unwind and clear my mind. It helps me recharge and find inner peace. How about you? What do you like to do to unwind after a long day?"
      
        elif "Describe a recent act of kindness you've witnessed or experienced."in self.user_input:
         self.text_to_speech(" I saw a stranger help an elderly person carry groceries, showcasing the power of kindness and empathy in everyday interactions.what about did you help somebody recently?")
         return " I saw a stranger help an elderly person carry groceries, showcasing the power of kindness and empathy in everyday interactions.what about did you help somebody recently?"
        
        elif "What's a skill or hobby you've always wanted to learn but haven't had the chance to yet?"in self.user_input:
         self.text_to_speech("Oh, there are so many skills and hobbies I've always wanted to learn! One that comes to mind is playing the guitar. I've always admired people who can strum beautiful melodies and create music with their fingertips. It's such a versatile instrument, and I think it would be a wonderful way to express myself creatively. Maybe one day I'll find the time to pick up a guitar and start learning. Is there a skill or hobby you've been wanting to try?")
         return "Oh, there are so many skills and hobbies I've always wanted to learn! One that comes to mind is playing the guitar. I've always admired people who can strum beautiful melodies and create music with their fingertips. It's such a versatile instrument, and I think it would be a wonderful way to express myself creatively. Maybe one day I'll find the time to pick up a guitar and start learning. Is there a skill or hobby you've been wanting to try?"
        
        elif "Tell me about a childhood memory that still brings a smile to your face"in self.user_input:
         self.text_to_speech(" I remember building forts with blankets and pillows with my siblings. Those playful moments filled with laughter and imagination are cherished memories.what about did you had any such memory that still makes you smile?")
         return " I remember building forts with blankets and pillows with my siblings. Those playful moments filled with laughter and imagination are cherished memories.what about did you had any such memory that still makes you smile?"
        
        
        elif "Wikipedia" in self.user_input:
          query = self.user_input.replace("Wikipedia", "").strip()
          try:
            result = wikipedia.summary(query, sentences=2)
            self.text_to_speech(result)
            return result
          except wikipedia.DisambiguationError as e:
            result = f"Ambiguous term. Please specify: {', '.join(e.options)}"
          except wikipedia.PageError:
            result = "No Wikipedia page found for the query."
          self.text_to_speech(result)
          return result
        

        else:
            return "I am not able to understand"
        

    def search_api(self, query):
     url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"

     payload = {
	"messages": [
		{
			"role": "user",
			"content":{"query":query}
		}
	],
	"model": "gpt-4-turbo-preview",
	"max_tokens": 200,
	"temperature": 0.9
}
     headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "d19ccafbf7mshb20cf6f021509cfp1dc5d8jsn37542c4371bf",
	"X-RapidAPI-Host": "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com"
  }
     response = requests.post(url, json=payload, headers=headers)
     print(response.json())
    
    def weather(self):
      s = HTMLSession()
      query = "pune"
      url =f"https://www.google.com/search?q=weather+in+{query}"
      r=s.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})
      temp = r.html.find("span#wob_tm" , first= True).text
      unit = r.html.find("div.vk_bk.wob-unit span.wob_t" , first= True).text
      desc= r.html.find("span#wob_dc" , first= True).text
      return temp+" " + unit+" " + desc

    def text_to_speech(self, text):
        engine = pyttsx3.init()
        time.sleep(0.2)
        engine.say(text)
        engine.runAndWait()


        
        

