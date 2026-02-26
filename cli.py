import json
import time
from datetime import datetime

import config
from client import RoverClient

# ============================================
# HBCE ROVER CONTROL — CLI
# - manual command interface for lab testing
# - safe defaults
# ============================================

HELP = """
HBCE Rover Control — CLI

Movement:
  w = forward
  s = back
  a = left
  d = right
  q = strafe_left
  e = strafe_right
  z = rotate_left
  c = rotate_right
  x = stop

Modes:
  1 = mode E (exploration)
  2 = mode S (security)
  3 = mode R (rescue)

Safety:
  ! = ESTOP ON
  @ = ESTOP OFF (requires ARM)
  r = ARM (re-arm rover)

Telemetry:
  t = read /status
  l = read /log

Other:
  h = help
  p = ping loop (poll /status)
  exit = quit
"""

MOVE_MAP = {
    "w": "FORWARD",
    "s": "BACK",
    "a": "LEFT",
    "d": "RIGHT",
    "q": "STRAFE_LEFT",
    "e": "STRAFE_RIGHT",
    "z": "ROTATE_LEFT",
    "c": "ROTATE_RIGHT",
    "x": "STOP",
}

MODE_MAP = {
    "1": "E",
    "2": "S",
    "3": "R",
}

def pretty(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False))

def main():
    client = RoverClient()

    print("HBCE ROVER CONTROL — CLI")
    print(f"Rover URL: {config.ROVER_URL}")
    print(HELP)

    while True:
        cmd = input("> ").strip().lower()

        if cmd in ("exit", "quit"):
            print("Bye.")
            break

        if cmd in ("h", "help", "?"):
            print(HELP)
            continue

        try:
            if cmd in MOVE_MAP:
                move = MOVE_MAP[cmd]
                res = client.cmd(move, v=0.2, ms=300)
                pretty(res)
                continue

            if cmd in MODE_MAP:
                mode = MODE_MAP[cmd]
                res = client.mode(mode)
                pretty(res)
                continue

            if cmd == "!":
                pretty(client.estop(True))
                continue

            if cmd == "@":
                # estop off often requires arm; we keep it explicit
                pretty(client.estop(False))
                continue

            if cmd == "r":
                pretty(client.arm("lab"))
                continue

            if cmd == "t":
                pretty(client.status())
                continue

            if cmd == "l":
                pretty(client.log())
                continue

            if cmd == "p":
                print("Polling /status (Ctrl+C to stop)...")
                while True:
                    st = client.status()
                    print(datetime.now().isoformat(), st.get("mode"), st.get("faults"), st.get("distance_front"))
                    time.sleep(config.POLL_INTERVAL_S)

            print("Unknown command. Press 'h' for help.")

        except KeyboardInterrupt:
            print("\nStopped polling.")
            continue
        except Exception as e:
            print("ERROR:", str(e))

if __name__ == "__main__":
    main()
