# DSA Transparency Database Analyzer

This project is designed to download, process, and analyze data from the Digital Services Act (DSA) Transparency Database. It allows users to filter and compile data related to misinformation across various social media platforms.

## Features

- Download ZIP files from the DSA Transparency Database for a specified date range
- Process local ZIP files containing nested ZIP and CSV data
- Filter data based on specified platforms and keywords
- Compile filtered data into a single CSV file for further analysis

## Requirements

- Python 3.7+
- pandas
- requests

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/dsa-transparency-analyzer.git
   cd dsa-transparency-analyzer
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script from the command line:

```
python main.py
```

Follow the prompts to either process local ZIP files or download and process new files.

## Project Structure

```
project_root/
│
├── main.py
├── config.py
├── utils/
│   ├── __init__.py
│   ├── logging_setup.py
│   ├── file_operations.py
│   └── user_input.py
├── data_processing/
│   ├── __init__.py
│   ├── downloader.py
│   ├── zip_processor.py
│   └── csv_processor.py
├── requirements.txt
└── README.md
```

## Configuration

Edit the `config.py` file to modify:
- `BASE_URL`: The base URL for downloading ZIP files
- `PLATFORMS`: The list of platforms to include in the analysis
- `KEYWORD`: The keyword to filter the data (default is "misinformation")

## Output

The script will create a new directory for each run, containing:
- A log file with processing information
- A CSV file with the filtered and compiled data

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Gen AI

This project has been developed using Chat-GPT 4, Chat-GPT 4o and Claude 3.5. 
