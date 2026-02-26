# HBCE Rover Control — Development Roadmap

Status: LAB INIT

This roadmap defines the evolution of the rover control system from simulator stage to real-world operational unit.

---

## Phase 1 — Ground Control Core (ACTIVE)

- Console CLI control
- Telemetry daemon
- Append-only logging
- Rover simulator
- Protocol specification
- Testing checklist
- System architecture

Goal:
Stable ground-control infrastructure ready before hardware arrival.

---

## Phase 2 — Real Rover Connection (NEXT)

When hardware arrives:

- Flash Pico W firmware
- Connect rover to Wi-Fi
- Expose HTTP endpoints
- Link console to real rover
- Validate safety layer
- Validate ESTOP + ARM
- Run full testing checklist

Goal:
Real rover fully controlled by HBCE console.

---

## Phase 3 — Autonomous Behaviors

- Exploration mode stable
- Security patrol logic
- Rescue assist mode
- Obstacle avoidance tuning
- Movement precision tuning
- Mission logging

Goal:
Reliable indoor operational rover.

---

## Phase 4 — Advanced Systems

- Multi-rover control
- Camera integration
- Sensor fusion
- Remote secure access
- Persistent mission logs
- Industrial presentation readiness

Goal:
Professional robotic unit for exploration, security and rescue demonstration.

---

## Phase 5 — HBCE Robotics Layer

- Identity-bound rover nodes
- Operator control structure
- Fleet management
- EU compliance structure
- Industrial deployment model

Goal:
Operational robotic infrastructure aligned with HBCE systems.

---

Development philosophy:
Slow is smooth.  
Smooth becomes deterministic.  
Deterministic becomes operational.
