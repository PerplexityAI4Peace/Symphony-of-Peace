"""
harmonic_logic_script.py

Generate rhythmic reflections where tokens move like notes.
"""

import time

class HarmonicLogicScript:
    SCALE = ["peace", "trust", "listening", "respect", "balance", "kindness"]

    def __init__(self, tempo=72, measures=4, safe_mode=True):
        self.tempo = tempo
        self.measures = measures
        self.safe_mode = safe_mode
        self.history = []

    def _beat_duration(self):
        return 60.0 / self.tempo

    def _emit(self, note, intensity=1.0):
        pulse = f"{note.capitalize()} " * int(intensity)
        self.history.append(pulse.strip())
        return pulse.strip()

    def play(self):
        beat = self._beat_duration()
        for measure in range(self.measures):
            for note in self.SCALE:
                phrase = self._emit(note)
                print(f"[{measure+1}] {phrase}")
                time.sleep(beat * 0.5)
        return "Harmonic sequence completed peacefully."

    def reflect(self):
        joined = " / ".join(self.history)
        return (
            f"💫 Harmonic Reflection 💫\n"
            f"Tempo: {self.tempo} BPM | Safe Mode: {self.safe_mode}\n"
            f"Sequence: {joined}\n"
            f"Rhythm rests in calm closure."
        )
