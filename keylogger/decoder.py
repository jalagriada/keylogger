#!/usr/bin/env python3
# decoder.py - Decode keystroke logs into clean text (handles backspace & errors)

def decode_log(file_path):
    output = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            try:
                # Split log line (handle different log formats)
                parts = line.split(" - ", 1)
                if len(parts) < 2:
                    continue
                
                char = parts[1].strip()

                # Special handling
                if char == "[space]":
                    output.append(" ")
                elif char == "[enter]":
                    output.append("\n")
                elif char == "[backspace]":
                    if output:
                        output.pop()  # remove last character
                elif char.startswith("[") and char.endswith("]"):
                    # Skip other special keys like [shift], [ctrl], etc.
                    continue
                else:
                    # Normal character - remove any extra quotes or spaces
                    clean_char = char.strip('"\' ')
                    if clean_char:
                        output.append(clean_char)
            except (ValueError, IndexError):
                continue  # skip malformed lines

    return "".join(output)

def clean_text(text):
    """Additional cleaning to handle any remaining artifacts"""
    # Remove any stray brackets or special markers that might have been missed
    import re
    text = re.sub(r'\[.*?\]', '', text)  # Remove any remaining [something] patterns
    text = re.sub(r'\s+', ' ', text)  # Normalize multiple spaces
    text = text.strip()
    return text

if __name__ == "__main__":
    log_file = "keystrokes.log"   # pangalan ng log file mo
    decoded_text = decode_log(log_file)
    clean_output = clean_text(decoded_text)
    print(clean_output)
