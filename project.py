import json
import pyttsx3
import speech_recognition as sr
import pyaudio
import random
import datetime
import wikipedia
import webbrowser
import googletrans
import wolframalpha
import os
import smtplib
import pyjokes
import pywhatkit
import pyautogui
import psutil
from urllib.request import urlopen
import requests

gt = googletrans.Translator()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
voiceRate = 175
engine.setProperty('rate',voiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        a = "Hello vinay Good Morning !","Good Morning vinay","Hello vinay good morning","O,good morning sir","O,good morning vinay","Wow welcome back vinay"
        speak(random.choice(a))

    elif hour>=12 and hour<17:
        b = "Hello vinay Good Afternoon !","Good Afternoon vinay","Hello vinay good afternoon","O,good afternoon sir","O,good afternoon vinay","Wow welcome back vinay"
        speak(random.choice(b))

    else:
        c = "Hello vinay Good Evening !","Good Evening vinay","Hello vinay good evening","O,good evenning sir","O,good evening vinay","Wow welcome back vinay"
        speak(random.choice(c))

    speak("I am BirdBrain. Please tell me how may I help you ?")
wishme()
def takeCommand():
    #It takes microphone i/p from the user & returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.energy_threshold = 300
        r.pause_threshold = 1

        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-us')
        print("User said : ", query)

    except Exception as e:
        #print(e)

        speak("Please sir say that again...")
        return "None"
    return query

def takeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.energy_threshold = 300
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print("User said : ", query)

    except Exception as e:
        # print(e)

        speak("Please sir say that again...")
        return "None"
    return query.lower()

app = wolframalpha.Client("PJ33V7-6X4HLX3A9H")



if __name__ == '__main__':

    while True:
        query = takeCommand().lower()

        if 'name' in query:
            speak("Sir my name is Birdbrain & i am your desktop assistant")

        elif 'how are you' in query:
            speak("I am fine sir,thank you for asking. How about you?")




        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to the wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'twitter' in query:
            webbrowser.open("https://twitter.com/?lang=en")

        elif 'telegram' in query:
            webbrowser.open("https://web.telegram.org/")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak("Sir the current time is {strTime}")

        elif 'date' in query:
            strdate = datetime.datetime.now().date()
            speak("Today's date is")
            speak(strdate)

        elif 'day' in query:
            strday = datetime.datetime.now().day
            speak(strday)

        elif 'month' in query:
            strmonth = datetime.datetime.now().month
            speak(strmonth)

        elif 'open python editor' in query:
             os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe")


        elif 'open java editor' in query:
            os.startfile("C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.1\\bin\\idea64.exe")


        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif 'translator' in query:
            speak("Please tell me the line sir")
            line = takeHindi()
            text = gt.translate(line)
            line= text.text
            line=line.lower()
            print(line)
            speak(line)

        elif 'temperature' in query:
            res = app.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)

        elif 'calculate' in query:
            speak("What should I calculate sir ?")
            gh = takeCommand().lower()
            res = app.query(gh)
            print(next(res.results).text)
            speak(next(res.results).text)

        elif 'message' in query:
            speak("What should I send to xyz?")
            say = takeCommand()
            speak('Please tell me time to deliver the message')
            pywhatkit.sendwhatmsg('+91 7829503320',f"{say}",int(input()),int(input()))
            speak("The message has been sent")

        elif 'news' in query:
            try:
               jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&apiKey=94f7df3489b34d9299a7ccdebeb8ffcf''')
               data = json.load(jsonObj)
               i = 1
               speak("Here are some top headlines of India")
               print('''-----------TOP HEADLINES-----------''')
               for item in data['articles']:
                  print(str(i)+' - '+item['title'] + '\n')
                  print(item['description'] + '\n')
                  speak(str(i)+' - '+item['title'] + '\n')
                  i +=1
            except Exception as e:
                print(str(e))


        elif 'quit' in query:
            speak("Thank you sir ! you can call me anytime & have a nice day")

            break
