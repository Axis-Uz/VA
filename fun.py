import subprocess
import time
from turtle import end_fill
import pyttsx3 as tts
import speech_recognition as sr
import PyDictionary as pyd
from email.message import EmailMessage
from newsapi import NewsApiClient
import datetime
import requests
import wikipedia
import webbrowser
import os
import json
import smtplib
import ssl
import randfacts
import wolframalpha
import re
import dadjokes
import random
import winshell
import socket
from termcolor import cprint, colored


def storeWeather():
    open_weather = stored_API["openweather"]
    stored_date = json.load(open("data/weather.json"))['date']
    today = str(datetime.datetime.now().date())
    if stored_date == today:
        return
    else:
        location = settings['city'].strip()

        weather_data = requests.get(
            open_weather['url']+location+"&appid="+open_weather['client']).json()
        dump_weather = {}
        dump_weather.setdefault('date', str(datetime.datetime.now().date()))
        dump_weather.setdefault('weather', weather_data["main"])
        dump_weather.setdefault(
            'description', weather_data["weather"][0]["main"])
        dump_weather.setdefault('wind-speed', weather_data["wind"]["speed"])
        dump_weather.setdefault('wind-angle', weather_data["wind"]["deg"])
        dump_weather.setdefault('city', weather_data["name"])
        json.dump(dump_weather, open("weather.json", "w"), indent=4)


def getVoice():
    for k in voices.keys():
        if voices[k]['default'] == "true":
            return voices[k]


user_profile = json.load(open('data/user_profile.json'))["user"]
contacts = json.load(open('data/user_profile.json'))["contacts"]
settings = json.load(open("data/va_settings.json"))
voices = json.load(open("data/voices.json"))
voice = getVoice()
stored_Websites = settings["websites"]
stored_API = json.load(open("data/api.json"))


commands = json.load(open("data/commands.json"))
for k, v in commands.items():
    commands[k] = list(map(lambda x: x.lower().strip(), v))


engine = tts.init('sapi5')
engine.setProperty('rate', 500)  # Normal 150~250
engine.setProperty('voice', voice['id'])


def speak(text, color_passed='green'):  # Uzair
    """Inputted text is spoken"""
    if type(text) == str:
        text = " ".join([w.capitalize() for w in text.split(" ")]).strip()

    engine.say(text)
    cprint(text=voice["callName"].capitalize()+": ",
           color="yellow", attrs=['bold'], end='')
    print(colored(text, color_passed))
    engine.runAndWait()


def updateVoices():
    """Updates the voices available"""
    x = {}
    voices = engine.getProperty('voices')
    for i, v in enumerate(voices):
        x.setdefault(i, {})
        x[i]["name"] = v.name
        x[i]["id"] = v.id
        x[i]["default"] = "false"
        x[i]["index"] = i
        x[i]["callName"] = v.name.split(" ")[1]
    x[1]["default"] = "true"
    json.dump(x, open("data/voices.json", "w"), indent=4)


def wishMe():
    """Greet the User"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! ")
    else:
        speak("Good Evening!")

    speak("I am "+voice['callName'] +
          ". Please tell me how may I help you")


def acceptCommand():  # Uzair
    """Accepts the user's command via the microphone and returns the string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # TODO Earphone
        r.energy_threshold = 10000
        cprint("Listening...🎙️", 'yellow', attrs=['blink'])
        r.adjust_for_ambient_noise(source, duration=0.5)
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language=settings["language"])
            cprint(text=user_profile["name"]+": ",
                   color="blue", attrs=["bold"], end="")
            cprint(text=query, end="\n")
        except Exception as e:
            speak("Unable to recognize your voice. Please say that again...")
            return "None"
    return query.lower()


def sendMail(query):  # Varun
    """Send Mail"""
    sender = user_profile["email"]
    password = user_profile["password"]
    for c in commands["email"]:
        if c in query:
            query = query.replace(c, "").strip()
            if contacts.__contains__(query):
                receiver = contacts[query]['email']
                break
            else:
                receiver = str(input("Receiver ?"))

    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = str(input("Subject:"))
    em.set_content(str(input("Content: ")))

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, em.as_string())
            speak("Mail Sended")
    except Exception as e:
        speak("Unable to Send the Mail !!")


def searchWikipedia(query):  # Anurag
    """Searches Wikipedia for the user's query"""
    for c in commands['search']:
        if c in query:
            query = query.replace(c, "")
            break
    q = wikipedia.search(query)[0]
    results = wikipedia.summary(q, sentences=1, auto_suggest=False)
    speak(q+", According to Wikipedia")
    speak(results)


def getFacts():  # Harsh
    """Returns a random fact"""
    speak("Here is a random fact")
    speak(randfacts.get_fact())


