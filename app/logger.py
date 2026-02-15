import csv
import os
from datetime import datetime

LOG_FILE = "chat_logs.csv"

def log_chat(session_id: str, query: str, response: str, is_crisis: bool):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "session_id", "query", "response", "crisis"])

        writer.writerow([
            datetime.now().isoformat(),
            session_id,
            query,
            response,
            is_crisis
        ])