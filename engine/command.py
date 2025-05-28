import pyttsx3
import speech_recognition as sr
import eel
import time
import sqlite3


con = sqlite3.connect("lyra.db", check_same_thread=False) 
cursor = con.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
con.commit()



def save_message(sender, message):
    cursor.execute("INSERT INTO chat_history (sender, message) VALUES (?, ?)", (sender, message))
    con.commit()



def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    eel.receiverText(text)
    save_message("lyra", text)
    engine.say(text)
    engine.runAndWait()



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage('listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(1)
        return query.lower()

    except Exception as e:
        return ""



@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        if query:
            print(query)
            eel.senderText(query)
            save_message("user", query)
        else:
            eel.senderText("...")
            save_message("user", "...")
    else:
        query = message
        print(f"Text input: {query}")
        eel.senderText(query)
        save_message("user", query)

    if not query:
        speak("I didn't catch that, please try again.")
        return

    print(f"User said: {query}")

    if "open" in query:
        from features import openCommand
        openCommand(query)
        response = f"Opening {query.split('open')[-1].strip()}"
        eel.receiverText(response)
        save_message("lyra", response)
        speak(response)

    elif "on youtube" in query:
        from features import PlayYouTube
        PlayYouTube(query)
        response = "Searching on YouTube."
        eel.receiverText(response)
        save_message("lyra", response)
        speak(response)

    elif "send message" in query or "phone call" in query or "video call" in query:
        from features import findcontact, whatsapp
        flag = ""
        contact_no, name = findcontact(query)

        if contact_no is None or name is None:
            speak("I couldn't find that contact.")
            return

        print(f"Contact Found: {name} -> {contact_no}")

        if "send message" in query:
            flag = 'message'
            speak("What message would you like to send?")
            message = takecommand()
            eel.senderText(message)
            save_message("user", message)
            if not message:
                speak("Message cannot be empty.")
                return

        elif "phone call" in query:
            flag = 'call'
            message = ""

        else:
            flag = 'video call'
            message = ""

        print(f"Sending {flag} to {contact_no}")
        whatsapp(contact_no, message, flag, name)
        speak(f"{flag.capitalize()} to {name} initiated.")

    else:
         from features import chatBot
         chatBot(query)
      

    eel.ShowHood()


@eel.expose
def get_chat_history():
    cursor.execute("SELECT sender, message FROM chat_history ORDER BY timestamp ASC")
    return cursor.fetchall()

@eel.expose
def clear_chat_history():
    cursor.execute("DELETE FROM chat_history")
    con.commit()
    print("Chat history cleared from the database.")