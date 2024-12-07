import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import eel
import threading
from playsound import playsound
import time
import requests
pygame.mixer.init()
def is_connected():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def play_sound(text, filename="output.mp3"):
    if is_connected():
        try:
            tts = gTTS(text=text, lang="tr")
            tts.save(filename)
            os.system(f"start {filename}")
        except Exception as e:
            print(f"Ses oynatma sırasında hata oluştu: {str(e)}")
    else:
        print("İnternet bağlantısı yok. Ses dosyası oluşturulamadı.")
        
# Kullanıcı metnini seslendiren fonksiyon
def speak(text):
    def play_sound():
        tts = gTTS(text=text, lang='tr')
        filename = 'turkish_speech.mp3'
        tts.save(filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        if os.path.exists(filename):
            os.remove(filename)
    
    threading.Thread(target=play_sound).start()

# Kullanıcıdan komut alacak fonksiyon
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # JavaScript'e "Dinliyorum..." mesajı gönder
        eel.DisplayMessage("Dinliyorum...")  

        print('Dinliyorum...')
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=0.3)  # Ortam gürültüsünü ayarlama

        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            # Zaman aşımı durumunu JavaScript'e bildirin
            eel.DisplayMessage("Mikrofon zaman aşımına uğradı.")
            print("Mikrofon zaman aşımına uğradı.")
            return ''

    try:
        # Konuşma algılanıyor ve işleniyor
        eel.DisplayMessage("Konuşma algılanıyor...")
        print('hmm...')
        query = r.recognize_google(audio, language='tr-TR,en-US')
        print(f'Kullanıcı Dedi ki: {query}')
        eel.DisplayMessage(f"Kullanıcı Dedi ki: {query}")
        time.sleep(2)

    except Exception as e:
        # Hata durumunu JavaScript'e bildirin
        eel.DisplayMessage("Anlaşılamadı, lütfen tekrar deneyin.")
        print("Anlaşılamadı, lütfen tekrar deneyin.")
        return ''
    
    return query.lower()

def activate_listening():
    eel.DisplayMessage("useReadyMessages")  # JavaScript'teki özel durumu teti

@eel.expose
def allCommands(message=1):
    try:
        # allCommands fonksiyonunun çağrıldığını kontrol etmek için terminal çıktısı
        print("allCommands fonksiyonu çağrıldı")

        # Gelen mesajın kaynağını kontrol ediyoruz: sesli veya chat
        if message == 1:
            query = takecommand()  # Kullanıcıdan sesli komut al
            print(f"Sesli komut alındı: {query}")
        else:
            query = message  # Chat kısmından gelen mesajı al
            print(f"Chat komutu alındı: {query}")

        # Eğer komut boşsa işlem yapmamak için kontrol
        if not query:
            print("Komut alınamadı.")
            eel.DisplayMessage("Lütfen bir şey söyleyin.")
            return

        # Gelen komutu terminalde yazdırıyoruz
        print(f"Gelen komut: {query}")

        # Komutları kontrol ediyoruz ve uygun işlemi çağırıyoruz
        if "aç" in query:
            from engine.features import openCommand
            print("openCommand fonksiyonu çağrılıyor...")
            openCommand(query)
            print("openCommand başarıyla çalıştırıldı.")
        elif "youtube'da" in query.lower():
            print("YouTube komutu algılandı.")
            from engine.features import PlayYoutube
            PlayYoutube(query)
            print("YouTube komutu başarıyla işlendi.")
        else:
            # Komut tanınmadığında kullanıcıya bildirim gönder
            eel.DisplayMessage("Bu komutu anlayamadım. Lütfen tekrar deneyin.")

    except Exception as e:
        import traceback
        error_message = traceback.format_exc()
        # Hata ayrıntısını terminale yazdırıyoruz
        print(f"Hata ayrıntısı: {error_message}")
        eel.DisplayMessage("Bir hata oluştu, lütfen tekrar deneyin.")




    eel.ShowHood()
 