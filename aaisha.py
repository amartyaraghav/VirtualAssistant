import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install puautogui
import cv2 #pip install opencv
import psutil #pip install psutil
import pyjokes #pip install pyjokes

engine =pyttsx3.init()
voice_id = 'com.apple.speech.synthesis.voice.samantha'
engine.setProperty('voice', voice_id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    #speak("Current time is:")
    speak("The current time is")
    
    speak(Time)

def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    #speak("Today's date is: ")
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back sir!")
    #time()
    #date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour <18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Aaisha at your service. Please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio ,language ='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please.")
        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com',"password")
    server.sendmail('abc@gmai.com',to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("/Users/raghav/Desktop/Jarvis/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    battery = (psutil.sensors_battery()).percent
    speak("Battery is at")
    speak(battery)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send email")
        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = '/Applications/Google Chrome.app %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ '.com')
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play songs' in query:
            songs_dir = ""
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            rem = open('data.txt','w')
            rem.write(data)
            rem.close()
        elif 'do you know anything' in query:
            rem = open('data.txt', 'r')
            speak("you said me to remember that" +rem.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'recent capture' in query:
            ss = cv2.imread("ss.png")
            speak("Showing recently captured Screenshot")
            cv2.imshow("Screenshot",ss)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif 'device status' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'offline'  in query:
            speak("Tadaaa!! Have a nice day Sir!")
            quit()


def voiceDetails():
    voices = engine.getProperty('voices')   
    for voice in voices: 
        # to get the info. about various voices in our PC  
        print("Voice:") 
        print("ID: %s" %voice.id) 
        print("Name: %s" %voice.name) 
        print("Age: %s" %voice.age) 
        print("Gender: %s" %voice.gender) 
        print("Languages Known: %s" %voice.languages)

#takeCommand()
#wishme()
#speak("Hello! Aaisha at your service.")
#date()
#time()