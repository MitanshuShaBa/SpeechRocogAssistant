import speech_recognition as sr
from gtts import gTTS
import os
import playsound


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove('voice.mp3')


def answer(text):
    if text == 'what is my name':
        speak('Your name is Mitanshu')
    else:
        speak('you said ' + text)


# listening to audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said:\n>>>" + text)
    speak(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
