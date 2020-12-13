import speech_recognition 			
import pyttsx3
import win32.win32api
import sys
import datetime
import requests,json
import platform
import os
import wikipedia
import webbrowser 
import subprocess

listener = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def first():
    engine.say("i am jarvis, your personal assistant ")
    engine.say("initialising system ")
    engine.runAndWait()




def talk(text):

    engine.say(text)
    engine.runAndWait()

def wish():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        talk('good morning sir')

    elif hour>12 and hour<18:
        talk('good afternoon sir')

    else:
        talk('good evening sir')
    get_command()

def details():

    my_system = platform.uname()
    talk(f"System: {my_system.system}")
    talk(f"Node Name: {my_system.node}")
    talk(f"Release: {my_system.release}")
    talk(f"Version: {my_system.version}")
    talk(f"Machine: {my_system.machine}")
    talk(f"Processor: {my_system.processor}")

def open_app(command):

    if 'open notepad' in command:
        talk('opening notepad')
        npath = 'C:\\Windows\\system32\\notepad.exe'     # Your notepad location type here \\ is important
        os.startfile(npath)

    if 'open adobe' in command:
        talk('opening adobe reader')
        apath = 'C:\\Program Files (x86)\\Adobe\Reader 9.0\\Reader\\AcroRd32.exe'	# Your adobe reader location type here \\ is important
        os.startfile(apath)

    if 'open command' in command:
        talk('opening command prompt')
        cpath = 'C:\\Windows\\system32\\cmd.exe'	# Your cmd location type here \\ is important
        os.startfile(cpath)

    if 'open youtube' in command:
        talk('opening youtube')
        webbrowser.open('https://www.youtube.com/')
    
    if 'open facebook' in command:
        talk('opening facebook')
        webbrowser.open('https://m.facebook.com/')

    if 'open instagram' in command:
        talk('opening instagram')
        webbrowser.open('https://www.instagram.com/')
    
    if 'open google drive' in command:
        talk('opening google drive')
        webbrowser.open('https://drive.google.com/drive/my-drive')

    if 'open google' in command:
        talk('opening google..')
        talk('sir, what should i search on google')
        with speech_recognition.Microphone() as source:
                listener.adjust_for_ambient_noise(source, duration=0.2)
                voice = listener.listen(source)
                cmd = listener.recognize_google(voice)
                cmd = cmd.lower() 
                webbrowser.open(f'{cmd}')
    
   


def search(command):

    if 'wikipedia' in command:
        talk('searching wikipedia..')
        command = command.replace('wikipedia','')
        results = wikipedia.summary(command,sentences=2)
        talk('according to wikipedia')
        talk(results)
        print(results)

   


def selection(command):

    command = command.lower()

    if 'weather' in command:
        talk('getting weather data')
        webbrowser.open('weather in kerala')

    if 'play music' in command:
        talk('playing music')
        music_dir = 'D:\\ABHISHEK.P\\music test'		# Your music location type here \\ is important
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    
    if 'sleep' in command:
        talk("thank you for using me, have a good day")
        exit()

    if 'system details' in command:
        details()

    if 'jarvis' in command:
        talk('please tell me what can i do for you ')  

    if 'name' in command:
        talk('my name is jarvis , your personal assistant')

    if 'sing ' in command:
        talk('sorry sir ,i dont know how to sing ')

    if 'date today' in command:
        x = datetime.datetime.now().date()
        talk(x)

    if 'previous date' in command:
        x = datetime.date.today()- datetime.timedelta(days=1)
        talk(x)

    if 'date tomorrow' in command:
        x = datetime.date.today() + datetime.timedelta(days=1)
        talk(x)

    if 'how are you' in command:
        talk('i am fine sir, Thank you  , Hope you are fine')
    
    if 'hai'  in command:
        talk('hai sir')
    
    


def get_command():

    #talk(' please tell me what can i do for you')
    while True:
        try:
            print('listening...')
            with speech_recognition.Microphone() as source:
                listener.adjust_for_ambient_noise(source, duration=0.2)
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                print(command)
                if 'jarvis' in command:
                    first()
                if 'open' in command:
                    open_app(command)
                if 'search' in command:
                    search(command)
                selection(command)
                
        except:
            pass
def exit():
    os._exit(os.EX_OK)

wish()
