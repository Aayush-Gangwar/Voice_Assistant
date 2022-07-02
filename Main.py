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