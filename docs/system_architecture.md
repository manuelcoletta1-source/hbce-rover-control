# HBCE Rover System Architecture — v0.1

Distributed ground-control architecture for exploration, security and rescue rover units.

---

## 1. Core Structure

Ground Console (PC)
↓ Wi-Fi local network
Rover Node (Pico W)

Control and intelligence remain external.
Execution remains onboard rover.

This separation ensures:
- deterministic control
- safety override priority
- scalable multi-rover operation

---

## 2. Ground Console

Components:
- CLI manual control
- telemetry daemon
- append-only logging
- command interface
- safety commands (ESTOP / ARM)

Responsibilities:
- mission control
- audit logging
- operator interface
- multi-unit future coordination

---

## 3. Rover Node

Embedded controller:
- Raspberry Pi Pico W

Responsibilities:
- execute movement
- read sensors
- enforce safety layer
- expose HTTP API
- maintain local log buffer

The rover never acts outside safety rules.

---

## 4. Safety Architecture

Always active:
- ESTOP latch
- watchdog (signal loss)
- collision gate
- speed limits
- low battery protection

Safety layer overrides all commands.

---

## 5. Operational Modes

E — Exploration  
S — Security  
R — Rescue  

Each mode adjusts:
- speed
- behavior
- logging priority
- safety thresholds

---

## 6. Logging Philosophy

Append-only.
Deterministic.
Timestamped.
Auditable.

Console log = permanent record  
Rover log = rolling buffer

---

## 7. Future Expansion

- multi rover control
- autonomous patrol logic
- sensor fusion
- camera integration
- EU robotics compliance layer

Status: LAB ARCHITECTURE ACTIVE
