import os 
import sys
import logging
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# %(asctime)s:Inserts the timestamp of when the log record was created.
# %(levelname)s:Inserts the log level (severity of the log message).ex-Debug, info ,Warning
# %(module)s:Inserts the name of the module where the logging call was made.
# The module is typically the name of the Python file (without the .py extension).
# %(message)s:Inserts the actual log message provided in the logging call.
# Example: The text you pass in logging.info("This is a log message").


log_dir="logs"
log_filepath=os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)
# log_dir = "logs":Specifies the directory where the log file will be stored. In this case, it is a folder named "logs".
# log_filepath = os.path.join(log_dir, "logging.log"):Constructs the full file path to the log file.
# The os.path.join() ensures that the directory and file name are combined correctly, regardless of the operating system (e.g., Windows uses \ while Linux/Mac uses /).
# os.makedirs(log_dir, exist_ok=True):Ensures that the "logs" directory is created if it doesn’t already exist.
# exist_ok=True prevents an error if the directory already exists.



logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]

)

# level=logging.INFO:Sets the logging level to INFO. Messages at INFO level or higher (WARNING, ERROR, CRITICAL) will be logged, but DEBUG messages will be ignored.
# format:Defines the format for the log messages.logging_str is the above format which we have created

# handlers=[...]:Defines the destinations for the log messages. In this case, two handlers are used:
# logging.FileHandler(log_filepath):Sends log messages to the specified file (logging.log in the "logs" directory).
# Each log message is appended to the file.
# logging.StreamHandler(sys.stdout):Sends log messages to the console (standard output) so you can see them in real-time during execution.

logger=logging.getLogger("datasciencelogger")

# logging.getLogger(name):
# Retrieves or creates a logger instance with the specified name.
# If a logger with the same name already exists, it will return the existing instance.
# If it doesn’t exist, a new logger is created with the given name.