import pyttsx3 
import speech_recognition as sr
import datetime
import screen_brightness_control as src
import wikipedia 
import webbrowser
import os
from pywikihow import search_wikihow
import time
import subprocess
import smtplib
import requests
import pywhatkit
import sys
import pyjokes
import cv2
import pyautogui as pi
from playsound import playsound
from googletrans import Translator
from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning Sir!")
        print("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!") 
        print("Good Afternoon Sir!")  

    else:
        speak("Good Evening Sir!")
        print("Good Evening Sir!")  

    speak("I'm Kiara, your Desktop Assistant.")
    print("I'm Kiara, your Desktop Assistant.")

def date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()

    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 
    print("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')
    speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')  

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])
    f.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 550
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def translation():
    dic = ('afrikaans', 'af', 'albanian', 'sq',
        'amharic', 'am', 'arabic', 'ar',
        'armenian', 'hy', 'azerbaijani', 'az',
        'basque', 'eu', 'belarusian', 'be',
        'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
        'bg', 'catalan', 'ca', 'cebuano',
        'ceb', 'chichewa', 'ny', 'chinese (simplified)',
        'zh-cn', 'chinese (traditional)',
        'zh-tw', 'corsican', 'co', 'croatian', 'hr',
        'czech', 'cs', 'danish', 'da', 'dutch',
        'nl', 'english', 'en', 'esperanto', 'eo',
        'estonian', 'et', 'filipino', 'tl', 'finnish',
        'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
        'gl', 'georgian', 'ka', 'german',
        'de', 'greek', 'el', 'gujarati', 'gu',
        'haitian creole', 'ht', 'hausa', 'ha',
        'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
        'hi', 'hmong', 'hmn', 'hungarian',
        'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
        'id', 'irish', 'ga', 'italian',
        'it', 'japanese', 'ja', 'javanese', 'jw',
        'kannada', 'kn', 'kazakh', 'kk', 'khmer',
        'km', 'korean', 'ko', 'kurdish (kurmanji)',
        'ku', 'kyrgyz', 'ky', 'lao', 'lo',
        'latin', 'la', 'latvian', 'lv', 'lithuanian',
        'lt', 'luxembourgish', 'lb',
        'macedonian', 'mk', 'malagasy', 'mg', 'malay',
        'ms', 'malayalam', 'ml', 'maltese',
        'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
        'mn', 'myanmar (burmese)', 'my',
        'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
        'pashto', 'ps', 'persian', 'fa',
        'polish', 'pl', 'portuguese', 'pt', 'punjabi',
        'pa', 'romanian', 'ro', 'russian',
        'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
        'serbian', 'sr', 'sesotho', 'st',
        'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
        'slovak', 'sk', 'slovenian', 'sl',
        'somali', 'so', 'spanish', 'es', 'sundanese',
        'su', 'swahili', 'sw', 'swedish',
        'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
        'te', 'thai', 'th', 'turkish',
        'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
        'ug', 'uzbek', 'uz',
        'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
        'yiddish', 'yi', 'yoruba',
        'yo', 'zulu', 'zu')
    try:
        trans = "None"
        def source_language():
            print("what do you like to translate?")
            trans = takeCommand().lower()
            while (trans == "None"):
                trans = takeCommand().lower()
            return trans

        trans = source_language()

        def destination_language():
            print("In which language you want to convert : Ex. Hindi , English , etc.")
            to_lang = takeCommand().lower()
            while (to_lang == "None"):
                to_lang = takeCommand().lower()
            return to_lang

        to_lang = destination_language()

    except Exception as e:
        if(to_lang not in dic):
            print("Language in which you are trying \
                to convert is currently not available ,\
                    please input some other language")
            speak("Language in which you are trying \
                to convert is currently not available ,\
                    please input some other language")
            return

    to_lang = dic[dic.index(to_lang)+1]

    translator = Translator()

    text_to_translate = translator.translate(trans, dest=to_lang)

    text = text_to_translate.text

    speak = gTTS(text=text, lang=to_lang, slow=False)

    speak.save("captured_voice.mp3")

    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')
    print(text)

