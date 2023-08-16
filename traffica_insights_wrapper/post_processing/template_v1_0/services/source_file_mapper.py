import os
import logging


def get_source_files() -> list[str]:
    data_folder = os.getcwd() + "\\data"

    file_list = os.listdir(data_folder)

    csv_files = [
        data_folder + "\\" + f
        for f in list(filter(lambda r: r.lower().endswith(".csv"), file_list))
    ]
    zip_files = [
        data_folder + "\\" + f
        for f in list(filter(lambda r: r.lower().endswith(".zip"), file_list))
    ]
    source_files = csv_files + zip_files

    if len(source_files) == 0:
        logging.info("No source files found in 'data' folder.")

    else:
        logging.info(f"Source files found [{len(source_files)}]: ")
        [logging.info(f"--> [CSV] {os.path.basename(f)}") for f in csv_files]
        [logging.info(f"--> [ZIP] {os.path.basename(f)}") for f in zip_files]

    return source_files
