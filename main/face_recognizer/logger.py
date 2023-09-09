# -*- coding: utf-8 -*-


from rich.console import Console

LOG_LEVEL_INFO: str = 'info'
LOG_LEVEL_DEBUG: str = 'debug'
LOG_LEVEL_WARNING: str = 'warning'
LOG_LEVEL_ERROR: str = 'error'


class Logger:
    def __init__(self) -> None:
        self.logger = Console()

    def log(self, log_level: str, log_message: str) -> None:
        if log_message is None:
            return

        if log_level == LOG_LEVEL_INFO:
            self.logger.log(r"[d]\[INFO][/] {log_message}")
        elif log_level == LOG_LEVEL_DEBUG:
            pass
        elif log_level == LOG_LEVEL_WARNING:
            pass
        elif log_level == LOG_LEVEL_ERROR:
            pass

    def destroy(self) -> None:
        pass
