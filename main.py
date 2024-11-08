import os
import eel
import threading
import random
from playsound import playsound
from engine.features import playasssistantSound  # Bu fonksiyonun doğru çalıştığını varsayıyorum
from engine.command import *
# `playasssistantSound` fonksiyonunu bir iş parçacığında çalıştırmak için yeni bir fonksiyon
def play_sound_thread():
    playasssistantSound()


# Mikrofon sesini çalacak fonksiyon
@eel.expose
def play_mic_sound():
    playsound(r"C:\Users\C V E X\Desktop\AI ASSISTANT\www\sounds\mikrofon.mp3")

# Rastgele asistan mesajları döndüren fonksiyon
@eel.expose
def get_random_prompt():
    prompts = [
        "Ben Hope, size nasıl yardımcı olabilirim?",
        "Birlikte beyin fırtınası yapalım mı?",
        "Spotify'ı açmamı ister misiniz?",
        "Takvimi kontrol etmek ister misiniz?",
        "Hava durumuna bakmamı ister misiniz?",
        "Hatırlatıcı eklemek ister misiniz?",
        "Görev listesi oluşturalım mı?",
        "E-posta uygulamanızı açmamı ister misiniz?",
        "Yeni bir not oluşturmamı ister misiniz?",
        "Navigasyonu açmamı ister misiniz?",
        "Bir konuda yardım ister misiniz?"
    ]
    return random.choice(prompts)

# Eel ile web içeriğini başlatma
eel.init("www")

# Ses dosyasını arka planda çal
threading.Thread(target=play_sound_thread).start()

# HTML dosyasını aç (bu durumda varsayılan tarayıcıda açar)
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# Eel uygulamasını başlat
eel.start('index.html', mode=None, host='localhost', block=True)
