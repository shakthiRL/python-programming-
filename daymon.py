def copy_file(input_file_name, output_file_name):
    try:
        # Open the input file in read mode
        with open(input_file_name, 'r') as input_file:
            # Read the contents of the input file
            file_contents = input_file.read()

        # Open the output file in write mode
        with open(output_file_name, 'w') as output_file:
            # Write the contents to the output file
            output_file.write(file_contents)

        print("File contents copied successfully.")
    except FileNotFoundError:
        print("File not found. Please check the file names and try again.")
