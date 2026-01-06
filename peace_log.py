"""
peace_log.py

Adds persistence to the Reflective Portal.
"""

import json
from pathlib import Path
from datetime import datetime

class PeaceLog:
    DEFAULT_FILE = Path("peace_logs.json")

    def __init__(self, file_path=None):
        self.file_path = Path(file_path) if file_path else self.DEFAULT_FILE
        self.logs = self._load_file()

    def _load_file(self):
        if self.file_path.exists():
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_cycle(self, reflection_summary, entries):
        snapshot = {
            "saved_at": datetime.utcnow().isoformat(),
            "summary": reflection_summary,
            "entries": entries
        }
        self.logs.append(snapshot)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.logs, f, indent=2, ensure_ascii=False)
        print(f"🌾 Peace Log saved → {self.file_path}")
        return snapshot

    def reopen_all(self):
        if not self.logs:
            print("No peace logs yet—each day is a fresh beginning.")
            return []
        print(f"📖  Loaded {len(self.logs)} peace log(s).")
        for log in self.logs:
            date = log["saved_at"]
            tone = log["summary"]["tone"]
            print(f"• {date}  —  tone {tone}")
        return self.logs
