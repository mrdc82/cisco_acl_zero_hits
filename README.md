# Firewall Hit Count Analyzer

## Overview
This project contains two Python scripts for analyzing firewall rule hit counts and extracting rules with zero hit counts. The scripts utilize `tkinter`, `glob`, and `os` for user interaction and file handling.

## Features
- **`hitcounts.py`**: Iterates through a folder containing multiple files with firewall rules and their hit counts. It extracts and exports rules with zero hit counts.
- **`zero_counts.py`**: Allows the user to select a single file and extract rules with zero hit counts.

## Requirements
Ensure you have the following modules installed:
- `tkinter` (for GUI file selection)
- `glob` (for file searching)
- `os` (for file and directory operations)

## Installation
No special installation is required. Ensure you have Python installed along with the required modules.

## Usage
1. Run `hitcounts.py` to analyze multiple files in a selected folder.
   ```sh
   python hitcounts.py
   ```
2. Run `zero_counts.py` to analyze a single file.
   ```sh
   python zero_counts.py
   ```

## License
This project is licensed under the MIT License.

## Contribution
Feel free to fork this repository and submit pull requests with improvements or additional features.

## Author
Constantinos Charalambous

