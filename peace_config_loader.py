"""
peace_config_loader.py

Reads the peace_config.json file to share preferences across modules.
"""

import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "peace_config.json"

def load_config():
    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print("⚠️  Error reading config, using defaults:", e)
    return {
        "tempo_bpm": 72,
        "session_minutes": 10,
        "tone": "gentle",
        "color_palette": ["#bde0fe", "#caf0f8", "#ade8f4", "#90e0ef", "#89c2d9"],
        "affirmations": [
            "🕊️  Peace — I engage in calm, non‑violent communication.",
            "💗  Love — I act from respect and goodwill, not dependency.",
            "🌱  Respect — I honor boundaries and limitations of all beings."
        ]
    }
