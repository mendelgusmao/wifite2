import json

from ..config import Configuration


class CrackedFile:
    @staticmethod
    def load_cracked_file(cls):
        if cls.networks:
            return

        try:
            cls.networks = json.load(open(Configuration.cracked_file, "r"))
            cls.bssids = set([network["bssid"] for network in cls.networks])
        except Exception:
            cls.networks = []
            cls.bssids = set()
            pass

    @staticmethod
    def is_cracked(cls, bssid):
        cls.load_cracked_file()

        return bssid in cls.bssids
