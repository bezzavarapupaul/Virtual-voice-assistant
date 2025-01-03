from gtts import gTTS
import speech_recognition as sr
import playsound
import uuid
import os
from time import ctime
import webbrowser
import random
import re

# Function to recognize speech
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me, I'm listening...")
        audio = r.listen(source, phrase_time_limit=5)
    data = ""
    try:
        data = r.recognize_google(audio, language='en-US')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("I didn't understand. Please speak clearly.")
    except sr.RequestError as e:
        print("Unable to process your request. Try again later.")
    return data

# Function to respond with speech
def respond(text):
    print(text)
    tts = gTTS(text=text, lang='en', tld='co.in')
    filename = "Speech_%s.mp3" % str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Virtual assistant logic
def virtual_assnt(data):
    listening = True

    # Utility Commands
    if "how are you" in data:
        respond("I'm good, thank you. How about you?")
    elif "what is the time" in data:
        respond(ctime())
    elif "who are you" in data:
        respond("I'm your AI assistant, coded by Paul.")
    elif "shutdown" in data:
        listening = False
        respond("Goodbye! Have a great day.")
    
    # Browsing and Social Media
    elif "open LinkedIn" in data.casefold():
        webbrowser.open("https://www.linkedin.com")
        respond("Opening LinkedIn.")
    elif "open GitHub" in data.casefold():
        webbrowser.open("https://www.github.com")
        respond("Opening GitHub.")
    elif "open Gmail" in data.casefold():
        webbrowser.open("https://mail.google.com")
        respond("Opening Gmail.")
    elif "search for a job" in data.casefold():
        webbrowser.open("https://www.naukri.com")
        respond("Opening job search website.")
    elif "open Google" in data.casefold():
        webbrowser.open("https://www.google.com")
        respond("Opening Google.")
    elif "open YouTube" in data.casefold():
        webbrowser.open("https://www.youtube.com")
        respond("Opening YouTube.")
    elif "search" in data.casefold():
        query = data.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        respond(f"Searching for {query}.")
    elif "locate" in data.casefold():
        location = data.replace("locate", "").strip()
        webbrowser.open(f"https://www.google.com/maps/search/{location}")
        respond(f"Locating {location} on Google Maps.")
    
    # Fun facts
    elif "tell me a joke" in data:
        jokes = [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "Why don’t skeletons fight each other? They don’t have the guts."
        ]
        respond(random.choice(jokes))
    elif "tell me a fact" in data:
        facts = [
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible.",
            "Octopuses have three hearts.",
            "Bananas are berries, but strawberries are not."
        ]
        respond(random.choice(facts))
    
    # System tasks
    elif "play music" in data:
        webbrowser.open("https://www.spotify.com")
        respond("Opening Spotify for you.")
    elif "open calculator" in data:
        os.system("calc")
        respond("Opening calculator.")
    elif "check weather" in data.casefold():
        respond("Please provide your city.")
        city = listen()
        url = f"https://www.google.com/search?q=weather+in+{city}"
        webbrowser.open(url)
        respond(f"Checking weather in {city}.")
    
    # Knowledge base
    elif "what is" in data or "who is" in data or "define" in data:
        query = data.replace("what is", "").replace("who is", "").replace("define", "").strip()
        url = f"https://en.wikipedia.org/wiki/{query}"
        webbrowser.open(url)
        respond(f"Here is what I found about {query} on Wikipedia.")
    
    # Fun activities
    elif "roll a dice" in data:
        dice = random.randint(1, 6)
        respond(f"You rolled a {dice}.")
    elif "flip a coin" in data:
        coin = random.choice(["Heads", "Tails"])
        respond(f"It's {coin}.")
    
    # Extended commands (examples to show the range of functionality)
    elif "what can you do" in data:
        respond("I can perform tasks like web browsing, telling jokes, checking the time, playing music, and more. Ask me anything!")
    elif "translate" in data:
        respond("What do you want me to translate?")
        text = listen()
        respond(f"Translating '{text}' is currently not implemented. Sorry about that!")
    # Coding Assistance
    elif "start coding session" in data:
        respond("What programming language should I assist you with?")
        language = listen()
        if "Python" in language:
            respond("Opening Python tutorials on W3Schools.")
            webbrowser.open("https://www.w3schools.com/python/")
        elif "JavaScript" in language:
            respond("Opening JavaScript tutorials on W3Schools.")
            webbrowser.open("https://www.w3schools.com/js/")
        else:
            respond(f"I couldn't find resources for {language}.")
    
    # Entertainment and Relaxation
    elif "play a song" in data:
        webbrowser.open("https://open.spotify.com")
        respond("Opening Spotify for your music.")
    elif "recommend a movie" in data:
        movies = [
            "Inception", "The Matrix", "The Shawshank Redemption", 
            "Interstellar", "Parasite", "Forrest Gump"
        ]
        respond(f"I recommend you watch {random.choice(movies)}.")
    elif "suggest a book" in data:
        books = [
            "The Alchemist by Paulo Coelho", "Sapiens by Yuval Noah Harari",
            "Atomic Habits by James Clear", "1984 by George Orwell"
        ]
        respond(f"How about reading '{random.choice(books)}'?")
    
    # Learning and Productivity
    elif "learn something new" in data:
        webbrowser.open("https://www.coursera.org")
        respond("Opening Coursera for learning new skills.")
    elif "open coding platform" in data:
        webbrowser.open("https://www.hackerrank.com")
        respond("Opening HackerRank.")
    elif "set a reminder" in data:
        respond("What should I remind you about?")
        reminder = listen()
        respond(f"Reminder set for: {reminder}.")
    
    # Health and Fitness
    elif "suggest a workout" in data:
        workouts = ["Push-ups", "Squats", "Plank", "Yoga stretches"]
        respond(f"Try doing some {random.choice(workouts)} for 10 minutes.")
    elif "track my steps" in data:
        respond("Please use your fitness tracker app for step count.")

    # Default Case
    else:
        respond("I'm sorry, I didn't understand that command. Can you repeat?")
    
    return listening

# Main loop
respond("Hello! How can I assist you today?")
listening = True
while listening:
    user_input = listen()
    listening = virtual_assnt(user_input)
