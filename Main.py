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