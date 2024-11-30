import re


def extract_yt_term(command):
    # Youtube ile ilgili herhangi bir arama terimini yakalamak için düzenli ifade
    pattern = r'(?:youtube.*?)([\w\s]+)'  # Türkçe ve İngilizce destekler
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1).strip() if match else None  # None döner, varsayılan içerik kullanmaz
    
    # re.search kullanarak komut içinde eşleşme ara
    match = re.search(pattern, command, re.IGNORECASE)
    
    # Eğer bir eşleşme bulunursa, yakalanan şarkı adını döndür; aksi takdirde None döndür
    return match.group(1) if match else None 