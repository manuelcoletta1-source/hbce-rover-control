import time
import json
import os
from datetime import datetime
import requests

import config

# ============================================
# HBCE ROVER CONTROL — GROUND CONSOLE CORE
# - telemetry poll
# - command helpers
# - append-only log
# ============================================

os.makedirs(config.LOG_DIR, exist_ok=True)

# --------------------------------------------
# HTTP CLIENT
# --------------------------------------------
def rover_get(endpoint: str):
    r = requests.get(f"{config.ROVER_URL}{endpoint}", timeout=config.HTTP_TIMEOUT_S)
    r.raise_for_status()
    return r.json()

def rover_post(endpoint: str, payload: dict):
    r = requests.post(
        f"{config.ROVER_URL}{endpoint}",
        json=payload,
        timeout=config.HTTP_TIMEOUT_S
    )
    r.raise_for_status()
    return r.json()

# --------------------------------------------
# LOG APPEND ONLY
# --------------------------------------------
def log_event(kind: str, data: dict):
    record = {
        "ts": datetime.now().isoformat(),
        "console": config.CONSOLE_ID,
        "kind": kind,
        "data": data
    }
    with open(config.LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

# --------------------------------------------
# COMMANDS (reserved for Step 1 runtime)
# --------------------------------------------
def send_move(move: str, v: float = 0.2, ms: int = 300):
    return rover_post("/cmd", {"move": move, "v": v, "ms": ms})

def set_mode(mode: str):
    return rover_post("/mode", {"mode": mode})

def estop(on: bool = True):
    return rover_post("/estop", {"on": on})

def arm(token: str = "lab"):
    return rover_post("/arm", {"token": token})

# --------------------------------------------
# MAIN LOOP
# --------------------------------------------
def main_loop():
    print("HBCE ROVER CONTROL — CONSOLE ACTIVE")
    print(f"Console: {config.CONSOLE_ID}")
    print(f"Rover URL: {config.ROVER_URL}")
    print("Polling /status ...\n")

    while True:
        try:
            status = rover_get("/status")
            print(json.dumps(status, indent=2, ensure_ascii=False))
            log_event("STATUS", status)
            time.sleep(config.POLL_INTERVAL_S)

        except Exception as e:
            err = {"error": str(e)}
            print("ROVER OFFLINE / CONNECTION FAIL:", err["error"])
            log_event("ERROR", err)
            time.sleep(max(1.0, config.POLL_INTERVAL_S))

# --------------------------------------------
if __name__ == "__main__":
    main_loop()