def getJokes():  # Harsh
    """Returns a random joke"""
    speak("Here is a random joke")
    joking = dadjokes.Dadjoke()
    speak(joking.joke)


def playMusic(query):  # Rhea
    """Plays music from the user's directory"""
    music_dir = json.load(open("data/user_profile.json"))["music-dir"]
    songs = [s.lower() for s in os.listdir(music_dir)]

    for c in commands['music']:
        if query.__contains__(c):
            query = query.replace(c, '').strip()
            break

    if query+".mp3" in songs:
        speak("Playing Music")
        os.startfile(music_dir+"\\" + query + ".mp3")
    elif query == '':
        speak("Playing Music")
        os.startfile(music_dir+"\\"+random.choice(songs))
    else:
        speak("I don't know that song")


def playYouTube(query):  # Rhea
    """Plays a YouTube video from the user's query"""
    for c in commands['youtube']:
        if c in query:
            query = query.replace(c, '')
            break
    query = query.strip().replace(' ', '+')
    try:
        webbrowser.open(
            "https://www.youtube.com/results?search_query=" + query)
    except Exception as e:
        speak("Unable to play youtube, please try again.")


def solveProblems():  # Harsh
    """Perform basic problems solving"""
    client = wolframalpha.Client(stored_API["wolframalpha"]["client"])
    speak("What do you want to ask ?")
    solve_query = acceptCommand()
    response = client.query(solve_query)
    try:
        answer = next(response.results).text
        speak(answer)
    except Exception as e:
        speak("Unable to solve, please try again")


def useDictionary(query):  # Rhea
    """Get Meaning, Synonyms, Antonyms"""
    dictionary = pyd.PyDictionary()
    for c in commands["dictionary"]:
        if c in query:
            query = query.replace(c, "")
            break
    try:
        result = dictionary.meaning(query)
        speak("According to dictionary,")
        for k, v in result.items():
            print("> "+k+": "+"\n\t>".join(v))
    except Exception as e:
        speak("I don't know that")


def openWebsite(query):  # Varun
    """Opens a website from the user's query"""
    for c in commands['website']:
        if c in query:
            website = query.replace(c, "").strip()
            break
    if stored_Websites.__contains__(website):
        webbrowser.open(stored_Websites[website])
    else:
        speak("I don't know that website.")


def getNews():  # Anurag
    "Return Top 3 Headlines"
    client = NewsApiClient(api_key=stored_API['news']['client'])
    top_art = client.get_top_headlines(
        country="in", language=settings["language"])['articles']
    title = [t['title'].split("-") for t in top_art][0:3]
    speak("These are top three headlines: ")
    engine.setProperty('rate', 200)
    for t in title:
        speak(t[0]+"from"+t[1])
    engine.setProperty('rate', 150)

# TODO Lock Screen --> #Sarthak
# TODO Bin --> #Anurag
# TODO Notes --> #Varun


def retrieveWeather(query):
    weatherData = json.load(open("data/weather.json"))
    today = str(datetime.datetime.now().date())
    if weatherData["date"] == today:
        location = settings['city'].strip()
        qk = parseQuery(query)
        for c in commands['weather']:
            if c in query:
                query = query.replace(c, '').strip()
        speak("Today's Forecast For "+location.capitalize()+" is: ")
        speak("Min Temperature: " +
              str(weatherData['weather']['temp_min'])+" Kelvin")
        speak("Max Temperature: " +
              str(weatherData['weather']['temp_max'])+" Kelvin")
        speak("Humidity: "+str(weatherData['weather']['humidity'])+"%")
        speak("Description:"+str(weatherData['description']))
        if query == "verbose":
            speak("Wind Speed: "+str(weatherData["wind-speed"]))
            speak("Wind Angle: "+str(weatherData["wind-angle"]))
            speak("Atmospheric Pressure: " +
                  str(weatherData["weather"]["pressure"])+" millibar")
    else:
        speak("Unable to Forecast,Cause of Rain & Showers I Guess.")


def getTime():  # Sarthak
    """Return Current Time"""
    speak("The Time is "+datetime.datetime.now().strftime("%H:%M"))


def getDate():  # Sarthak
    "Return Today Date"
    speak("Today's Date is "+str(datetime.datetime.now().date()))


def lockWin():
    '''Locks the Device'''
    speak("Locking the Device")
    subprocess.call('rundll32.exe user32.dll, LockWorkStation')


def goToSleep():
    '''Go to Sleep'''
    speak("For how much time you want to stop from listening commands ?")
    time.sleep(int(acceptCommand()))


def emptyBin():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
    speak("Emptied Recycle Bin")


def parseQuery(query):
    "Maps the Query with the Appropriate Function"
    query_key = ''
    for k, c in commands.items():
        for v in c:
            if re.findall(v, query):
                query_key = k
                return query_key


def isConnected():
    try:
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False
