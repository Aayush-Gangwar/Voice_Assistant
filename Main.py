# importing neccessary python libraries used for system.
from win32com.client import Dispatch
import pyttsx3
import datetime
from bs4 import BeautifulSoup
import speech_recognition as sr
import pyaudio
import numpy as np
import wikipedia
import requests
import webbrowser
import sports
import os
import pywhatkit
import smtplib
import cv2
import wolframalpha
import sys
import winsound
import pyautogui
from email.mime.text import MIMEText
from pycricbuzz import Cricbuzz
import speedtest
import random

# setting up the voices and engine to accept commands for system from user.
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",130)

def speak(text):   # speak function/module of system..help in converting text to voice.
    engine.say(text)
    engine.runAndWait()

def acceptcommands():   # module for accepting voice input from user and recognizes with google_recognize. and converting into text string.
    c = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening---")
        c.pause_threshold=0.5
        c.energy_threshold= 100
        audio=c.listen(source)

    try:
        print("recognizing")
        query=c.recognize_google(audio,language="en-in")
        speak(query)
        print(f"user said: {query}")
    except Exception as error:
        # speak("can't recognize..please speak again...")
        return "NONE"
    return query

contacts={"xyz":["+9191xxxxxxxx","user_mail@gmail.com"]}   #sample contact list for sending message,emails.

def accept_wake_commands(wake):   # capture the wake up command from user.
    c = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am at sleep mode sir")
        c.pause_threshold=0.5
        c.energy_threshold= 100
        audio=c.listen(source)

    try:
        print("sleeping")
        query=c.recognize_google(audio,language="en-in")
        speak(query)
        print(f"user said: {query}")
    except Exception as error:
        pass
        return "NONE"
    return query

access=False
def face_lock():    # security module ...unlock the system by recognizes the correct user face id only.
    count=2
    base = cv2.imread("opencv_frame_base.png")   # original user face id...(unlock system by comparing new faces from this base image).
    try:
        hsv_base = cv2.cvtColor(base, cv2.COLOR_BGR2HSV)
    except:
        count=1
        speak("Welcome sir")
        speak("I am your voice assistant")
        speak("give me your face id for security")
    if(count==2):
        speak("Show your face for access")
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")
        img_counter = 0
        while True:
            ret, frame = cam.read()
            if not ret:
                speak("failed to grab frame")
                break
            cv2.imshow("test", frame)
        
            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                speak("Escape hit for closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)        # accept present user face id..
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
    else:
        c=0
        while(c<2):
            cam = cv2.VideoCapture(0)
            cv2.namedWindow("test")
            img_counter = 0
            while True:
                ret, frame = cam.read()
                if not ret:
                    speak("failed to grab frame")
                    break
                cv2.imshow("test", frame)
            
                k = cv2.waitKey(1)
                if k%256 ==27:
                    # ESC pressed
                    speak("Escape hit for closing...")
                    break
                elif k%256 == 32:
                    # SPACE pressed
                    if(c==0):
                        img_name = "opencv_frame_base.png".format(img_counter)          # accept base face id..in case it's not present in directory.
                        cv2.imwrite(img_name, frame)
                        c+=1
                    else:
                        img_name = "opencv_frame_{}.png".format(img_counter)           # accept present user face id..
                        cv2.imwrite(img_name, frame)
                        img_counter += 1
                        c+=1
   # cam.release()
    cv2.destroyAllWindows()
    # function for comapring new face id and base user face id.
    base = cv2.imread("opencv_frame_base.png")
    test = cv2.imread("opencv_frame_0.png")
    hsv_base = cv2.cvtColor(base, cv2.COLOR_BGR2HSV)
    hsv_test = cv2.cvtColor(test, cv2.COLOR_BGR2HSV)

    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
    cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    compare_method = cv2.HISTCMP_CORREL

    base_test = cv2.compareHist(hist_base, hist_test, compare_method)
    if(base_test>=0.8):  # unlock only when >=80% of images are same.
        access= True
        speak("Access granted")
        wish()
        Task_execution()  # task execution will start from this function.
    else:
        speak("Access denied")
    cv2.waitKey(0)

def temp(query):    # temperature module..tells the temperature of place present in query(user voice input).
    url= f"https://www.google.com/search?q={query}"
    try:
        r=requests.get(url)
        data=BeautifulSoup(r.text,"html.parser")
        temp=data.find("div",class_="BNeawe").text
        speak(temp)
    except:
        speak("There is some error..please speak again")

def wolfram(query):    # for maths and science
    api_id ="TT4H6R-U4KUUXQUXK"
    requester=wolframalpha.Client(api_id)
    requested=requester.query(query)
    try:
        ans=next(requested.results).text
        return ans
    except:
        Speak("Sorry, sir not got any answer")

def calculation(query):  # for maths calculations.
    query=str(query)
    query=query.replace("jarvis","")
    query=query.replace("plus","+")
    query=query.replace("multiply","*")
    query=query.replace("into","+")
    query=query.replace("minus","-")
    query=query.replace("divide","/")

    query=str(query)
    try:
        result=wolfram(query)
        speak(f"answer is {result}")
    except:
        speak("Sorry sir, did not got the answer")

def My_location():   # to got user location.
    ip_ad=requests.get('https://api.ipify.org').text
    url= 'https://get.geojs.io/v1/ip/geo/'+ip_ad+".json"    # revel user location.
    r=requests.get(url)
    r=r.json()
    city=r['city']
    country=r["country"]
    speak(f"Sir,you are in {city,country}")

def wish():        # gretting module...wish user according to time.
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and  hour<=12):
        speak("Good morning Sir")
    elif(hour >=12 and   hour<=16):
        speak("Good afternoon Sir")

    elif(hour>=16 and  hour<=19):
        speak("Good evening Sir")
    else:
        speak("Good night Sir")
    speak("Myself jarvis!,Your personal voice assistant. How may i help you.")

