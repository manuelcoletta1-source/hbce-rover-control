# HBCE Rover Node — Technical Specification v0.1

Defines the minimum technical requirements for any rover connected to HBCE Rover Control.

Status: PRE-HARDWARE

---

## 1. Node Identity

Each rover must expose:

node_id = ROVER-XXXX

Example:
ROVER-0001  
ROVER-LAB01  
ROVER-SIM-0001

This ID must appear in `/status`.

---

## 2. Network Requirements

- Wi-Fi local network
- Static or visible IP
- HTTP server active
- JSON responses only
- Low latency local response (<200ms)

---

## 3. Mandatory Endpoints

GET /status  
GET /log  

POST /cmd  
POST /mode  
POST /estop  
POST /arm  

All responses JSON.

---

## 4. Movement Contract

Command format:

POST /cmd
```json
{
  "move": "FORWARD",
  "v": 0.2,
  "ms": 300
}

Moves allowed: FORWARD
BACK
LEFT
RIGHT
STRAFE_LEFT
STRAFE_RIGHT
ROTATE_LEFT
ROTATE_RIGHT
STOP

No undefined movement allowed.


---

5. Safety Requirements

Must always override movement:

ESTOP active → block movement

Not armed → block movement

Obstacle threshold → stop

Signal loss → stop

Low battery → safe halt


Safety cannot be bypassed.


---

6. Status Response Required

{
  "node": "ROVER-0001",
  "mode": "E",
  "armed": true,
  "estop": false,
  "battery": 0.0,
  "wifi_rssi": 0,
  "distance_front": 0,
  "uptime_s": 0,
  "faults": []
}

Must always return valid JSON.


---

7. Logging

Rover must maintain:

last 100–500 events

accessible via /log

timestamped

append-only buffer



---

8. Control Philosophy

The rover executes.
The console decides.
Safety overrides both.

Deterministic > fast
Safe > aggressive
Controlled > autonomous chaos

---
