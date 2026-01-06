"""
harmonic_visual_layer.py

Extends HarmonicLogicScript with calm visual simulation.
"""

import itertools
import time

class HarmonicVisualLayer:
    COLORS = {
        "peace": "🌊  soft blue",
        "trust": "🌿  gentle green",
        "listening": "🌸  rose pink",
        "respect": "🌼  warm gold",
        "balance": "🌙  silver gray",
        "kindness": "🔥  amber light"
    }

    WAVE = itertools.cycle(["~", "~~", "~~~", "~~"])

    def __init__(self, tempo=72):
        self.tempo = tempo
        self.frame_delay = 60.0 / tempo / 2
        self.visual_log = []

    def render(self, sequence):
        for concept in sequence:
            color = self.COLORS.get(concept, "⬜  white neutral")
            wave = next(self.WAVE)
            frame = f"{wave}  {color}  {wave}"
            self.visual_log.append(frame)
            print(frame)
            time.sleep(self.frame_delay)
        print("\n✨  Visual harmony complete.  ✨")
        return self.visual_log
