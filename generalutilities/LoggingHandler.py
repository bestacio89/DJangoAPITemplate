# broader_utils/logging_utils.py

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

def log_info(message):
    """
    Logs an informational message.

    Args:
    - message (str): Message to log.
    """
    logging.info(message)

def log_warning(message):
    """
    Logs a warning message.

    Args:
    - message (str): Warning message to log.
    """
    logging.warning(message)

def log_error(message):
    """
    Logs an error message.

    Args:
    - message (str): Error message to log.
    """
    logging.error(message)

def log_debug(message):
    """
    Logs a debug message.

    Args:
    - message (str): Debug message to log.
    """
    logging.debug(message)
