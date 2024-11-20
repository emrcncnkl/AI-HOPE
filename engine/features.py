import os
from playsound import playsound
import eel
import re
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
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Youtube'da "+search_term+" oynatılıyor")
    kit.playonyt(search_term)

def extract_yt_term(command):
     # Şarkı adını yakalamak için bir düzenli ifade deseni tanımla
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    
    # re.search kullanarak komut içinde eşleşme ara
    match = re.search(pattern, command, re.IGNORECASE)
    
    # Eğer bir eşleşme bulunursa, yakalanan şarkı adını döndür; aksi takdirde None döndür
    return match.group(1) if match else None 
