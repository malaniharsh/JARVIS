import speech_recognition as sr
import webbrowser
import pyttsx3
import wikipedia
import requests 
import datetime
import mscl
import pywhatkit
import os 
import google.generativeai as genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()
news = "28580f9d92e344e6b4007d0a29c3abc8"
api = "AIzaSyCchvDClOJEod_8xIAjs7XNNjyxuFOG6Mw"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    
    elif hour >=12 and hour<18:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

def ai(c):
    c = processCommand().lower()

    genai.configure(api_key=api)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(c)
    print(response.text)


def processCommand(c):
    

    if "who is the jarvis" in c.lower():
        speak("jarvis is the virtual assistant who can do your work as google mini or alexa and also can your more work")
    
    if "open google" in c.lower():
        speak("google is opening")
        webbrowser.open("google.com")

    if "open youtube" in c.lower():
        speak("youtube is opening")
        webbrowser.open("youtube.com")

    if "open facebook" in c.lower():
        speak("facebook is opening")
        webbrowser.open("facebook.com")

    if "open link in" in c.lower():
        speak("linkedin is opening")
        webbrowser.open("linkedin.com")

    if 'wikipedia' in c.lower():
        speak("wikipedia is searching...")
        c = c.replace("wikipedia","")
        results = wikipedia.summary(c, sentences=5)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    if c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = mscl.music[song]
        webbrowser.open(link)

    if  "search" in c.lower():
       sq = c.replace("search","").strip()
       speak(f"jarvis is searching for {sq} on google")
       pywhatkit.search(sq)


    if 'news' in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            speak("the news is")

            for article in articles:
                speak(article['title'])
    
    if 'time' in c.lower():
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Time is {time}")
        print(f"Time is {time}")

    if 'open darshan' in c.lower():
        speak("opening darshan ums...")
        webbrowser.open("darshanums.in/StudentPanel/StudentDashboard.aspx")

    if 'open darshan university' in c.lower():
        speak("opening darshan university website...")
        webbrowser.open("darshan.ac.in")

    if "speak english" in c.lower():
        speak("yes i'm very well speak english and 10 more languages")

    if "speak chinese" in c.lower():
        speak("yes,嗨,吾贾维斯也,子无恙乎?")

    if 'jarvis power off' in c.lower():
        speak("jarvis is the exit from the command")
        exit()

    else :
        ai(c.lower())


if __name__ == "__main__":
    wishMe()
    speak("jarvis is initializing......")
    while True:
        #listen for the wake word jarvis
        #obtain aubio from the microphone
        r = sr.Recognizer()

        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("say something")
                audio = r.listen(source,timeout=3,phrase_time_limit=2)
            query = r.recognize_google(audio,language='en-in')
            print("user said this:\n",query)
            if "jarvis" in query.lower():
                speak("Yes Sir, How may i help you")
                #listen for the command
                with sr.Microphone() as source:
                    print("jarvis is activate")
                    audio = r.listen(source)
                    c = r.recognize_google(audio,language='en-in')

                    processCommand(c)

        except Exception as e:
            print("Error;{0}".format(e))







