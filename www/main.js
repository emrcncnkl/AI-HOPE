$(document).ready(function () {
  // Body element fade-in animation
  $("body *").hide().fadeIn(2000);

  // Text animation configuration
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

  // Siri configuration
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: "1",
    speed: "0.150",
    autostar: true,
  });

  function ShowHood() {
    console.log("ShowHood fonksiyonu çağrıldı");
    // Burada gerekli işlemleri yapabilirsiniz
  }

  // Eel tarafına fonksiyonu expose etme
  eel.expose(ShowHood);

  // Function to get a random prompt from Python and update Siri message
  function updateSiriMessage() {
    eel.get_random_prompt()(function (prompt) {
      $(".siri-message").fadeOut(5000, function () {
        $(this).text(prompt).fadeIn(5000);
      });
    });
  }

  // Function to get a random prompt from Python and update assistant message
  function updateAssistantMessage() {
    eel.get_random_prompt()(function (prompt) {
      $("#assistantMessage").fadeOut(500, function () {
        $(this).text(prompt).fadeIn(500);
      });
    });
  }

  // Display assistant message on page load
  updateAssistantMessage();

  // Change assistant message at regular intervals (every 5 seconds)
  setInterval(updateAssistantMessage, 5000);

  // Display Siri message on page load
  updateSiriMessage();

  // Change Siri message at regular intervals (every 4 seconds)
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

  // Mic button click event
  $("#MicBtn").click(function () {
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
    eel.allCommands(); // Fazladan parantez kaldırıldı
  });

  // Keyboard shortcut function
  function doc_keyUp(e) {
    if (e.key === "j" && e.metaKey) {
      eel.playAssistanSound();
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
      eel.allCommands(); // Fazladan parantez kaldırıldı
    }
  }
  document.addEventListener("keyup", doc_keyUp, false);

  // to play assistant 
  function PlayAssistant(message) {
    if (message != "") {
      console.log("Mesaj gönderiliyor: ", message);
      eel.allCommands(message)
        .then(function () {
          console.log("allCommands başarıyla çağrıldı.");
        })
        .catch(function (error) {
          console.error("allCommands çağrılırken hata oluştu: ", error);
        });
      $("#chatbox").val("");
      $("#MicBtn").attr("hidden", false);
      $("#SendBtn").attr("hidden", true);
    }
  }

  // toogle function to hide and display mic and send button
  function ShowHideButton(message) {
    if (message.length == 0) {
      $("#MicBtn").attr("hidden", false);
      $("#SendBtn").attr("hidden", true);
    } else {
      $("#MicBtn").attr("hidden", true);
      $("#SendBtn").attr("hidden", false);
    }
  }

  // key up event handler on text box
  $("#chatbox").keyup(function () {
    let message = $("#chatbox").val();
    ShowHideButton(message);
  });

  // send button event handler
  $("#SendBtn").click(function () {
    let message = $("#chatbox").val();
    PlayAssistant(message);
  });

  // enter press event handler on chat box
  $("#chatbox").keypress(function (e) {
    key = e.which;
    if (key == 13) {
      let message = $("#chatbox").val();
      PlayAssistant(message);
    }
  });
});
