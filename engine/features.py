import os
from playsound import playsound
import eel
import re
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import sqlite3  # SQLite modülünü içe aktar
import webbrowser
import struct
import time
import pvporcupine
import pyaudio
import pyautogui as autogui
from engine.helper import extract_yt_term  # Web tarayıcı kontrol modülünü içe aktar
from hugchat import hugchat
# Veritabanına bağlanma ve cursor tanımlama
conn = sqlite3.connect("hope.db")  # hope.db SQLite veritabanı dosyanız
cursor = conn.cursor()  # Veritabanı cursor'ı

@eel.expose
def playasssistantSound():
    music_dir = "www/sounds/Start.mp3"
    if os.path.exists(music_dir):
        playsound(music_dir)
    else:
        print(f"Ses dosyası bulunamadı: {music_dir}")


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("aç", "")
    query.lower()
    app_name = query.strip()
    if app_name != "":  # Eğer uygulama adı boş değilse

        try:
            # Veritabanında uygulama yolu arıyoruz
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:  # Eğer sonuç bulunursa
                speak(query + " açılıyor")
                os.startfile(results[0][0])  # Uygulamayı başlat

            elif len(results) == 0:  # Eğer sonuç bulunamazsa, web bağlantılarını kontrol et
                cursor.execute(
                    'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:  # Eğer bir web bağlantısı bulunursa
                    speak(query + " açılıyor")
                    webbrowser.open(results[0][0])  # Web tarayıcısında bağlantıyı aç

                else:
                    # Eğer hem uygulama hem web bağlantısı bulunamazsa, komut satırında çalıştırmayı dene
                    speak(query + " açılıyor")
                    try:
                        os.system('start '+query)
                    except:
                        speak("Maalesef bulunamadı")  # Komut çalışmazsa hata mesajı ver
        except:
            speak("Bir hata oluştu")  # Genel bir hata durumunda mesaj


        else:
            speak("üzgünüm istediğini bulamadım...")
    
def PlayYoutube(query):
    search_term = extract_yt_term(query)  # Arama terimini çıkart
    if not search_term:  # Eğer None ise, işlem yapılmasın
        speak("Youtube'da oynatılacak bir içerik bulunamadı.")
        print("Youtube'da oynatılacak bir içerik bulunamadı.")
        return
    
    # Eğer geçerli bir terim varsa, videoyu oynat
    speak("Youtube'da " + search_term + " oynatılıyor")
    kit.playonyt(search_term)



def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["hope","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("anahtar kelime algılandı")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response
