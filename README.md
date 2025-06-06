# Disclaimer
The author is not responsible for any misuse of this software. Use it at your own risk and ensure compliance with all applicable laws and regulations.

# Ethical Considerations
Use Responsibly: This software is for educational and testing purposes only. Using a keylogger to monitor someone without their explicit consent is illegal in many jurisdictions and violates privacy rights.

Transparency: Always inform and obtain consent from users before deploying this software on their systems.

Security: The ZIP file is encrypted, but ensure the password and output files are handled securely to prevent unauthorized access.

# keycap
This app could capture all the keyboard keystrokes into a file, if a secret key phrase input, the capture will be stopped.
# Keylogger

**Author**: KPFZIPOH
**License**: MIT License  
**Repository**: [Your GitHub Repository URL]  

## Description

This is a Python-based keylogger that captures keystrokes, saves them to a file (`keys.txt`), and archives the file into a password-protected ZIP archive when a predefined stop code (`999123123999`) is detected. The program uses the `pynput` library for keyboard input monitoring and `pyzipper` for creating encrypted ZIP files. It includes logging for debugging and monitoring, with a separate thread to check for the stop code in the output file.

**Note**: This project is intended for **educational purposes only**. Unauthorized use of keyloggers to capture keystrokes without consent is **illegal** and **unethical**. Ensure you have explicit permission from all parties involved before using this software.

## Features

- Captures all keystrokes, including special keys (e.g., Enter, Backspace, Ctrl).
- Saves keystrokes to `keys.txt` with start and stop timestamps.
- Archives the output file into a password-protected ZIP file using AES encryption.
- Stops execution when the stop code `999123123999` is typed.
- Logs program activity and errors to `keylogger.log` for debugging.
- Configurable parameters (e.g., output file name, stop code, ZIP password) via a configuration dictionary.
- Multi-threaded design for keyboard listening and file monitoring.

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - `pynput` (for keyboard input monitoring)
  - `pyzipper` (for creating encrypted ZIP files)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone [Your GitHub Repository URL]
   cd keylogger
