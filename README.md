# HBCE Rover Control

Ground-control console for Wi-Fi rover units used in **exploration**, **security**, and **rescue** scenarios.

This repository provides:
- deterministic remote control (manual CLI)
- real-time telemetry polling
- safety control primitives (ARM / ESTOP)
- append-only operational logging (console-side)

Hardware target: rover nodes based on **Raspberry Pi Pico W** (or similar embedded controllers) exposing a local HTTP API.

---

## Quickstart

### Requirements
- Python 3.10+
- `requests`

Install:
```bash
pip install requests

Configure rover URL

Edit config.py:

ROVER_URL (example: http://192.168.1.50)

POLL_INTERVAL_S

log paths



---

Run

Interactive control (CLI)

python cli.py

Key commands:

w/a/s/d movement

q/e strafe

z/c rotate

x stop

1/2/3 set mode E/S/R

! ESTOP ON

@ ESTOP OFF

r ARM

t status

l log

p polling loop


Telemetry daemon (append-only log)

python main.py

Console-side logs are written to:

log/console_events.log



---

Expected Rover HTTP API (contract)

Status

GET /status → JSON object

{
  "node": "ROVER-0001",
  "mode": "E",
  "armed": true,
  "estop": false,
  "battery": 7.2,
  "wifi_rssi": -62,
  "distance_front": 34,
  "uptime_s": 128,
  "faults": []
}

Commands

POST /cmd

{"move":"FORWARD","v":0.2,"ms":300}

POST /mode

{"mode":"E"}

POST /estop

{"on":true}

POST /arm

{"token":"lab"}

Log

GET /log → list of events (implementation-defined)


---

Principles

fail-safe first

remote stop priority

deterministic movement

append-only logging

low-latency local network operation


Status: LAB INIT

