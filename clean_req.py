import time

# Define the input and output file names
input_file = 'requirements_3.txt'
output_file = 'requirements_3.txt'

# Read each line separately from the input file and remove version numbers
with open(input_file, 'r') as infile:
    lines = infile.readlines()

# Remove version numbers and write each non-blank line separately to the output file
with open(output_file, 'w') as outfile:
    for line in lines:
        cleaned_line = line.split('==')[0] + '\n'
        if cleaned_line.strip() and cleaned_line.strip() != "\n":  # Check if the cleaned line is not blank
            outfile.write(cleaned_line)

print(f'Cleaned requirements saved to {output_file}')
time.sleep(3)  # Wait for 3 seconds before the next iteration
