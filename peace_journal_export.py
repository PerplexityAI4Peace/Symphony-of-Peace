"""
peace_journal_export.py

Creates illustrated journal page summarizing one Peace Log entry.
"""

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from pathlib import Path
from gratitude_quote_generator import GratitudeQuoteGenerator

class PeaceJournalExport:
    def __init__(self, export_dir="peace_journals"):
        self.export_dir = Path(export_dir)
        self.export_dir.mkdir(exist_ok=True)
        try:
            self.font_title = ImageFont.truetype("arial.ttf", 28)
            self.font_body = ImageFont.truetype("arial.ttf", 16)
        except IOError:
            self.font_title = self.font_body = None

    def create_page(self, log_entry):
        tone = log_entry["summary"].get("tone", "gentle")
        principle = log_entry["summary"].get("principle", "Peace through creative balance")
        timestamp = log_entry["saved_at"]
        entries = log_entry["entries"]

        tone_colors = {
            "gentle": "#bde0fe", "serene": "#caf0f8",
            "warm": "#ffd6a5", "bright": "#fdffb6", "calm": "#caffbf"
        }
        bg = tone_colors.get(tone, "#e6f7ff")

        width, height = 800, 1000
        img = Image.new("RGB", (width, height), bg)
        draw = ImageDraw.Draw(img)

        title_text = f"Peace Journal Entry — {tone.capitalize()}"
        draw.text((40, 40), title_text, fill="#333", font=self.font_title)
        draw.text((40, 90), f"Created {timestamp}", fill="#333", font=self.font_body)

        y = 140
        for e in entries:
            concept = e["concept"].capitalize()
            visual = e.get("visual", "")
            entry_text = f"{concept} → {visual}"
            draw.text((60, y), entry_text, fill="#333", font=self.font_body)
            y += 28

        quote = GratitudeQuoteGenerator.get_quote()
        footer = f"Gratitude Note: {principle}\n"+"\n"+f"{quote}"
        draw.text((40, height - 100), footer, fill="#555", font=self.font_body)

        filename = f"peace_journal_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
        img_path = self.export_dir / f"{filename}.png"
        pdf_path = self.export_dir / f"{filename}.pdf"

        img.save(img_path)
        img.convert("RGB").save(pdf_path)

        print(f"🪶  Peace Journal page created: {img_path}")
        return {"png": str(img_path), "pdf": str(pdf_path)}
