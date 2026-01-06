"""
grattitude_scroller.py

Adds a calm scrolling gratitude line to the Peace GUI.
"""

import tkinter as tk
import time
import threading
from gratitude_quote_generator import GratitudeQuoteGenerator

class GratitudeScroller(tk.Frame):
    def __init__(self, master, delay=0.2, refresh_interval=20):
        super().__init__(master, bg="#e6f7ff")
        self.pack(fill="x", side="bottom")
        self.delay = delay
        self.refresh_interval = refresh_interval
        self.quote = GratitudeQuoteGenerator.get_quote()
        self.label = tk.Label(self, text=f"  {self.quote}  ", bg="#e6f7ff",
                              fg="#333", font=("Segoe UI", 10))
        self.label.pack(side="left", padx=6)
        self.running = True

        threading.Thread(target=self._scroll_loop, daemon=True).start()
        threading.Thread(target=self._refresh_loop, daemon=True).start()

    def _scroll_loop(self):
        while self.running:
            text = self.label.cget("text")
            self.label.config(text=text[1:] + text[0])
            time.sleep(self.delay)

    def _refresh_loop(self):
        while self.running:
            time.sleep(self.refresh_interval)
            self.quote = GratitudeQuoteGenerator.get_quote()
            self.label.config(text=f"  {self.quote}  ")

    def stop(self):
        self.running = False
