import os
import re
from gtts import gTTS

def generate_voice(script):
    script = re.sub(r'\(.*?\)', '', script)
    script = re.sub(r'\[.*?\]', '', script)
    script = script.strip()
    tts = gTTS(text=script, lang="en")
    tts.save("voiceover.mp3")
    print("Voiceover saved!")

