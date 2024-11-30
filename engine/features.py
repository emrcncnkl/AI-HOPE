import os
from playsound import playsound
import eel
import re
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import sqlite3  # SQLite modülünü içe aktar
import webbrowser  # Web tarayıcı kontrol modülünü içe aktar

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


def extract_yt_term(command):
    # Youtube ile ilgili herhangi bir arama terimini yakalamak için düzenli ifade
    pattern = r'(?:youtube.*?)([\w\s]+)'  # Türkçe ve İngilizce destekler
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1).strip() if match else None  # None döner, varsayılan içerik kullanmaz
    
    # re.search kullanarak komut içinde eşleşme ara
    match = re.search(pattern, command, re.IGNORECASE)
    
    # Eğer bir eşleşme bulunursa, yakalanan şarkı adını döndür; aksi takdirde None döndür
    return match.group(1) if match else None 
