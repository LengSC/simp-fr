# -*- coding: utf-8 -*-


from rich.console import Console


class Logger:
    LOG_LEVEL_INFO: str = 'info'
    LOG_LEVEL_DEBUG: str = 'debug'
    LOG_LEVEL_WARNING: str = 'warning'
    LOG_LEVEL_ERROR: str = 'error'

    def __init__(self) -> None:
        self.logger = Console()

    def log(self, log_level: str, log_message: str) -> None:
        if log_message is None:
            return

        if log_level == self.LOG_LEVEL_INFO:
            self.logger.log(f'[d bold]\[INFO][/] [d]{log_message}[/]')
        elif log_level == self.LOG_LEVEL_DEBUG:
            self.logger.log(f'[yellow bold]\[DEBUG][/] [yellow]{log_message}[/]')
        elif log_level == self.LOG_LEVEL_WARNING:
            self.logger.log(f'[red bold]\[WARN][/] [red]{log_message}[/]')
        elif log_level == self.LOG_LEVEL_ERROR:
            self.logger.log(f'[red bold on yellow]\[ERR!][/] [red on #191981]{log_message}[/]')
