import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # this is iam going ti print which it displays the date and time where ever we used this logger function in the file modules

log_path=os.path.join(os.getcwd(),"logs") # combining the path of current working directory and creating a logs file and combined it wil cwd

os.makedirs(log_path,exist_ok=True)  # for creating log folder iam passing it here makdirs


LOG_FILEPATH=os.path.join(log_path,LOG_FILE)


logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)