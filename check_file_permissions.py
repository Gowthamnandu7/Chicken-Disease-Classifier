import os

def check_file_permissions(filepaths):
    for filepath in filepaths:
        if os.path.exists(filepath):
            # Check if the file is readable
            if os.access(filepath, os.R_OK):
                print(f"File '{filepath}' is readable.")
            else:
                print(f"File '{filepath}' is not readable.")
            
            # Check if the file is writable
            if os.access(filepath, os.W_OK):
                print(f"File '{filepath}' is writable.")
            else:
                print(f"File '{filepath}' is not writable.")
            
            # Check if the file is executable
            if os.access(filepath, os.X_OK):
                print(f"File '{filepath}' is executable.")
            else:
                print(f"File '{filepath}' is not executable.")
        else:
            print(f"File '{filepath}' does not exist.")

# Check permissions for multiple files or directories
config_filepath = r"C:\Users\vgnun\OneDrive\Desktop\Chicken-Disease-Classifier\config\config.yaml"
params_filepath = r"C:\Users\vgnun\OneDrive\Desktop\Chicken-Disease-Classifier\params.yaml"

# Add other file or directory paths as needed
filepaths_to_check = [config_filepath, params_filepath]

check_file_permissions(filepaths_to_check)
