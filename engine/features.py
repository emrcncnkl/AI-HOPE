import os
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME

@eel.expose
def playasssistantSound():
    music_dir = "www/sounds/Start.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("aç", "")
    query.lower()

    if query != "":
        speak( query + "açılıyor..." )
        os.system(query + 'başlatılıyor...')
    else:
        speak("üzgünüm istediğini bulamadım...")
