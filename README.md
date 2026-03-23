# 🟡 2.5D Pac-Man Clone (Ursina Engine)

A simple but functional Pac-Man-style game built using **Python + Ursina**.
It recreates the classic arcade feel with a top-down view, maze navigation, collectible dots, and chasing ghosts.

---

## 🎮 Features

* 🟡 Smooth Pac-Man movement
* 🧱 Grid-based maze with proper wall collision
* ⚪ Collectible dots with score tracking
* 👻 3 ghosts that actively chase the player
* 🚪 Side tunnels (teleport from left ↔ right)
* 🧠 Basic ghost AI (directional chasing like classic Pac-Man)
* 🎥 True top-down camera

---

## 🕹️ Controls

| Key | Action     |
| --- | ---------- |
| W   | Move Up    |
| S   | Move Down  |
| A   | Move Left  |
| D   | Move Right |

---

## 🚀 Installation

Make sure you have Python 3.12+ installed.
Activate Virtual Environment:
For macOS/Linux/Unix systems:
```bash
python3 -m venv venv && source venv/bin/activate
```
For Windows
```bash
python -m venv venv
```
in Powershell:
```bash
.\venv\Scripts\Activate.ps1
```
in CMD:
```bash
venv\Scripts\activate.bat
```

Install dependencies:

```bash
pip install ursina
```

---

## ▶️ Run the Game

in Windows
```bash
python app.py
```
in macOS/Linux/Unix systems:
```bash
python3 app.py
```

---

## 🧠 How It Works

* The maze is defined as a **2D grid** (1 = wall, 0 = path)
* Player and ghosts move within this grid
* Collision is handled by checking grid positions
* Ghosts use a simple AI:

  * Move toward the player based on axis distance
  * Avoid walls and each other
  * Fallback to random movement if blocked

---

## 🎯 Objective

* Collect all dots 🟡
* Avoid ghosts 👻
* Survive as long as possible

---

## ⚠️ Known Limitations

* Ghost AI is basic (no personalities yet)
* No power pellets or “scared mode”
* Movement is smooth but not fully arcade-perfect

---

## 🔥 Future Improvements

* Power pellets (ghosts turn blue)
* Multiple ghost behaviors (Blinky, Pinky, etc.)
* Sound effects (“waka waka”)
* More accurate original Pac-Man map
* Score saving system

---

## 🧑‍💻 Author Notes

This project focuses on:

* Keeping code understandable
* Balancing simplicity with gameplay feel
* Gradually improving toward a full Pac-Man clone

---
