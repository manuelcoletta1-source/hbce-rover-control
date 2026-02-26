# HBCE Rover Node Protocol — v0.1 (LAB)

Defines operational states, safety rules and HTTP contract
for rover units used in exploration, security and rescue.

---

## 1. Operational Modes

### E — Exploration
- Default speed: low
- Collision threshold: strict
- Auto-avoid enabled
- Logging: movement + obstacle events

### S — Security
- Patrol path or controlled loop
- Anomaly detection events
- Silent safe-stop on critical event
- Full logging

### R — Rescue
- Reduced max speed
- Manual override priority
- Beacon enabled (light / sound)
- Mission timeout (TTL)
- Auto-stop on signal loss

---

## 2. Safety Layer (Always Active)

- ESTOP latch (requires ARM to resume)
- Wi-Fi watchdog (timeout → STOP)
- Collision gate (distance < threshold → STOP)
- Low battery gate (below threshold → mode downgrade or STOP)
- Motor stall detection (retry then STOP)

Safety layer overrides mission layer.

---

## 3. HTTP Endpoints (Mandatory)

GET /status  
GET /log  

POST /cmd  
POST /mode  
POST /estop  
POST /arm  

All responses must be JSON.

---

## 4. Status Schema

```json
{
  "node": "ROVER-XXXX",
  "mode": "E|S|R",
  "armed": true,
  "estop": false,
  "battery": 0.0,
  "wifi_rssi": 0,
  "distance_front": 0,
  "uptime_s": 0,
  "faults": []
}


---

5. Logging Principles

Append-only in memory (ring buffer)

Exportable via /log

Timestamped (ISO 8601)

Severity levels: INFO, WARN, ERROR



---

6. Control Philosophy

Deterministic motion

No aggressive pursuit behaviors

Stop-first logic

Network loss = safe halt


Status: LAB SPECIFICATION

---

