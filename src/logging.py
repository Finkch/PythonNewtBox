# Used to log

from datetime import datetime
import os

import logging

LOG_DIR     = 'logs'
MAX_LOGS    = 5

# A filter to only allow NewtBox log requests through
class NewtBoxFilter(logging.Filter):
    def filter(self, record):
        return record.name.startswith('src')


# Logging configuration
def logs_setup(stream_level = logging.ERROR, file_level = logging.DEBUG) -> None:

    # Creates the logging file for this execution
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(LOG_DIR, f"roguer_{timestamp}.log")


    # Use a not-very-verbose format for console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s]:  %(message)s'))
    stream_handler.setLevel(stream_level)
    stream_handler.addFilter(NewtBoxFilter())
    

    # Verbose logging for files
    file_handler = logging.FileHandler(log_file, mode = 'w')
    file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s @ %(module)s:%(lineno)d:  %(message)s'))
    file_handler.setLevel(file_level)
    file_handler.addFilter(NewtBoxFilter())


    # Sets up the logger
    logging.basicConfig(
        level       = min(stream_level, file_level),
        handlers    = [stream_handler, file_handler]
    )


    # Removes any old logs
    logs_cleanup()


# Gets rid of old logs
def logs_cleanup() -> None:
    
    # Gets the logs sorted by modification data
    logs = sorted(
        (file for file in os.listdir(LOG_DIR) if file.endswith('.log')),
        key = lambda x: os.path.getmtime(os.path.join(LOG_DIR, x)),
        reverse = True
    )

    # Removes any logs beyond the most recent MAX_LOG amount
    for old in logs[MAX_LOGS:]:
        os.remove(os.path.join(LOG_DIR, old))
