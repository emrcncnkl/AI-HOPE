import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import eel
import threading
from playsound import playsound
import time
pygame.mixer.init()

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
def allCommands():
    query = takecommand()  # Kullanıcıdan komut al
    if not query:  # Eğer komut boşsa, işlem yapılmasın
        print("Komut alınamadı.")
        eel.DisplayMessage("Lütfen bir şey söyleyin.")
        return

    print(f"Gelen komut: {query}")

    if "aç" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "youtube'da" in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)
    else:
        eel.DisplayMessage("Bu komutu anlayamadım. Lütfen tekrar deneyin.")

    eel.ShowHood()
 