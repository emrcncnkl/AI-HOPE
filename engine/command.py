import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import eel
import time
import requests
import webbrowser
import pywhatkit as kit

pygame.mixer.init()

# Internet kontrolü yapan fonksiyon
def is_connected():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Seslendirme fonksiyonu
def speak(text):
    try:
        if is_connected():
            print("Internet bağlantısı var, gTTS kullanılarak ses dosyası oluşturulacak.")
            tts = gTTS(text=text, lang='tr')
            filename = f"output_{time.time_ns()}.mp3"
            tts.save(filename)
            print(f"{filename} dosyası oluşturuldu, ses çalınıyor...")
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            if os.path.exists(filename):
                os.remove(filename)

            print("Ses başarıyla oynatıldı.")
        else:
            print("İnternet bağlantısı yok, ses dosyası oluşturulamadı.")
            eel.DisplayMessage("İnternet bağlantısı yok, ses dosyası oluşturulamadı.")
    except Exception as e:
        print(f"Ses oynatma sırasında hata oluştu: {e}")
        eel.DisplayMessage("Ses oynatma sırasında hata oluştu, lütfen tekrar deneyin.")

# Kullanıcıdan komut alacak fonksiyon
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        eel.DisplayMessage("Dinliyorum...")
        print('Dinliyorum...')
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=0.3)

        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            eel.DisplayMessage("Mikrofon zaman aşımına uğradı.")
            print("Mikrofon zaman aşımına uğradı.")
            return ''

    try:
        eel.DisplayMessage("Konuşma algılanıyor...")
        print('hmm...')
        query = r.recognize_google(audio, language='tr-TR,en-US')
        print(f'Kullanıcı Dedi ki: {query}')
        eel.DisplayMessage(f"Kullanıcı Dedi ki: {query}")
        time.sleep(2)

    except Exception as e:
        eel.DisplayMessage("Anlaşılamadı, lütfen tekrar deneyin.")
        print(f"Anlaşılamadı, lütfen tekrar deneyin. Hata: {e}")
        return ''

    return query.lower()

# Komutları açma fonksiyonu
def openCommand(query):
    try:
        query = query.replace("aç", "").strip()
        if query:
            print(f"{query} açılıyor...")
            os.system(f"start {query}")
            return f"{query} başarıyla açıldı."
        else:
            return "Lütfen geçerli bir komut girin."
    except Exception as e:
        print(f"openCommand sırasında hata: {e}")
        return "Komut çalıştırılamadı."

# YouTube oynatma fonksiyonu
def PlayYoutube(query):
    try:
        search_term = query.replace("youtube'da", "").replace("aç", "").strip()
        if search_term:
            print(f"YouTube'da {search_term} oynatılıyor...")
            kit.playonyt(search_term)
            return f"YouTube'da {search_term} oynatılıyor."
        else:
            return "YouTube için geçerli bir içerik bulunamadı."
    except Exception as e:
        print(f"PlayYoutube sırasında hata: {e}")
        return "YouTube komutu çalıştırılamadı."

@eel.expose
def allCommands(message=1):
    try:
        print("allCommands fonksiyonu çağrıldı")

        if message == 1:
            query = takecommand()
            print(f"Sesli komut alındı: {query}")
        else:
            query = message.strip()
            print(f"Chat komutu alındı: {query}")

        if not query:
            print("Komut alınamadı.")
            eel.DisplayMessage("Lütfen bir şey söyleyin.")
            return

        print(f"Gelen komut: {query}")

        if "aç" in query:
            response = openCommand(query)
        elif "youtube'da" in query.lower():
            response = PlayYoutube(query)
        else:
            response = "Bu komutu anlayamadım. Lütfen tekrar deneyin."

        print(f"İşlem Yanıtı: {response}")
        speak(response)

    except Exception as e:
        import traceback
        error_message = traceback.format_exc()
        print(f"Hata ayrıntısı: {error_message}")
        eel.DisplayMessage("Bir hata oluştu, lütfen tekrar deneyin.")
        speak("Bir hata oluştu, lütfen tekrar deneyin.")

    eel.ShowHood()
