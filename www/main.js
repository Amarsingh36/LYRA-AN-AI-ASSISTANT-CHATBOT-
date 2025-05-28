

//   $('.text').textillate({
//       loop: true,
//       sync: true,
//       in: {
//           effect: "bounceIn",
//       },
//       out: {
//           effect: "bounceOut",
//       },

//   });

  
// Initialize SiriWave
// SiriWave Initialization

// Initialize SiriWave animation
var SiriWave = new SiriWave({
  container: document.getElementById("siri-container"),
  width: 800,
  height: 200,
  style:  "ios9",
  amplitude: "1",
  speed: "0.30",
  autostart: true
});

$('.siri-message').textillate({
  loop: true,
  sync: true,
  in: {
      effect: "bounce",
      sync: true,
  },
  out: {
      effect: "flipOutY",
      sync: true,
  },

});


$("#MicBtn").click(function () {
    eel.playAssistantsound(); 
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
    eel.allCommands();
  });
  
  