from logLevel import LogLevel
from log import Log
from datetime import datetime, timedelta
from collections import defaultdict
from random import choice, randint

class MockLogService():
    def __init__(self, level: LogLevel = LogLevel.DEBUG):
            self.log_levels = [l for l in list(LogLevel) if l>=level]
            self.logs = []
            
    def simulate(self, n_of_logs: int = 150):
        random_logs_per_level = defaultdict(list)
        
        #create random log messages per each level
        for _ in range(int(n_of_logs/(len(self.log_levels)*3))):
            random_logs_per_level[choice(self.log_levels)].append(f"log_message_{randint(10_000_000, 99_999_999)}")
        
        current_time = datetime.now()
        
        #create randomm logs
        for _ in range(n_of_logs):
            current_time = current_time + timedelta(milliseconds=500)
            log_level = choice(self.log_levels)
            self.logs.append(Log(log_level, current_time, choice(random_logs_per_level[log_level])))