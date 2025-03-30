import datetime

class Logger:
    def __init__(self, log_file="logs.txt"):
        self.log_file = log_file

    def log_info(self, message):
        """Logs an info message with a timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] INFO: {message}"
        print(log_entry)  # Also print to console
        with open(self.log_file, "a") as file:
            file.write(log_entry + "\n")

# Global logger instance
logger = Logger()

def log_info(message):
    logger.log_info(message)
