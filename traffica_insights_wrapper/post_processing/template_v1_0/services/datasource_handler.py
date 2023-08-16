import os.path
import zipfile
import pandas as pd
import logging
from .utils.log_utils import print_header, print_divider, print_df_preview


class DatasourceHandler:
    df: pd.DataFrame
    config: dict

    def __init__(self, source_file_path: str, config: dict):

        print_header(f"Processing source file: {os.path.basename(source_file_path)}...")
        self.config = config

        source_file_path = source_file_path.lower()
        if source_file_path.endswith(".csv"):
            self.init_from_csv(source_file_path)
        elif source_file_path.endswith(".zip"):
            self.init_from_zip(source_file_path)
        else:
            raise f"Invalid file type: {source_file_path}"

        self.apply_pre_filters()

    def init_from_csv(self, source_file_path: str):
        # Using 'utf-8-sig' encoding to correctly parse the BOM
        # Source: https://github.com/pandas-dev/pandas/issues/4793
        self.df = pd.read_csv(source_file_path, sep=";", encoding="utf-8-sig")

    def init_from_zip(self, source_file_path: str):
        logging.info("--> Extracting...")
        logging.info("")
        # Using 'utf-8-sig' encoding to correctly parse the BOM
        # Source: https://github.com/pandas-dev/pandas/issues/4793
        self.df = pd.read_csv(
            source_file_path, sep=";", encoding="utf-8-sig", compression="zip"
        )

    def apply_pre_filters(self):

        pattern = "|".join(self.config["filter"]["techband_exclude"])
        self.df = self.df[self.df["TechBand"].str.match(pattern) == False]

        pattern = "|".join(self.config["filter"]["techband_include"])
        self.df = self.df[self.df["TechBand"].str.match(pattern) == True]

        print_df_preview(self.df)
