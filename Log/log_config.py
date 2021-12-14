from configparser import ConfigParser


class HandleConfig(ConfigParser):
    def __init__(self,file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")

conf = HandleConfig(file_path)

