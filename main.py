# main.py
import os
import sys


# Add the project root directory to Python's module search path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)


import pandas as pd
from config import PLATFORMS, KEYWORD
from datetime import datetime
from utils.logging_setup import setup_logging
from utils.file_operations import create_work_directory
from utils.user_input import get_user_input
from data_processing.downloader import download_files
from data_processing.zip_processor import process_zip_files


def main():
    # Create work directory
    work_dir = create_work_directory()

    # Change current working directory
    os.chdir(work_dir)

    # Set up logging in the new work directory
    logger = setup_logging(work_dir)

    user_choice, parameters = get_user_input()

    final_data = pd.DataFrame()

    if user_choice == 'local':
        logger.info("Processing ZIP files from local folder.")
        print("Starting processing of local ZIP files...")
        folder_path = parameters['path']
        for zip_file in os.listdir(folder_path):
            if zip_file.endswith('.zip'):
                for df in process_zip_files(os.path.join(folder_path, zip_file), logger):
                    final_data = pd.concat([final_data, df], ignore_index=True)
    elif user_choice == 'download':
        logger.info("Downloading and processing files based on the provided date range.")
        print("Starting download and processing...")
        for zip_path in download_files(parameters['start_date'], parameters['end_date'], logger):
            for df in process_zip_files(zip_path, logger):
                final_data = pd.concat([final_data, df], ignore_index=True)

    # Save final consolidated CSV
    output_csv = f"filtered_misinformation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    final_data.to_csv(output_csv, index=False)
    logger.info(f"Final filtered data saved to {output_csv}")
    print(f"Final filtered data saved to {output_csv}")


if __name__ == "__main__":
    main()