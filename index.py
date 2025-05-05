# File Read & Write Challenge

def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"File successfully modified and saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print("Error: An issue occurred while reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")





# Error Handling Lab

def read_file_with_error_handling():
    filename = input("Enter the filename to read: ")
    
    try:
        # Try opening the file
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file {filename}.")
    except IOError:
        print("Error: An input/output error occurred.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


