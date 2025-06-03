# This is an optional script to autologin MT5 on Windows
import subprocess
import time

# Replace this with your actual terminal path
terminal_path = "C:\Program Files\MetaTrader 5\terminal64.exe"

# Optional: login details can be passed if needed
subprocess.Popen([terminal_path])
time.sleep(5)
print("MT5 Terminal launched.")
