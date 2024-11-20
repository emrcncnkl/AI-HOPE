$(document).ready(function () {
    // Hazır mesajların listesi (döngüyle kullanılabilir)
    const readyMessages = [
        "Dinliyorum...",
        "Sesi algılıyorum...",
        "Konuşma analiz ediliyor...",
        "Sonuç oluşturuluyor..."
    ];

    let currentIndex = 0; // Mesaj sırasını takip etmek için bir değişken

    // Python'dan gelen mesajı işleyen fonksiyon
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        if (message === "useReadyMessages") {
            // Hazır mesajlardan sıradaki mesajı göster
            const selectedMessage = readyMessages[currentIndex];
            $(".siri-message").text(selectedMessage);
            $(".siri-message").textillate('start');

            // Sonraki mesaj için sırayı güncelle
            currentIndex = (currentIndex + 1) % readyMessages.length; // Döngüsel gösterim
        } else {
            // Python'dan gelen mesajı doğrudan göster
            $(".siri-message").text(message);
            $(".siri-message").textillate('start');
        }
    }

    // Mikrofon butonuna tıklama olayını dinleyin
    $("#MicBtn").on("click", function () {
        // Mikrofondan dinleme başlatıldığında hazır mesaj döngüsünü başlat
        DisplayMessage("useReadyMessages");
    });
});
