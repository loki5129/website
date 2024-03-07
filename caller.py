import subprocess

def run_python_file(file_path):
    try:
        # Run the specified Python file using subprocess
        subprocess.run(['python', file_path], check=True)
        print(f"Successfully ran {file_path}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error running {file_path}: {e}")
        return False

if __name__ == "__main__":
    # Replace 'data_runner.py' and 'weather_data.py' with the names of the Python files you want to execute
    python_files_to_run = ['C:\\Users\\tjbwa\\Downloads\\website-main\\website-main\\data_runner.py', 'C:\\Users\\tjbwa\\Downloads\\website-main\\website-main\\weather_data.py','C:\\Users\\tjbwa\\Downloads\\website-main\\website-main\\vairable_store.py']

    # Keep track of whether both files ran successfully
    all_files_successful = True

    # Call the function to run each specified Python file
    for file_to_run in python_files_to_run:
        if not run_python_file(file_to_run):
            all_files_successful = False

    # Print a success message if both files ran successfully
    if all_files_successful:
        print("Both Python files ran successfully.")
    else:
        print("One or more Python files encountered errors.")
