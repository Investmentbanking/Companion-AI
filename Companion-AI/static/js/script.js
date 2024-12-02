const chatForm = document.getElementById("chat-form")
const userMessage = document.getElementById("user-message")
const personalitySelector = document.getElementById("personality-selector")
const chatHistory = document.getElementById("chat-history");
const chatWindow = document.getElementById("chat-window");


// Event listener listens for submit event and prevents default form submission using
// preventDefault method, prevents page from refreshing
chatForm.addEventListener("submit", function(event) {
    event.preventDefault();

    const userMessageValue = userMessage.value
    const personalitySelectorValue = personalitySelector.value


    // If message empty or consists only of spaces triggers alert
    if(!userMessageValue.trim()) {
        alert("Please enter a message!");
        return;
    }

    // triggers function & adds users message to chat window
    appendMessage(userMessageValue, "user")

    // creates object with users message and selected personality
    // JS object
    const data = {
        user_input: userMessageValue,
        personality: personalitySelectorValue
    };

    // sends http post request to /chat endpoint of backend
    fetch("/chat", {
        method: "POST",
        // data sent in JSON format
        headers: {
            "Content-Type": "application/json"
        },
        // converts data object into JSON string & sends to backend
        body: JSON.stringify(data)
    })
        // handles response from backend
        .then(response => {
            // checks if response is okay (200 status), if not throws error
            if (!response.ok) {
                throw new Error("Network response now OK");
            }
            // returns response into JSON object
            return response.json();
        })
        // appends chatbots response from backend to chat history
        // data is the response object
        .then(data => {
            appendMessage(data.response, "bot");
        })
        // logs errors 
        .catch(error => {
            console.error("Error:", error);
            appendMessage("Something went wrong please try again later", "bot");
        })
   
        // resets input field
        userMessage.value = "";
    


    // validateForm();
});

function appendMessage(message, sender) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message");
    messageElement.classList.add(sender);
    messageElement.textContent = message;

    chatHistory.appendChild(messageElement);

    // setTimeout(() => {
    //     chatHistory.scrollTop = chatHistory.scrollHeight;
    // }, 0);

    chatWindow.scrollTop = chatWindow.scrollHeight;
}

personalitySelector.addEventListener()

