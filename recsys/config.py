import os
import json
from configparser import ConfigParser
from pathlib import Path


class Config:
    """
    Config Class wrapping the reading of config values from public and private files
    """
    CONFIG_FILES_TO_READ = [
        "../configs/config.ini",  # public file, entered into git
    ]

    def __init__(self):
        parser = ConfigParser()
        parser.read([self.get_absolute_path_from_config(x) for x in self.CONFIG_FILES_TO_READ])

        self.root_location = self.get_absolute_path_from_config(parser["data"]["root_location"])
        self.data_path = self.get_absolute_path_from_config(parser["data"]["data_path"])

    @staticmethod
    def get_absolute_path_from_config(string_relative_path: str) -> Path:
        return Config.get_absolute_path_from_origin(__file__, string_relative_path)

    @staticmethod
    def get_absolute_path_from_origin(origin: str, string_path: str) -> Path:
        """
        Convert relative paths to absolute paths relative to the given origin
        :param origin: path to start resolving relative paths from
        :param string_path:
        :return:
        """
        path = Path(string_path)
        if path.is_absolute():
            return path
        else:
            return Path(Path(origin).parent.resolve(), Path(string_path)).resolve()
