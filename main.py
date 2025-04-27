import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pythoncom
import pywintypes

print("Initializing Jarvis")
MASTER = "khaja"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("good afternoon" + MASTER)

    else:
        speak("good Evening" + MASTER)

    speak("I am Jarvis. How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kb.aisha786@gmail.ocm', 'password')
    server.sendmail("harry@gmail.com", to, content)
    server.close()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query

def main():

    speak("Initializing Jarvis")
    wishMe()
    query = takeCommand()

    #Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)

    elif 'open youtube' in query.lower():
            #webbrowser.open('youtube.com')
            url = "youtube.com"
            chrome_path = 'c:/program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
            #webbrowser.open('youtube.com')
            url = "google.com"
            chrome_path = 'c:/program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'open spotify' in query.lower():
            #webbrowser.open('youtube.com')
            url = "https://open.spotify.com/"
            chrome_path = 'c:/program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")

    elif 'email to harry' in query.lower():
            try:
                speak("what should i send")
                content = takeCommand()
                to = "19311a12g2@sreenidhi.edu.in"
                sendEmail(to, content)
                speak("Email has been sent to raj")
            except Exception as e:
                print(e)
main()

