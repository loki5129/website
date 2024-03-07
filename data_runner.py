import requests

url = "https://www.met.ie/Open_Data/xml/Met-Sea-area.xml"  # Replace with the URL of the website you want to fetch

try:
    # Make a GET request to the website
    response = requests.get(url)
    response.raise_for_status()  # Check for any errors

    # Open a file in write mode ('w') to save the website content
    with open('website_data.txt', 'w', encoding='utf-8') as file:
        # Write the website content to the file
        file.write(response.text)

    print("Website data written to website_data.txt successfully.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching website data: {e}")
input_file_path = 'website_data.txt'
output_file_path = 'output_file.txt'

# Open the input file in read mode ('r') and the output file in write mode ('w')
with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Iterate through each line in the input file
    for line in input_file:
        # Check if the line is not a blank line
        if line.strip():
            # Write non-blank lines to the output file
            output_file.write(line)

print("Blank lines removed. Output saved to", output_file_path)

url = "https://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=53.277130;long=-6.144750"  # Replace with the URL of the website you want to fetch

try:
    # Make a GET request to the website
    response = requests.get(url)
    response.raise_for_status()  # Check for any errors

    # Open a file in write mode ('w') to save the website content
    with open('website_data.txt', 'a', encoding='utf-8') as file:
        # Write the website content to the file
        file.write(response.text)

    print("Website data written to website_data.txt successfully.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching website data: {e}")
input_file_path = 'website_data.txt'
output_file_path = 'output_file.txt'

# Open the input file in read mode ('r') and the output file in write mode ('w')
with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Iterate through each line in the input file
    for line in input_file:
        # Check if the line is not a blank line
        if line.strip():
            # Write non-blank lines to the output file
            output_file.write(line)

print("Blank lines removed. Output saved to", output_file_path)
