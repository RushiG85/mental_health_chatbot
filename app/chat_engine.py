import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

memory_store = {}

def get_response(session_id: str, user_input: str) -> str:
    if session_id not in memory_store:
        memory_store[session_id] = []

    messages = memory_store[session_id]

    # Keep only last 4 messages to avoid overload
    messages = messages[-4:]
    memory_store[session_id] = messages

    prompt = (
        "You are a calm, supportive, empathetic mental health assistant.\n"
        "Give gentle, caring, and supportive responses.\n\n"
    )

    for role, content in messages:
        prompt += f"{role}: {content}\n"

    prompt += f"user: {user_input}\nassistant:"

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        data = response.json()
        reply = data.get("response", "").strip()

        if not reply:
            reply = "I'm here with you. Please tell me more about how you're feeling."

    except Exception as e:
        reply = "I'm here for you. Please try again in a moment."

    messages.append(("user", user_input))
    messages.append(("assistant", reply))

    return reply