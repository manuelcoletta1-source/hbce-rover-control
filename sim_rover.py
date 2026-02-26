from flask import Flask, request, jsonify
from datetime import datetime
import random
import time

app = Flask(__name__)

# ============================================
# STATE
# ============================================

state = {
    "node": "ROVER-SIM-0001",
    "mode": "E",
    "armed": True,
    "estop": False,
    "battery": 7.4,
    "wifi_rssi": -55,
    "distance_front": 120,
    "uptime_s": 0,
    "faults": []
}

log_buffer = []
start_time = time.time()

# ============================================
# LOG
# ============================================

def add_log(ev, lvl="INFO", extra=None):
    entry = {
        "ts": datetime.now().isoformat(),
        "lvl": lvl,
        "ev": ev
    }
    if extra:
        entry.update(extra)
    log_buffer.append(entry)

# ============================================
# ROUTES
# ============================================

@app.route("/status", methods=["GET"])
def status():
    state["uptime_s"] = int(time.time() - start_time)
    state["distance_front"] = random.randint(20, 150)
    return jsonify(state)

@app.route("/log", methods=["GET"])
def get_log():
    return jsonify(log_buffer[-50:])

@app.route("/cmd", methods=["POST"])
def cmd():
    data = request.json
    move = data.get("move", "UNKNOWN")

    if state["estop"] or not state["armed"]:
        add_log("CMD_BLOCKED", "WARN", {"move": move})
        return jsonify({"ok": False, "reason": "NOT_ARMED"})

    add_log("MOVE", extra={"move": move})
    return jsonify({"ok": True, "move": move})

@app.route("/mode", methods=["POST"])
def mode():
    data = request.json
    m = data.get("mode", "E")
    state["mode"] = m
    add_log("MODE_SET", extra={"mode": m})
    return jsonify({"ok": True, "mode": m})

@app.route("/estop", methods=["POST"])
def estop():
    data = request.json
    on = data.get("on", True)
    state["estop"] = on
    add_log("ESTOP", "WARN", {"on": on})
    return jsonify({"ok": True, "estop": on})

@app.route("/arm", methods=["POST"])
def arm():
    state["armed"] = True
    state["estop"] = False
    add_log("ARMED")
    return jsonify({"ok": True, "armed": True})

# ============================================

if __name__ == "__main__":
    print("HBCE ROVER SIMULATOR ACTIVE")
    app.run(host="0.0.0.0", port=5000)
