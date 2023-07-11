class Chatbox {
    constructor() {
      this.args = {
        chatBox: document.querySelector(".chatbox__support"),
        sendButton: document.querySelector(".send__button"),
        micbtn: document.querySelector(".mic"),
      };
  
      this.state = false;
      this.messages = [];
    }
  
    display() {
      const { chatBox, sendButton, micbtn } = this.args;
  
      sendButton.addEventListener("click", () => this.onSendButton(chatBox));
      micbtn.addEventListener("click", () => this.speak(chatBox));
  
      const node = chatBox.querySelector("input");
      node.addEventListener("keyup", ({ key }) => {
        if (key === "Enter") {
          this.onSendButton(chatBox);
        }
      });
    }
  
    toggleState(chatbox) {
      this.state = !this.state;
  
      // show or hide the box
      if (this.state) {
        chatbox.classList.add("chatbox--active");
      } else {
        chatbox.classList.remove("chatbox--active");
      }
    }
  
    speak(chatbox) {
      console.log("clicked");
      var m = [];
      m = this.messages;
      console.log(m.length);
  
      if ("SpeechRecognition" in window || "webkitSpeechRecognition" in window) {
        // Create speech recognition object
        const SpeechRecognition =
          window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();
  
        // Configure recognition settings
        recognition.continuous = true;
        recognition.lang = "en";
  
        recognition.onstart = function () {
          console.log("listening");
        };
  
        recognition.onspeechend = function () {
          console.log("end");
          recognition.stop();
        };
  
        recognition.onresult = function (event) {
          var transcript = event.results[0][0].transcript.toLowerCase();
          console.log(transcript);
          console.log(typeof transcript);
  
          let msg1 = { name: "User", message: transcript };
          m.push(msg1);
  
          var html = "";
          m
            .slice()
            .reverse()
            .forEach(function (item, index) {
              html +=
                '<div class="messages__item messages__item--operator">' +
                item.message +
                "</div>";
            });
  
          const chatmessage = chatbox.querySelector(".chatbox__messages");
          chatmessage.innerHTML = html;
  
          let text1 = transcript;
          if (text1 === "") {
            return;
          }
  
          fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            body: JSON.stringify({ message: text1 }),
            mode: "cors",
            headers: {
              "Content-Type": "application/json",
            },
          })
            .then((r) => r.json())
            .then((r) => {
              let msg2 = { name: "Aafhana", message: r.answer };
              let speech = new SpeechSynthesisUtterance();
              speech.lang = "en";
              speech.text = msg2.message;
              m.push(msg2);
  
              window.speechSynthesis.speak(speech);
              var html = "";
              m
                .slice()
                .reverse()
                .forEach(function (item, index) {
                  if (item.name === "Aafhana") {
                    html +=
                      '<div class="messages__item messages__item--visitor">' +
                      item.message +
                      "</div>";
                  } else {
                    html +=
                      '<div class="messages__item messages__item--operator">' +
                      item.message +
                      "</div>";
                  }
                });
  
              const chatmessage = chatbox.querySelector(".chatbox__messages");
              chatmessage.innerHTML = html;
            })
            .catch((error) => {
              console.error("Error:", error);
            });
        };
  
        recognition.start();
      } else {
        console.log("Speech recognition not supported in this browser");
      }
    }
  
    onSendButton(chatbox) {
      var textField = chatbox.querySelector("input");
      let text1 = textField.value;
  
      if (text1 === "") {
        return;
      }
  
      let msg1 = { name: "User", message: text1 };
      this.messages.push(msg1);
  
      this.displayLoadingMessage(chatbox);
  
      fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: JSON.stringify({ message: text1 }),
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((r) => r.json())
        .then((r) => {
          let msg2 = { name: "Aafhana", message: r.answer };
          this.messages.push(msg2);
          this.updateChatText(chatbox);
          textField.value = "";
        })
        .catch((error) => {
          console.error("Error:", error);
          this.updateChatText(chatbox);
          textField.value = "";
        });
    }
  
    displayLoadingMessage(chatbox) {
      const chatmessage = chatbox.querySelector(".chatbox__messages");
      chatmessage.innerHTML +=
        '<div class="messages__item messages__item--operator">Loading...</div>';
    }
  
    updateChatText(chatbox) {
      var html = "";
      this.messages
        .slice()
        .reverse()
        .forEach(function (item, index) {
          if (item.name === "Aafhana") {
            html +=
              '<div class="messages__item messages__item--visitor">' +
              item.message +
              "</div>";
          } else {
            html +=
              '<div class="messages__item messages__item--operator">' +
              item.message +
              "</div>";
          }
        });
  
      const chatmessage = chatbox.querySelector(".chatbox__messages");
      chatmessage.innerHTML = html;
    }
  }
  
  const chatbox = new Chatbox();
  chatbox.display();
  