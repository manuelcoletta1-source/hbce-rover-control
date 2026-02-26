# HBCE Rover — Testing Checklist v0.1

Use this checklist to validate rover behavior before real missions.

All tests must PASS.

---

## 1. Connection

[ ] Rover reachable via browser (IP responds)  
[ ] /status returns valid JSON  
[ ] Telemetry daemon receives data  
[ ] CLI connects without error  

PASS = stable for 60s without disconnect

---

## 2. Basic Movement

[ ] Forward command executes  
[ ] Stop command immediate  
[ ] Left/right movement correct  
[ ] Rotation correct  
[ ] No random movement  

PASS = deterministic response

---

## 3. Modes

[ ] Mode E sets correctly  
[ ] Mode S sets correctly  
[ ] Mode R sets correctly  
[ ] Mode change logged  

PASS = mode visible in /status and log

---

## 4. Safety Layer

[ ] ESTOP stops all motion immediately  
[ ] Movement blocked while ESTOP active  
[ ] ARM restores control  
[ ] Wi-Fi loss → rover stops (test later)  

PASS = fail-safe always wins

---

## 5. Logging

[ ] Movement events logged  
[ ] Mode changes logged  
[ ] ESTOP logged  
[ ] No log corruption  

PASS = append-only consistent

---

## 6. Mission Simulation

Exploration:
[ ] Move + avoid obstacle (sim)  
[ ] No collision behavior  

Security:
[ ] Patrol loop stable  
[ ] No random drift  

Rescue:
[ ] Slow controlled movement  
[ ] Manual override priority  

PASS = stable 5 minutes continuous

---

Status: LAB VALIDATION REQUIRED
