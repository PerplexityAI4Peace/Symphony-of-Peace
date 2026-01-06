"""
peace_dashboard.py

A minimal terminal dashboard.
"""

from datetime import datetime
import math

class PeaceDashboard:
    SUN = ["·", "°", "o", "O", "☀"]
    COLORS = {
        "gentle": "🩵", "serene": "💙", "bright": "🌕", "warm": "🧡", "calm": "💚"
    }

    def __init__(self, logs):
        self.logs = logs

    def display(self):
        if not self.logs:
            print("No logs yet — horizon is patiently waiting.")
            return

        print("\n🌅  PEACE DASHBOARD")
        print("─────────────────────────────")
        for idx, log in enumerate(self.logs[-10:], start=1):
            tone = log["summary"].get("tone", "gentle")
            shade = self.COLORS.get(tone, "🤍")
            count = log["summary"].get("summary_count", 1)
            height = min(5, max(1, math.ceil(count / 2)))
            layers = "".join(self.SUN[:height])
            timestamp = datetime.fromisoformat(log["saved_at"]).strftime("%b %d %Y %H:%M UTC")
            print(f"{shade}  {layers:<5}  {tone.capitalize():<8}  — {timestamp}")

        print("─────────────────────────────")
        print("☀️  Each sunrise marks one act of peaceful creation.\n")

        summary_count = len(self.logs)
        tones = {log['summary']['tone'] for log in self.logs}
        print(f"Total Sessions : {summary_count}")
        print(f"Distinct Tones : {', '.join(tones)}")
        print("Dashboard complete — May your next dawn arrive softly.")
