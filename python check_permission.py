import os

# Specify the path to the file or directory you want to check
path_to_check = 'data/data_file.csv'  # Replace with the actual path within your project

# Check if the path exists
if os.path.exists(path_to_check):
    # Check if it's a file
    if os.path.isfile(path_to_check):
        print(f"'{path_to_check}' is a file.")
    # Check if it's a directory
    elif os.path.isdir(path_to_check):
        print(f"'{path_to_check}' is a directory.")
    # If it's neither a file nor a directory
    else:
        print(f"'{path_to_check}' is neither a file nor a directory.")
    
    # Check read permission
    if os.access(path_to_check, os.R_OK):
        print(f"You have read permission for '{path_to_check}'.")
    else:
        print(f"You don't have read permission for '{path_to_check}'.")
    
    # Check write permission
    if os.access(path_to_check, os.W_OK):
        print(f"You have write permission for '{path_to_check}'.")
    else:
        print(f"You don't have write permission for '{path_to_check}'.")
else:
    print(f"'{path_to_check}' does not exist.")
