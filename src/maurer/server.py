"""Hot reload server for Maurer."""

import os
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Callable


# https://stackoverflow.com/a/182259/12696223
class Monkey(object):
    def __init__(self, path: str, fn: Callable):
        self._cached_stamp = 0
        self.filename = path
        self.fn = fn

    def watch(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            print("File changed")
            self._cached_stamp = stamp
            self.fn()

    def check_multi_files(self, files: list):
        raise NotImplementedError()

    def start(self, interval: float = 1.0):
        while True:
            self.watch()
            time.sleep(interval)


def run_server(directory: str, fn: Callable, interval: float = 1.0):
    monkey = Monkey(directory, fn)
    monkey.start()
