$(document).ready(function () {
    $("body *").hide().fadeIn(2000);
    $(".text").textillate({
      loop: true,
      sync: true,
      in: {
        effect: "fadeIn",
        sync: true,
      },
      out: {
        effect: "fadeOut",
        sync: true,
      },
    });
  
    // Siri config
    var siriWave = new SiriWave({
      container: document.getElementById("siri-container"),
      width: 800,
      height: 200,
      style: "ios9",
      amplitude: "1",
      speed: "0.150",
      autostar: true,
    });
  
     // Rastgele mesajı almak için Python fonksiyonunu çağır
     function updateSiriMessage() {
      eel.get_random_prompt()(function (prompt) {
        $(".siri-message").fadeOut(5000, function () {
          $(this).text(prompt).fadeIn(5000);
        });
      });
    }
  
     // Rastgele mesajı almak ve ana sayfada göstermek için Python fonksiyonunu çağır
     function updateAssistantMessage() {
      eel.get_random_prompt()(function (prompt) {
        $("#assistantMessage").fadeOut(500, function () {
          $(this).text(prompt).fadeIn(500);
        });
      });
    }
  
    // Sayfa ilk yüklendiğinde bir mesaj göster
    updateAssistantMessage();
  
    // Belirli aralıklarla mesajları değiştir (örneğin, her 5 saniyede bir)
    setInterval(updateAssistantMessage, 5000);
  
    // Sayfa ilk yüklendiğinde bir mesaj göster
    updateSiriMessage();
  
    // Belirli aralıklarla mesajları değiştir (örneğin, her 5 saniyede bir)
    setInterval(updateSiriMessage, 4000);
    
    
    // Siri message animation
    $(".siri-message").textillate({
      loop: true,
      sync: true,
      in: {
        effect: "fadeInUp",
        sync: true,
      },
      out: {
        effect: "fadeOutUp",
        sync: true,
      },
    });
  
    // Mic button
    $("#MicBtn").click(function (e) {
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
      eel.allCommands()()
  
      // Python'daki play_mic_sound işlevini çağır
      eel.play_mic_sound();
    });
  });
  