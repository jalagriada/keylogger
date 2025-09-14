# 🛡️ Advanced Keylogger Toolkit (For Educational Use Only)

A Python-based keylogger detection, execution, and decoding toolkit designed **for educational and ethical purposes only**. This project includes:

- ✅ `keylogger.py` — Logs all keystrokes (non-root)
- ✅ `detector.py` — Detects and terminates keylogger processes
- ✅ `decoder.py` — Decodes `keystrokes.log` to readable text

---

## 📚 Guide to Execute

### 1. Create a Virtual Environment *(optional but recommended)*

```bash
python3 -m venv keylogger_venv
```

> ⚠️ If you see this error:

```
source: no such file or directory: keylogger_venv/bin/activate
```

> Just run the command above to create the virtual environment first.

---

### 2. Activate the Virtual Environment

```bash
source keylogger_venv/bin/activate
```

You should now see something like this in your terminal:

```
(keylogger_venv) ─(finn㉿kali)-[~/Desktop/keylogger]
```

> ✅ **Make sure you are inside the virtual environment**. Otherwise, the program might not run properly.

---

### 3. Install Required Python Libraries

```bash
pip install -r requirements.txt
```

✅ Example of successful installation:

```
Successfully installed psutil notify2 pynput evdev python-xlib six
```

---

### 4. Run the Programs

#### 🔎 Start the Detector

```bash
python detector.py
```

#### 📝 Start the Keylogger

```bash
python keylogger.py
```

#### 🔓 Decode the Logs (Optional)

```bash
python decoder.py
```

This will read `keystrokes.log` and print the decoded keystrokes in a clean, human-readable format.

---

## 📁 Example File Structure

After running `ls`, you should see something like this:

```
decoder.py
det.py
detector.py
keylogger.py
key.py
keylogger_venv/
requirements.txt
'guide to execute.txt'
keystrokes.log
```

---

## 🧾 `requirements.txt` Contents

Here are the Python libraries required:

```
psutil>=5.9.0
notify2>=0.3.1
pynput>=1.7.6
```

You can also install them manually with:

```bash
pip install psutil notify2 pynput
```

---

## ⚠️ Disclaimer

> **THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY.**  
> Any illegal activities or misuse of this program are strictly prohibited.  
> Users are solely responsible for ensuring compliance with all local laws and regulations.  
> The creators or contributors of this tool **disclaim all liability** for any damage, loss, or legal issues resulting from the misuse of this software.  
> **Use responsibly and ethically.**

---

## 👨‍💻 Developed By

- 🎓 BSIT 3H Students  
- 🏫 Camarines Sur Polytechnic Colleges  
- 📍 Nabua, Camarines Sur

---

## ✅ Done and Enjoy Learning!

If you encounter any issues, recheck your virtual environment and dependencies. Always code ethically and responsibly. Happy coding! 💻🧠
