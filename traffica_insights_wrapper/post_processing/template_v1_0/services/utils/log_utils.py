import math
import os
import logging
import pandas as pd


LINE_WIDTH = os.get_terminal_size()[0] - 30

LOG_DIVIDERS = [
    "=" * LINE_WIDTH,
    "-" * LINE_WIDTH,
]


def print_divider(index=0):
    logging.info(LOG_DIVIDERS[index])


def print_header(text: str, index=0):
    text_parts = wrap_text(text)
    if index == 0:
        logging.info("")
        logging.info("")
        logging.info("")
        print_divider(0)
        [logging.info(p) for p in text_parts]
        print_divider(0)
        logging.info("")


def wrap_text(text: str, width=LINE_WIDTH) -> list[str]:
    result = []
    parts = math.ceil(len(text) / LINE_WIDTH)
    for p in range(0, parts):
        result.append(text[p * width : (p + 1) * width])
    return result


def print_df_preview(df: pd.DataFrame):

    lines = df.to_string(max_rows=10, line_width=LINE_WIDTH, max_cols=10).splitlines()
    print_divider(1)
    [logging.info(line) for line in lines]
    logging.info("")
    logging.info(f"[{df.shape[0]} rows x {df.shape[1]} columns]")
    print_divider(1)
