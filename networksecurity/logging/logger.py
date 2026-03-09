import datetime
import logging
import os

Logfile = f"{datetime.datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "Logs", Logfile)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, Logfile)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
