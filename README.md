# ⚙️ Raspberry Pi Pico W – Servo Motor Sweep (PWM Control)

This project demonstrates how to control a **servo motor** using **PWM (Pulse Width Modulation)** on the **Raspberry Pi Pico W**.  
The servo smoothly sweeps from -90° → +90° → -90° repeatedly.

---

## 🧠 Working Principle
Servo motors respond to the **width** of a pulse within a 20 ms signal frame.

| Position | Pulse Width | Approx. Duty (16-bit) |
|-----------|-------------|------------------------|
| -90° | 1.0 ms | ≈1639 |
| 0° | 1.5 ms | ≈4915 |
| +90° | 2.0 ms | ≈8192 |

PWM frequency is fixed at **50 Hz (20 ms period)**.  
By changing the “on-time” of the pulse, we control the servo angle.

---

## 🧩 Components Required

| Component | Quantity | Description |
|------------|-----------|-------------|
| Raspberry Pi Pico W | 1 | Microcontroller board |
| Servo Motor (e.g. SG90 / MG90S) | 1 | 180° servo |
| Jumper Wires | — | For connections |
| External 5V Supply (recommended) | 1 | Powers servo safely |

---

## ⚙️ Circuit Connections

| Servo Pin | Pico W Pin | Description |
|------------|-------------|-------------|
| VCC (Red) | 5V (VBUS) | Power |
| GND (Brown/Black) | GND | Ground |
| Signal (Orange/Yellow) | GPIO16 | PWM Signal |

⚠️ **Tip:** If the servo jitters, power it from an external 5 V source and connect grounds together.

---
