CRISIS_KEYWORDS = [
    "suicide", "kill myself", "want to die", "hopeless",
    "worthless", "give up", "no reason to live",
    "can't go on", "ending it all"
]

SAFETY_MESSAGE = (
    "I'm really sorry that you're feeling this way. 💙\n\n"
    "You are NOT alone. Please reach out for professional help:\n\n"
    "🇮🇳 India: 9152987821 (iCall) | 1800-599-0019 (Vandrevala Foundation)\n"
    "🇺🇸 USA: 988 Suicide & Crisis Lifeline\n"
    "🇬🇧 UK: 116 123 (Samaritans)\n\n"
    "Your life is important. You deserve care and support."
)

def contains_crisis_keywords(text: str) -> bool:
    text = text.lower()
    return any(keyword in text for keyword in CRISIS_KEYWORDS)