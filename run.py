# Hope'u çalıştırmak için
import multiprocessing


def startHope():
        # Code for process 1
        print("1. İşlem Başlatılıyor.")
        from main import start
        start()

# Anahtar Kelimeyi çalıştırmak için
def listenHotword():
        # Code for process 2
        print("2. İşlem Başlatılıyor.")
        from engine.features import hotword
        hotword()

# Start both processes
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startHope)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        p2.start()
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("Sistem Durduruldu")