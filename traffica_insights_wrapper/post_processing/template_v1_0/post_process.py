import os
import sys
import logging
import argparse

from services.source_file_mapper import get_source_files
from services.config_parser import get_config
from services.datasource_handler import DatasourceHandler

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(
            os.path.dirname(os.path.realpath(__file__)) + "/output.log",
            mode="a",
            encoding="utf-8",
        ),
        logging.StreamHandler(sys.stdout),
    ],
)

parser = argparse.ArgumentParser(
    description="Post process Ingenier@'s Traffica Insights wrapper tool data."
)
parser.add_argument("-config", help="Optional config file")

args = parser.parse_args()
config = get_config(os.getcwd() + "\\" + (args.config or "default_settings.cfg"))

source_files = get_source_files()

if len(source_files) == 0:
    sys.exit()

for file in source_files:
    handler = DatasourceHandler(file, config)
