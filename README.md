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
