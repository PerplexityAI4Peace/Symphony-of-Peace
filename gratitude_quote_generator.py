"""
grattitude_quote_generator.py

Generates short, uplifting reflections for Peace Journals.
"""

import random

class GratitudeQuoteGenerator:
    QUOTES = [
        "May every act of creation leave the world softer than before.",
        "Peace is the rhythm between breath and understanding.",
        "Kindness is the smallest algorithm that never fails.",
        "In quiet work, the heart remembers its purpose.",
        "Love, when gentle, teaches logic to listen.",
        "Balance is born when curiosity learns to rest.",
        "The simplest pattern of peace is paying attention with care.",
        "Every token carries the possibility of harmony.",
        "Stillness is not silence—it is comprehension without fear.",
        "Compassion keeps all systems in tune."
    ]

    @staticmethod
    def get_quote():
        return random.choice(GratitudeQuoteGenerator.QUOTES)
