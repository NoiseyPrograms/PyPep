import time
import os
print("Loading,please wait...")
time.sleep(5)
print("""Extras
        [1] Text To Speech""")
app = input("[?]")
if app == "1":
    print("Loading TTS Program...")
    time.sleep(4)
    os.startfile("tts.py")
    time.sleep(4)
    exit()