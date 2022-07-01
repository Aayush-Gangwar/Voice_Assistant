# Voice_Assistant
#### This was my attempt to make a voice assistant similar to JARVIS with face lock security.
#### It can do a lot of cool things and automate your daily tasks you do on your personal computers/laptops.

## Built with

<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>

## GUI

![gui fid](https://user-images.githubusercontent.com/101112022/176831217-41097835-7876-47e7-a8f2-b76783b025ac.gif)

## Features

#### For a cool demo of this project watch this [Video]()

It can do a lot of cool things, some of them being:

- Have face lock security
- Greet user
- sleep and wake mode
- Tell current time and date
- Launch applications/softwares 
- Open any website
- Tells about temperature/weather of any city
- Send email (with subject and content)
- Send message via whatsapp web (to person who are in contact list or ask for new numbers)
- Tells exact location of yours.
- Tells about any person (via Wikipedia)
- Can search anything on Google 
- Can play any song on YouTube
- Tells top headlines (via Times of India)
- Plays music
- Calculate mathematical problems (example: Jarvis, calculate 100-90,200/2,100*10 and so on)
- Answer any generic question (via Wolframalpha)
- Take important note in notepad
- Can tell your internet speed
- Tells a random joke
- Chat bot (can chat with user)
- Can switch the window
- Can take screenshot and save it with custom filename
- Has a cool Graphical User Interface
- GUI have button to directly open some apps

## Installation

- Clone the repo.
- Have to edit some things in main.py file-
    ```
    email = "<your_email>"
    email_password = "<your_email_password>"
    wolframalpha_id = "<your_wolframalpha_id>"
- Install all the requirements by just hitting ``` pip install -r requirements.txt ```
- Install PyAudio from wheel file by following instructions given [here](https://stackoverflow.com/a/55630212)
- Run the program by ``` python jarvis_gui.py ```
- Enjoy the voice assistant.

## Deployment

- Download the build folder and run the .exe file.

## API Keys
To run this program you will require a wolframaalpha API keys. Register your API key by clicking the following link

- [Wolframalpha](https://www.wolframalpha.com/)

## Code Structure


    │── utils               # GUI images/ gifs
    ├── jarvis.ui           # GUI file (in .ui format)
    ├── jarvisui.py         # GUI file (in .py format)
    ├── main.py             # main driver program of Jarvis
    ├── jarvis_gui.py       # main exe file(linked GUI with main.py file)
    ├── setup.py            #code to hide cmd window while executing the program
    ├── requirements.txt    # all dependencies of the program

- The code structure if pretty simple. The code is completely modularized and is highly customizable.

## Future Improvements
- Generalized conversations can be made possible by incorporating Natural Language Processing
- Addying more languages with english
- GUI can be made more nicer to look at and functional
- More functionalities can be added.
