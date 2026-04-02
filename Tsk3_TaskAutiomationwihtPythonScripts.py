import re

def extract_emails(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File {input_filename} not found.")
        return

    # Regex pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    emails = re.findall(email_pattern, content)

    # Remove duplicates
    unique_emails = sorted(set(emails))

    try:
        with open(output_filename, 'w') as outfile:
            for email in unique_emails:
                outfile.write(email + '\n')
        print(f"Extracted {len(unique_emails)} emails and saved to {output_filename}.")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Example usage
input_file = 'input.txt'   # Replace with your input filename
output_file = 'emails.txt' # Replace with your desired output filename

extract_emails(input_file, output_file)