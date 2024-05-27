# File Processor

## Overview
The File Processor is a Python script designed to read data from multiple `.dat` files in a specified input directory, process the data, and write the results to a CSV file in an output directory. The script ensures no duplicate data, calculates the gross salary, and includes statistics such as the second highest and average gross salary in the output file.

## Features
- Reads and concatenates data from multiple `.dat` files.
- Handles empty files gracefully.
- Removes duplicate records.
- Calculates gross salary (basic salary + allowances).
- Calculates and includes statistics (second highest and average gross salary) in the output file.
- Writes processed data to a CSV file with appended statistics.

## Requirements
- Python 3.x
- pandas library

## Installation
1. Ensure you have Python 3 installed.
2. Install the pandas library if not already installed:
    ```bash
    pip install pandas
    ```

## Usage
1. Place your `.dat` files in the input directory.
2. Define your input and output directories and the output file name.
3. Run the script.

### Example
1. Directory structure:
    ```
    input_directory/
        - DATA.dat
        - DATA1.dat
    output_directory/
    ```

2. Command to run the script:
    ```bash
    python file_processor.py
    ```

3. The processed data will be written to `output_directory/processed_data.csv`.

## Script Description

### read_input_files(input_directory)
- **Purpose**: Reads and concatenates data from all `.dat` files in the specified directory.
- **Parameters**: `input_directory` (str): The path to the directory containing input files.
- **Returns**: A pandas DataFrame containing the concatenated data from all input files.

### process_data(data)
- **Purpose**: Processes the data by removing duplicates and calculating the gross salary.
- **Parameters**: `data` (pandas DataFrame): The data to process.
- **Returns**: A pandas DataFrame with processed data.

### calculate_statistics(data)
- **Purpose**: Calculates statistics from the processed data.
- **Parameters**: `data` (pandas DataFrame): The processed data.
- **Returns**: A tuple containing the second highest gross salary and the average gross salary.

### write_output_file(data, output_file, second_highest_salary, average_salary)
- **Purpose**: Writes the processed data and statistics to a CSV file.
- **Parameters**:
  - `data` (pandas DataFrame): The processed data.
  - `output_file` (str): The path to the output file.
  - `second_highest_salary` (float): The second highest gross salary.
  - `average_salary` (float): The average gross salary.

### main(input_directory, output_directory, output_file_name)
- **Purpose**: Orchestrates the file processing workflow.
- **Parameters**:
  - `input_directory` (str): The path to the directory containing input files.
  - `output_directory` (str): The path to the directory to save the output file.
  - `output_file_name` (str): The name of the output file.

## Example Output
