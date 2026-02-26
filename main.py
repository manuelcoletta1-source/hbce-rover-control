import time
import json
import os
from datetime import datetime
import requests

# ============================================
# HBCE ROVER CONTROL — GROUND CONSOLE CORE
# ============================================

ROVER_URL = "http://192.168.1.50"   # cambierà quando il rover sarà online
LOG_DIR = "log"
LOG_FILE = f"{LOG_DIR}/console_events.log"

os.makedirs(LOG_DIR, exist_ok=True)

# --------------------------------------------
# HTTP CLIENT
# --------------------------------------------
def rover_get(endpoint):
    r = requests.get(f"{ROVER_URL}{endpoint}", timeout=3)
    return r.json()

def rover_post(endpoint, payload):
    r = requests.post(f"{ROVER_URL}{endpoint}", json=payload, timeout=3)
    return r.json()

# --------------------------------------------
# LOG APPEND ONLY
# --------------------------------------------
def log_event(data):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "ts": datetime.now().isoformat(),
            "data": data
        }) + "\n")

# --------------------------------------------
# COMMANDS
# --------------------------------------------
def send_move(move, v=0.2, ms=300):
    payload = {"move": move, "v": v, "ms": ms}
    return rover_post("/cmd", payload)

def set_mode(mode):
    return rover_post("/mode", {"mode": mode})

def estop(on=True):
    return rover_post("/estop", {"on": on})

def arm(token="lab"):
    return rover_post("/arm", {"token": token})

# --------------------------------------------
# MAIN LOOP
# --------------------------------------------
def main_loop():
    print("HBCE ROVER CONTROL — CONSOLE ACTIVE")
    print("Waiting rover telemetry...\n")

    while True:
        try:
            status = rover_get("/status")
            print(json.dumps(status, indent=2))
            log_event(status)
            time.sleep(2)

        except Exception as e:
            print("ROVER OFFLINE / CONNECTION FAIL:", e)
            time.sleep(3)

# --------------------------------------------
if __name__ == "__main__":
    main_loop()
