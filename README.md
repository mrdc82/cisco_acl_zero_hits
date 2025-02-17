# Firewall Rule Hit Count Analyzer

This repository contains two Python scripts designed to analyze firewall rule hit counts and extract rules with zero hits. The scripts are useful for cleaning up unused firewall rules or identifying rules that are not being utilized.

## Scripts

### 1. `hitcounts.py`
This script iterates through a folder containing multiple files with firewall rules and their hit counts. It identifies and exports rules with zero hit counts to a new file.

### 2. `zero_counts.py`
This script allows you to select a single file to analyze and extract rules with zero hit counts. It provides a user-friendly interface for selecting the file and saving the results.

## Requirements

To run these scripts, you need the following Python modules installed:

- `tkinter` (for GUI file selection in `zero_counts.py`)
- `glob` (for file pattern matching)
- `os` (for file and directory operations)

You can install these modules using `pip` if they are not already installed:

```bash
pip install tkinter

Usage
hitcounts.py
Place all your firewall rule files in a single folder.

Run the script:

bash
Copy
python hitcounts.py
The script will process all files in the folder and generate a new file (zero_hit_rules.txt) containing rules with zero hit counts.

zero_counts.py
Run the script:

bash
Copy
python zero_counts.py
A file dialog will open, allowing you to select a single firewall rule file.

The script will extract rules with zero hit counts and save them to a new file (zero_hit_rules_selected.txt).

Output
hitcounts.py generates a file named zero_hit_rules.txt in the same directory as the script.

zero_counts.py generates a file named zero_hit_rules_selected.txt in the same directory as the script.

Example
Input File (firewall_rules.txt)
Copy
Rule 1: Allow HTTP, Hits: 10
Rule 2: Allow HTTPS, Hits: 0
Rule 3: Block FTP, Hits: 5
Rule 4: Allow SSH, Hits: 0
Output File (zero_hit_rules.txt or zero_hit_rules_selected.txt)
Copy
Rule 2: Allow HTTPS, Hits: 0
Rule 4: Allow SSH, Hits: 0
Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure your code follows the existing style and includes appropriate documentation.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize this README to better suit your project!

Copy

### Notes:
1. Replace `[LICENSE]` with the actual license file if you include one.
2. Update the example input/output files if they differ from your actual use case.
3. Add any additional dependencies or instructions specific to your environment.
