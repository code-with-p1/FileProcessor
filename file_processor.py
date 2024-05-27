import os
import pandas as pd

# Responsibility: Reading and concatenating input files    
def read_input_files(input_directory):
    data_frames = []
    for file_name in os.listdir(input_directory):
        if file_name.endswith('.dat'):
            file_path = os.path.join(input_directory, file_name)
            # Check if the file is empty
            if os.path.getsize(file_path) > 0:
                df = pd.read_csv(file_path, delimiter='\t')
                data_frames.append(df)
            else:
                print(f"File {file_path} is empty and will be skipped.")

    if len(data_frames) != 0 :
        return pd.concat(data_frames, ignore_index=True)
    else:
        return pd.DataFrame([])

# Responsibility: Processing data (remove duplicates, calculate gross salary)
def process_data(data):
    if not data.empty:
        # Remove duplicate records
        data.drop_duplicates(inplace=True)

        # Calculate Gross Salary (Formula : Basic Salary + Allowances)
        data['gross_salary'] = data['basic_salary'] + data['allowances']

    return data

# Responsibility: Calculating statistics (second highest, average salary)
def calculate_statistics(data):
    second_highest_salary, average_salary = 0, 0.0
    if not data.empty:
        second_highest_salary = data['gross_salary'].nlargest(2).iloc[-1]
        average_salary = data['gross_salary'].mean()
    return second_highest_salary, average_salary

# Responsibility: Writing output file with processed data and statistics
def write_output_file(data, output_file, second_highest_salary, average_salary):
    # Write the processed data to CSV
    data.to_csv(output_file, index=False)

    # Append footer with statistics
    with open(output_file, 'w' if data.empty else 'a') as f:
        if not data.empty:
            f.write(f'Second Highest Salary={second_highest_salary},Average Salary={average_salary}')
        else:
            f.write(f'Empty Dataframe')

# Responsibility: Orchestrating the file processing workflow
def main(input_directory, output_directory, output_file_name):
    # Define paths
    output_file = os.path.join(output_directory, output_file_name)

    # Read input files
    data = read_input_files(input_directory)

    # Process data
    data = process_data(data)

    # Calculate statistics
    second_highest_salary, average_salary = calculate_statistics(data)

    # Write output file
    write_output_file(data, output_file, second_highest_salary, average_salary)

    print(f'Processed data written to {output_file}')

if __name__ == "__main__":
    # Define input and output directories
    input_directory = 'input_directory'
    output_directory = 'output_directory'
    output_file_name = 'processed_data.csv'

    # Run the main function
    main(input_directory, output_directory, output_file_name)