document.addEventListener("DOMContentLoaded", function () {
    const userInput = document.getElementById("user-input");
    const messages = document.getElementById("chatbot-messages");
    const sendButton = document.getElementById("send-button");

    if (!userInput || !messages || !sendButton) {
        console.error("Chatbot elements missing!");
        return;
    }

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        if (!userInput.value.trim()) return;

        const userMessage = document.createElement("div");
        userMessage.textContent = userInput.value;
        userMessage.style.textAlign = "right";
        userMessage.style.margin = "10px";
        userMessage.style.backgroundColor = "#e0f7fa";
        userMessage.style.padding = "10px";
        userMessage.style.borderRadius = "8px";

        messages.appendChild(userMessage);

        fetch("/api/chatbot", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userInput.value }),
        })
            .then((response) => response.json())
            .then((data) => {
                const botMessage = document.createElement("div");
                botMessage.textContent = data.reply || "I'm here to assist you!";
                botMessage.style.margin = "10px";
                botMessage.style.backgroundColor = "#f1f1f1";
                botMessage.style.padding = "10px";
                botMessage.style.borderRadius = "8px";

                messages.appendChild(botMessage);
            })
            .catch((error) => {
                console.error("Error fetching chatbot response:", error);
            });

        userInput.value = "";
    }
});
