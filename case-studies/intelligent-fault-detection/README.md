# Intelligent Fault Detection System

## Problem

Electrical systems often fail without warning due to:
- Hidden degradation
- Noise in sensor data
- Lack of predictive insight

Traditional diagnostics rely on reactive detection.

---

## Constraints

- Incomplete sensor data
- Noisy signals
- Cost limitations on hardware upgrades

---

## Approach

Designed a system combining:
- Signal anomaly detection
- Statistical deviation modeling
- Lightweight ML inference

---

## Key Insight

Instead of detecting failure, detect **deviation from normal system behavior**.

---

## Trade-offs

| Factor        | Decision |
|--------------|--------|
| Accuracy     | Moderate (to reduce compute cost) |
| Cost         | Low |
| Complexity   | Controlled |
| Reliability  | High (early detection) |

---

## Outcome

- Early-stage fault detection capability
- Reduced downtime risk
- Scalable across systems

---

## Files

- `simulation.py` → fault detection model
- `system_design.md` → architecture
- `tradeoff_analysis.md` → engineering reasoning
