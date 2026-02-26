# ============================================
# HBCE ROVER CONTROL — CONFIG
# ============================================

# Rover base URL (will be set once the Pico W is online)
ROVER_URL = "http://192.168.1.50"

# Telemetry polling interval (seconds)
POLL_INTERVAL_S = 2.0

# HTTP timeout (seconds)
HTTP_TIMEOUT_S = 3.0

# Logging
LOG_DIR = "log"
LOG_FILE = "log/console_events.log"

# Node identity (local console side)
CONSOLE_ID = "HBCE-CONSOLE-0001"
