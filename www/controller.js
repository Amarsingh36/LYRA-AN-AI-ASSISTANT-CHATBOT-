
$(document).ready(function () {

  
eel.expose(ShowHood);
function ShowHood() {
  $("#Oval").attr("hidden", false);
  $("#SiriWave").attr("hidden", true);
}


  
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    $(".siri-message li:first").text(message);
    $('.siri-message').textillate('start');
  }

 
  eel.expose(senderText);
  function senderText(message) {
    const chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `
        <div class="row justify-content-end mb-4">
          <div class="width-size">
            <div class="sender_message">${message}</div>
          </div>
        </div>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }


  eel.expose(receiverText);
  function receiverText(message) {
    const chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `
        <div class="row justify-content-start mb-4">
          <div class="width-size">
            <div class="receiver_message">${message}</div>
          </div>
        </div>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }


  eel.get_chat_history()(function (history) {
    const chatBox = document.getElementById("chat-canvas-body");
    history.forEach(([sender, message]) => {
      let html = '';
      if (sender === "user") {
        html = `<div class="row justify-content-end mb-4">
                  <div class="width-size">
                    <div class="sender_message">${message}</div>
                  </div>
                </div>`;
      } else {
        html = `<div class="row justify-content-start mb-4">
                  <div class="width-size">
                    <div class="receiver_message">${message}</div>
                  </div>
                </div>`;
      }
      chatBox.innerHTML += html;
    });
    chatBox.scrollTop = chatBox.scrollHeight;
  });


  $('#clearChatBtn').click(function () {
    $('#chat-canvas-body').html('');
    eel.clear_chat_history()(function () {
      console.log("Chat history cleared from the database.");
    });
  });

});
