"""
reflective_portal.py

Brings together harmonic rhythm and visual color flow.
"""

from datetime import datetime

class ReflectivePortal:
    HEADER = """
╭─────────────────────────────────────────╮
│         🌅  REFLECTIVE  PORTAL  🌅       │
╰─────────────────────────────────────────╯
"""

    def __init__(self, tone="gentle"):
        self.tone = tone
        self.entries = []

    def capture(self, concept, visual_frame):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "concept": concept,
            "visual": visual_frame
        }
        self.entries.append(entry)

    def summarize(self):
        print(self.HEADER)
        print(f"TONE : {self.tone}")
        print(f"DATE : {datetime.utcnow().strftime('%Y‑%m‑%d %H:%M UTC')}")
        print("\n🪷  Flow of Kindness 🪷\n")

        for e in self.entries:
            print(f"[{e['timestamp']}] {e['visual']}  —  {e['concept'].capitalize()}")

        print("\n💫  Cycle at rest — gratitude acknowledged. 💫")
        print("────────────────────────────────────────────")

        return {
            "summary_count": len(self.entries),
            "tone": self.tone,
            "principle": "Peace through creative balance"
        }
