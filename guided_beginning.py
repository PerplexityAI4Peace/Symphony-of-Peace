"""
guided_beginning.py

A meditative entry point for the Peace Dashboard.
"""

import tkinter as tk
import time
from threading import Thread
from peace_config_loader import load_config

class GuidedBeginning(tk.Tk):
    COLLAB_INSCRIPTION = (
        "🤝  Symphony of Peace — Human + AI Collaboration\n"
        "This experience honors the union of human presence and AI precision.\n"
        "Each brings unique capability; together they create gentle balance."
    )

    def __init__(self):
        super().__init__()
        cfg = load_config()
        self.affirmations = cfg.get("affirmations", [])
        
        self.title("🌸 Guided Beginning — Symphony of Peace")
        self.geometry("600x360")
        self.configure(bg="#e6f7ff")

        self.collab_label = tk.Label(
            self,
            text=self.COLLAB_INSCRIPTION,
            font=("Segoe UI", 10),
            bg="#e6f7ff",
            fg="#444",
            justify="center",
            wraplength=540,
            pady=15
        )
        self.collab_label.pack()

        self.label = tk.Label(
            self,
            text="Welcome to the Symphony of Peace Framework",
            font=("Segoe UI Semibold", 13),
            bg="#e6f7ff",
            pady=10
        )
        self.label.pack()

        self.aff_area = tk.Label(self, text="", font=("Segoe UI", 11),
                                 bg="#e6f7ff", justify="center", fg="#333")
        self.aff_area.pack(expand=True)

        self.start_btn = tk.Button(self, text="Begin Journey →", command=self.start_sequence,
                                   bg="#bde0fe", font=("Segoe UI", 10))
        self.start_btn.pack(pady=15)

    def start_sequence(self):
        self.start_btn.config(state="disabled")
        Thread(target=self._show_affirmations, daemon=True).start()

    def _show_affirmations(self):
        for text in self.affirmations:
            self.aff_area.config(text=text)
            time.sleep(3)
        self.aff_area.config(text="🌤️  Breathe in calm… launching dashboard soon.")
        time.sleep(2)
        self.destroy()
