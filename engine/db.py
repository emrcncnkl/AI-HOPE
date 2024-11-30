import sqlite3

# Veritabanına bağlan
conn = sqlite3.connect("hope.db")
cursor = conn.cursor()

# Eğer sys_command tablosu yoksa oluştur (id, name ve path sütunlarıyla)
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# Yeni bir uygulama eklemek için aşağıdaki formatı kullanabilirsiniz:
# query = "INSERT INTO sys_command VALUES (null, '<uygulama_adı>', '<uygulama_dosya_yolu>')"
# ÖRNEK: 
# query = "INSERT INTO sys_command VALUES (null, 'opera', 'C:\\Users\\C V E X\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Opera GX Browser.exe')"
# cursor.execute(query)

# sys_command tablosuna örnek veri ekliyoruz
# query = "INSERT INTO sys_command VALUES (null, 'opera', 'C:\\Users\\C V E X\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Opera GX Browser.exe')"
#  cursor.execute(query)

# Eğer web_command tablosu yoksa oluştur (id, name ve path sütunlarıyla)
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# Yeni bir web bağlantısı eklemek için aşağıdaki formatı kullanabilirsiniz:
# query = "INSERT INTO web_command VALUES (null, '<bağlantı_adı>', '<url>')"
# ÖRNEK:
# query = "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com')"
# cursor.execute(query)

# web_command tablosuna örnek veri ekliyoruz
# query = "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com')"
# cursor.execute(query)

# Değişiklikleri kaydet
conn.commit()

# Kullanıcılara rehber:
# 1. Veritabanına yeni bir uygulama veya web bağlantısı eklemek için yukarıdaki "INSERT INTO" formatını kullanabilirsiniz.
# 2. <uygulama_adı>, <uygulama_dosya_yolu> veya <url> alanlarını doldurarak eklemelerinizi yapabilirsiniz.
# 3. Bu dosyayı çalıştırarak eklemelerinizi veritabanına kaydedebilirsiniz.
