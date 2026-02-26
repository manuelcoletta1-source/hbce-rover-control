# Run HBCE Rover Control locally

This repository is developed on GitHub.  
To execute locally you only need Python 3.

---

## 1) Install dependencies

```bash
pip install -r requirements.txt


---

2) Run rover simulator (optional)

python sim_rover.py

Simulator will listen on:

http://127.0.0.1:5000

Make sure in config.py:

ROVER_URL = "http://127.0.0.1:5000"


---

3) Run CLI (manual control)

python cli.py


---

4) Run telemetry daemon (append-only log)

python main.py

Logs are written to:

log/console_events.log

---
