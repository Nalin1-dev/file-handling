def modify_file_content(content):
    """
    Function to modify the content of a file.
    Modify this logic based on specific requirements (e.g., adding line numbers).
    """
    modified_lines = []
    for i, line in enumerate(content.splitlines(), start=1):
        modified_lines.append(f"{i}: {line}")  # Example: Add line numbers.
    return "\n".join(modified_lines)

def main():
    try:
        # Ask the user for the input filename.
        input_filename = input("Enter the filename to read: ")

        # Try opening and reading the file.
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content of the file.
        modified_content = modify_file_content(content)

        # Ask the user for the output filename.
        output_filename = input("Enter the filename to write the modified content: ")

        # Write the modified content to the output file.
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content successfully written to '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file cannot be read or written. Check file permissions or disk space.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

