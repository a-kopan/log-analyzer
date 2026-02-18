from logLevel import LogLevel 
from datetime import datetime

class Log():
    def __init__(
        self, 
        level: LogLevel = LogLevel.DEBUG, 
        time: datetime = datetime.now(),
        message: str = "default message" 
        ):
        self.level = level
        self.time = time
        self.message = message
        
    def __str__(self):
        return f"[{self.time.strftime("%H:%M:%S")}] | {self.level} | {self.message}"
    
    