def date():      # date function...show current date.
    today=datetime.datetime.now()
    format = '%I:%M %p'
    date = today.strftime(format)
    speak(date)

def whatsapp_message():     # communication module...help in sending whatsapp message to person mention in query.
    speak("Tell me the name of Person!.")
    name=acceptcommands().lower()

    if(name in contacts):
        speak("Tell me the message...")
        message=acceptcommands()
        phone_no=contacts[name][0]
        try:
            pywhatkit.sendwhatmsg_instantly(phone_no, message)
            speak("message sent")
        except:
            speak("error in sending message..please try again")
    
    else:
        speak("Tell me the phone number")
        phone_no=(acceptcommands())
        phone_no="+91"+phone_no
        speak("Tell me the message...")
        message=acceptcommands()
        try:
            pywhatkit.sendwhatmsg_instantly(phone_no, message)
            speak("message sent")
        except:
            speak("error in sending message")

def send_mail():          # communication module...help in sending mail to person mention in query.
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    jarvis_mail_id="jarvisai889@gmail.com"
    jarvis_id_password="JarvisAi@2003"
    server.login(jarvis_mail_id,jarvis_id_password)

    speak("Tell me the name of Person!.")
    name=acceptcommands().lower()

    if(name in contacts):
        speak("Tell me the subject...")
        subject=acceptcommands()
        speak("Tell me the message...")
        message=acceptcommands()
        email_receiver=contacts[name][1]
        try:
            server.sendmail(jarvis_mail_id,[email_receiver],message)
            speak("Mail sent to"+name)
        except:
            speak("Error in sending mail..try again")
        server.close()
            
    else:
        speak("Tell me the message...")
        message=acceptcommands()
        speak("Tell me the recievers gmail id")
        email_receiver=acceptcommands()+"@gmail.com"
        try:
            server.sendmail(jarvis_mail_id,[email_receiver],message)
            speak("Mail sent")
        except:
            speak("Error in sending mail..try again")
    server.close()

def speedtest():     #to get the user internet speed.
    speak("Checking internet speed")
    speed=speedtest.Speedtest()
    upload=speed.upload()
    download=speed.download()
    upload=int(int(upload)/8000)
    download=int(int(download)/8000)
    speak(f"Sir,your downloading speed is{download} and uploading speed is{upload}")

def screen_shot():   # for clicking sceenshots
    ss=pyautogui.screenshot()
    ss.save("D:\\ss.png")
    speak("Screenshot is taken sir")

def wikipedia_search(query):    # web search module..help in scrapping or browse anything on wikipedia.
    speak("searching wikipedia")
    query=query.replace("wikipedia","")
    try:
        result= wikipedia.summary(query,sentences=2)
        speak(result)
    except:
        speak("There is some error..please speak again sir.")

def google_search(query):         # web search module..help in search anything on google.
    speak("searching wikipedia")
    query=query.replace("wikipedia","")
    try:
        result= wikipedia.summary(query,sentences=2)
        speak(result)
    except:
        speak("There is some error..please speak again sir.")
    query=query.replace("jarvis","")
    query=query.replace("google search","")
    try:
        pywhatkit.search(query)
        speak("Done Sir")
    except:
        speak("there is some error..please speak again..")

def open_site(query):            # function help in opening any site.
    speak("okay sir..launching")
    query=query.replace("jarvis","")
    query=query.replace("website","")
    site=query.replace("open","").lower()
    site=site.replace(" ","")
    try:
        open_site="https://www."+site+".com/"
        webbrowser.open(open_site)
        speak("Launched sir")
    except:
        speak("There is some error..please speak again sir.")

def chat_bot_module():           # chat bot function...user can chat according to inputs.
    command1=["hello","wake up","hey","suno na","hi","utho","you there"]
    reply1=["Hello sir,Welcome Back!","Always for you sir","How can i Help you"]
    command2=["bye","go and sleep"]
    reply2=["bye sir","nice meeting you"]
    speak("okay sir..chat bot activated start chatting")
    text=acceptcommands().lower()
    try:
        def chatterbot(text):
            for word in text.split():
                if word in command1:
                    speak(random.choice(reply1))
                elif word in command2:
                    speak(random.choice(reply2))
                else:
                    speak("hmm sir.")
    except:
        speak("Sir..please chat again")
