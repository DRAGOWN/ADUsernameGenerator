import sys

def process_names(input_file, output_file):
    """
    Reads a file of names and generates four different formats for each name.

    Args:
        input_file (str): The path to the input file containing names.
        output_file (str): The path to the output file where results will be saved.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            # Split the line into first and last name
            try:
                first_name, last_name = line.split()
            except ValueError:
                outfile.write(f"Invalid line: {line}\n")
                continue

            # Generate the different formats
            format1 = f"{first_name}.{last_name}"
            format2 = f"{first_name}{last_name}"
            format3 = f"{first_name[0]}.{last_name}"
            format4 = f"{first_name[0]}{last_name}"

            # Write the formats to the output file
            outfile.write(f"{format1}\n{format2}\n{format3}\n{format4}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    process_names(input_path, output_path)
    print(f"Formatted names have been written to {output_path}.")
