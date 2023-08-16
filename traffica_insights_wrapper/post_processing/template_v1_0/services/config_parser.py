import json
import configparser

config = configparser.ConfigParser()


def get_config(filename: str | None):
    result = {"filter": {"techband_include": [], "techband_exclude": [],}}
    if filename is not None:
        config.read(filename)
        result["filter"]["techband_include"] = json.loads(
            config["filter"]["techband_include"] or "[]"
        )
        result["filter"]["techband_exclude"] = json.loads(
            config["filter"]["techband_exclude"] or "[]"
        )
    return result
