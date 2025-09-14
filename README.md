# 🛡️ Advanced Keylogger Toolkit (Educational Use Only)

A complete Python-based keylogger detection, logging, and decoding toolkit. This project was developed for **educational and ethical testing purposes only**. It includes:

- A keylogger (`keylogger_pynput.py`) that logs keystrokes without requiring root access.
- A powerful terminator (`advanced_terminator.py`) that detects and stops running keylogger scripts.
- A decoder (`decoder.py`) that converts raw keystroke logs into readable text, handling `[backspace]`, `[enter]`, etc.

---

## 📌 Project Details

- **Course:** Bachelor of Science in Information Technology  
- **Section:** BSIT 3H  
- **School:** Camarines Sur Polytechnic Colleges  
- **Location:** Nabua, Camarines Sur  
- **Purpose:** Educational / Ethical Hacking Demo / Python Scripting Practice

---

## ⚙️ Features

✅ Keylogger without root access  
✅ Real-time detection and termination of suspicious `key.py` processes  
✅ System info gathering of detected processes  
✅ Auto mode and manual control for process termination  
✅ Decoder script to read log files as human-readable text  
✅ Virtual environment check for safety  

---

## 🧰 Tools Used

- Python 3  
- `psutil`  
- `pynput`  
- `platform`, `socket`, `subprocess` (standard libraries)  

---

## 🚀 Setup Instructions

### 1. 🔐 Set up a virtual environment (for keylogger safety)

```bash
python3 -m venv keylogger_venv
source keylogger_venv/bin/activate
pip install pynput
