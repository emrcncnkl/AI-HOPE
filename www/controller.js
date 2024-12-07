$(document).ready(function () {
    // Hazır mesajların listesi (döngüyle kullanılabilir)
    const readyMessages = [
        "Dinliyorum...",
        "Sesi algılıyorum...",
        "Konuşma analiz ediliyor...",
        "Sonuç oluşturuluyor..."
    ];

    let currentIndex = 0; // Mesaj sırasını takip etmek için bir değişken
    
    
    eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += '<div class="row justify-content-end mb-4">' +
                '<div class="width-size">' +
                '<div class="sender_message">' + message + '</div>' +
                '</div>' +
                '</div>';
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }
    
    eel.expose(receiverText)
    function receiverText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += '<div class="row justify-content-start mb-4">' +
                '<div class="width-size">' +
                '<div class="receiver_message">' + message + '</div>' +
                '</div>' +
                '</div>';
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }
    
    // Python'dan gelen mesajı işleyen fonksiyon
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        if (message === "useReadyMessages") {
            // Hazır mesajları döngüsel olarak göster
            const selectedMessage = readyMessages[currentIndex];
            $(".siri-message").text(selectedMessage);
            $(".siri-message").textillate('start');
            currentIndex = (currentIndex + 1) % readyMessages.length;
        } else {
            // Gelen mesajı doğrudan göster
            $(".siri-message").text(message || "Bir şey söylemediniz.");
            $(".siri-message").textillate('start');
        }
    }
    

    // Mikrofon butonuna tıklama olayını dinleyin
    $("#MicBtn").on("click", function () {
        // Mikrofondan dinleme başlatıldığında hazır mesaj döngüsünü başlat
        DisplayMessage("useReadyMessages");
    });
});
