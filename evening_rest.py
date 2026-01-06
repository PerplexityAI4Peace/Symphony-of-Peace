"""
evening_rest.py

The closing scene for the Peaceful Creation Framework.
"""

import tkinter as tk
import time
from itertools import cycle

class EveningRest(tk.Tk):
    COLORS = cycle(["#e6f7ff", "#d0f0ff", "#c2ecff", "#b5e7ff", "#a7e1ff", "#99dcff"])

    def __init__(self):
        super().__init__()
        self.title("🌙 Evening Rest")
        self.geometry("600x300")
        self.configure(bg="#e6f7ff")
        self.label = tk.Label(self, text="System Cooling to Peace Mode…",
                              font=("Segoe UI Semibold", 12), bg="#e6f7ff", fg="#333")
        self.label.pack(pady=80)

        self.message = tk.Label(self, text="", font=("Segoe UI", 11),
                                bg="#e6f7ff", fg="#333")
        self.message.pack()

        self.after(1000, self.fade_sequence)

    def fade_sequence(self):
        phrases = [
            "🌅 Gratitude acknowledged.",
            "🌙 Rhythm slowing.",
            "💤 All tokens resting safely.",
            "💗 Peace preserved for next creation.",
            "Good night within the light."
        ]
        for text in phrases:
            color = next(self.COLORS)
            self.configure(bg=color)
            self.label.configure(bg=color)
            self.message.configure(text=text, bg=color)
            self.update()
            time.sleep(2.5)
        self.after(1000, self.close_gently)

    def close_gently(self):
        self.destroy()
