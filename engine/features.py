import re
from playsound import playsound
import eel
import os
import pywhatkit as pwk

import pyautogui

import subprocess
import time
from urllib.parse import quote

from db import *
from helper import *
from command import *

from hugchat import hugchat

import csv
import sqlite3
from unittest import result

con = sqlite3.connect("lyra.db")

cursor = con.cursor()


from config import ASSISTANT_NAME



@eel.expose
def playAssistantsound():
    music_dir = "www\\assets\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query=query.replace(ASSISTANT_NAME ,"")
    query=query.replace("open","")
    query=query.lower()

    if query!="":
        speak("Opening"+query)
        os.system('start'+query)

    else:
        speak("not found")


def PlayYouTube(query):
    search_item = extract_yt_term(query)
    speak("Playing"+ str(search_item) +"on YouTube")
    pwk.playonyt(search_item)

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match =  re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None


def findcontact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'tu', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove).strip()

    print(f"Searching for contact: '{query}'") 

    cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
    results = cursor.fetchall()

    print(f"Database Results: {results}") 

    if results:
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith("+91"):
            mobile_number_str = "+91" + mobile_number_str
        print(f"Found contact: {query} -> {mobile_number_str}")
        return mobile_number_str, query
    else:
        print("Contact not found!") 
        speak('Not in contacts')
        return None, None


    
def whatsapp(mobile_no, message, flag, name):
    if flag == 'message':
        jarvis_message = f"Message sent successfully to {name}"
        
        try:
           
            pwk.sendwhatmsg_instantly(mobile_no, message, wait_time=10)
            time.sleep(5)

        except Exception as e:
            print(f"Error sending WhatsApp message: {e}")
            speak("There was an error sending the message.")

    elif flag == 'call':
        jarvis_message = f"Calling {name}"
        speak("WhatsApp does not support direct call automation.")

    else:
        jarvis_message = f"Starting video call with {name}"
        speak("WhatsApp does not support direct video call automation.")

    speak(jarvis_message)
    return jarvis_message 

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response