if __name__ == "__main__":
    pwd=input('Enter password')
    while(pwd!="password"):
        print('Invalid password: Please try again')
        pwd=input('Re-enter password: ')
    speak('verification successful')
    wishMe()
    speak('how may I help you')
    user_dir = os.path.expanduser("~")
    while True:
        query = takeCommand().lower()
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song) 
        
        elif 'resume' in query or 'pause' in query:
            pi.press("playpause")

        elif 'previous' in query:
            pi.press("prevtrack")

        elif 'next' in query:
            pi.press("nexttrack")
        
        elif 'time' in query:
            time = str(datetime.datetime.now())
            hr=time[11:13]
            min=time[14:16]
            print(time)
            speak(f"the time is {hr},hours and {min},minutes sir")
        
        elif 'date' in query:
            date()
        
        elif 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/hyderabad")
                speak('Here are some headlines from the Times of India, Happy reading')
                time.sleep(6)

        elif 'make a note' in query:
                text = takeCommand().lower()
                note(str(text))
                speak("file save")
                os.system("taskkill /f /im notepad.exe")

        elif ('bye' in query) or ('quit' in query) or ('stop' in query)or ('close' in query) or('exit' in query):
            speak('Have a good day Sir, See you again')
            sys.exit()
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "siddhaarth.4u@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")
                print("Sorry. I am not able to send this email")
        
        elif 'day brightness' in query:
            src.fade_brightness(0)
            src.fade_brightness(95, start=0)
            speak("Brightness is adjusted  , enjoy the day screen light master")
        
        elif 'night brightness' in query:
            src.fade_brightness(0)
            src.fade_brightness(25, start=0)
            speak("Brightness is adjusted , Take care,yourself master")
        
        elif (('my location' in query) or ('where am i' in query)):
            res = requests.get('https://ipinfo.io/')
            data = res.json()
            city = data['city']
            location = data['loc'].split(',')
            latitude = location[0]
            longitude = location[1]
            print("Latitude : ", latitude)
            speak(latitude+"Latitude")
            print("Longitude : ", longitude)
            speak(longitude+"Longitude")
            print("City : ", city)
            speak("you are currently at" + city)
            print("you are currently at" + city)

        elif 'your name' in query:
            speak('I am Kiara, your desktop assistant')
            print('I am Kiara, your desktop assistant')
        
        elif 'google assistant' in query:
            speak("He was my classmate, too intelligent guy. We both are best friends.")
            print("He was my classmate, too intelligent guy. We both are best friends.")

        elif 'siri' in query:
            speak("Siri, She's a competing virtual assistant on   a competitor's phone. \
                Not that I'm competitive or anything.")
            print("Siri, She's a competing virtual assistant on   a competitor's phone. \
                Not that I'm competitive or anything.")


        
        elif 'cortana' in query:
            print("I thought you'd never ask. So I've never thought about it.")
            speak("I thought you'd never ask. So I've never thought about it.")
        
        elif 'what is' in query:
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        
        elif 'volume up' in query:
            pi.press("volumeup")

        elif 'volume down' in query:
            pi.press("volumedown")

        elif 'mute volume' in query:
            pi.press("volumemute")
        
        elif 'how to' in query:
            try:
                max_results = 1
                data = search_wikihow(query, max_results)
                data[0].print()
                speak(data[0].summary)
            except Exception as e:
                print('Sorry, I am unable to find the answer for your query.')
                speak('Sorry, I am unable to find the answer for your query.')
        
        elif 'what language you use' in query:
            print("I am written in Python and I generally speak english.")
            speak("I am written in Python and I generally speak english.")
            
        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        
        elif 'translate' in query:
            speak('what do want to translate?')
            print('what do want to translate?')
            translation()    
            

    
