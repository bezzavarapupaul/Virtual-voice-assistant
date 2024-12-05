
from gtts import gTTS
import speech_recognition as sr
import playsound
import uuid
import os
from time import ctime
import webbrowser
import re

#define a function to recognize ur voice
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("tell bro im listening...")#my program run indication
        audio=r.listen(source,phrase_time_limit=3)
    data=""
    #exception handling
    try:
        data=r.recognize_google(audio,language='en-US')#language setting
        print("you told:"+data)#prints the statement we gave
    except sr.UnknownValueError:#if system didnt recognize
        print("konchem gattiga matladu bro")
    except sr.RequestError as e:
        print("matladadam radhu bro niku")#any unknown error if found
    return data
    tts = gTTS(text=data,lang='en',tld='co.in')
    tts.save('speech.mp3')
    playsound.playsound('speech.mp3')
listen()
def respond(String):
    print(String)
    tts= gTTS(text=String,lang='en',tld='co.in')
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
#we will start giving actions
def virtual_assnt(data):
        if 'how are you' in data:
            listening=True
            respond("hello im good")
        elif 'what is the time' in data:
            listening=True
            respond(ctime())
        elif 'who are you' in data:
            listening=True
            respond('im a ai assistant coded by paul')
        elif 'shutdown' in data:
            listening=False
            respond('ok done bye bye....')
        elif 'can you open google' in data:
            listening=True
            respond('no im not upto that instinct')
        elif 'open google' in data.casefold():
            listening=True
            reg_ex=re.search('open google(.*)',data)
            url="https://www.google.com/"
            if reg_ex:
                sub=reg.ex.group(1)
                url=url+'r/'
            webbrowser.open(url)
            respond('success')
        elif 'open youtube'in data.casefold():
            listening=True
            reg_ex=re.search('open youtube(.*)',data)
            url="https://www.youtube.com/watch?v=jUuFsVKutXE&list=RDO3I6GNX4rfs&index=2"
            if reg_ex:
                sub=reg.ex.group(1)
                url=url+'r/'
            webbrowser.open(url)
            respond('success')
        elif 'locate' in data.casefold():
            listening=True
            webbrowser.open('https://www.google.com/maps/search/'+data.replace("locate",""))
            result="Located"
            respond("Located{}".format(data.replace('locate','')))
        try:
            return listening
        except UnboundLocalError:
            print("timeout")
            
            
respond("chepara babu ")
listening=True
while listening==True:
    data=listen()
    listening=virtual_assnt(data)


