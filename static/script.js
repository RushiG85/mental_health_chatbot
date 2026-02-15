async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  if (!input.value.trim()) return;

  let userMsg = document.createElement("div");
  userMsg.className = "message user";
  userMsg.innerText = input.value;
  chatBox.appendChild(userMsg);

  chatBox.scrollTop = chatBox.scrollHeight;

  let text = input.value;
  input.value = "";

  let response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      session_id: "web",
      query: text
    })
  });

  let data = await response.json();

  let botMsg = document.createElement("div");
  botMsg.className = "message bot";
  botMsg.innerText = data.response;
  chatBox.appendChild(botMsg);

  chatBox.scrollTop = chatBox.scrollHeight;
}