import os, time, playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text= text,lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speaking_text = """Welcome to part 2 of creating a voice assistant with python. In this tutorial we will get microphone input from the user using the module pyaudio and speech_recognition."""
speak(speaking_text)

def get_audio():
    r = sr.Recognizer()
    #mp3file = sr.AudioFile("voice.mp3")
    #with mp3file as source:
    with sr.Microphone() as source:
        #audio = r.record(source)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

speak("Hello")
#get_audio()

