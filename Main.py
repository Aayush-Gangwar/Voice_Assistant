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