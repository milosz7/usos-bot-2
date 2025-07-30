import logging
import os
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), "../../out/logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Generate a timestamped log filename (e.g., logs/run_2025-07-30_14-52-01.log)
log_filename = f"run_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_file_path = os.path.join(LOG_DIR, log_filename)

logger = logging.getLogger("project_logger")
logger.setLevel(logging.INFO)

if not logger.hasHandlers():
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # Optional: also log to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
