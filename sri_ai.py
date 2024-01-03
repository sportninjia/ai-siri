# pip install SpeechRecognition 
# pip install PyAudio
# pip install pywhatkit
# pip install gtts
# pip install playsound
import speech_recognition as sr 
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    
    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")
    
def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:  
        audio = recorder.listen(source)

    speech_text = recorder.recognize_google(audio)
    print(speech_text)
      
    if "Hey Jarvis" in speech_text:
        speech("\tHow may I help you Adarsh")
        playsound("./sound/siri.mp3")
    else:
        return speech_text

name = "Henry"      
text = get_audio()

if "youtube" in text.lower():
    speech(f"Okay, I will search up {text} for you {name}.")
    pywhatkit.playonyt(text)
elif "joke" in text.lower():
    speech("Why don't scientists trust atoms? Because they make up everything!")
elif "search" in text.lower():
    speech(f"Okay, I will  {text} up for you {name}")
    pywhatkit.search(text)
else:
    speech("Sorry I can't do that command")