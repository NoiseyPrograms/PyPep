from gtts import gTTS
import time
import os   

print("Loading...")
time.sleep(4)
print("Welcome to Text To Speech Application. Please write your input")

x = input("[?]")

audio = gTTS(text=x, lang='en-US')

audio.save("tts.mp3")
os.system("start tts.mp3")