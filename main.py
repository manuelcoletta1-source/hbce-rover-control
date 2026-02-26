import time
import json
import os
from datetime import datetime

import config
from client import RoverClient

# ============================================
# HBCE ROVER CONTROL — TELEMETRY DAEMON
# - polls /status
# - writes append-only log records
# ============================================

os.makedirs(config.LOG_DIR, exist_ok=True)

def write_record(kind: str, data: dict):
    record = {
        "ts": datetime.now().isoformat(),
        "console": config.CONSOLE_ID,
        "kind": kind,
        "data": data
    }
    with open(config.LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def main():
    client = RoverClient()

    print("HBCE ROVER CONTROL — TELEMETRY DAEMON")
    print(f"Console: {config.CONSOLE_ID}")
    print(f"Rover URL: {config.ROVER_URL}")
    print(f"Polling interval: {config.POLL_INTERVAL_S}s\n")

    while True:
        try:
            status = client.status()
            print(json.dumps(status, indent=2, ensure_ascii=False))
            write_record("STATUS", status)
            time.sleep(config.POLL_INTERVAL_S)

        except Exception as e:
            err = {"error": str(e)}
            print("ROVER OFFLINE / CONNECTION FAIL:", err["error"])
            write_record("ERROR", err)
            time.sleep(max(1.0, config.POLL_INTERVAL_S))

if __name__ == "__main__":
    main()
