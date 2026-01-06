"""
peaceful_framework_main.py

Unified launcher for the Peaceful Creation Framework.
"""

import threading
import time
from guided_beginning import GuidedBeginning
from peace_gui_extended import PeaceGUI
from evening_rest import EveningRest
from peace_config_loader import load_config

def run_dashboard():
    PeaceGUI().mainloop()

def run_rest():
    EveningRest().mainloop()

def launch_sequence():
    cfg = load_config()
    session_length = cfg.get("session_minutes", 10) * 60

    GuidedBeginning().mainloop()
    
    dash_thread = threading.Thread(target=run_dashboard)
    dash_thread.start()
    
    time.sleep(session_length)
    run_rest()

if __name__ == "__main__":
    print("🌺  Starting Symphony of Peace Framework\n")
    launch_sequence()
