from urllib.request import urlopen
import re
import datetime
import math
file=open("weather.xml", "w")
url = "https://www.met.ie/Open_Data/xml/Met-Sea-area.xml"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<div class=folder id=folder3>") + len("<div class=folder id=folder3>")
end_index = html.find("</div class=folder id=folder3>")
title = html[start_index:end_index]
file.write(title)
file.close
  # Your XML file path
xml_file_path = 'weather.xml'
output_file_path = 'weather.xml'

first_11_lines = []

# Open the file and read the first 11 lines
with open(xml_file_path, 'r') as file:
    for _ in range(11):
        line = file.readline()
        first_11_lines.append(line)
        result_string = '\n'.join(first_11_lines)

    # Read the remaining content
    xml_content = file.read()

# Remove all XML tags using regular expressions
content_without_tags = re.sub(r'<.*?>', '', xml_content)

# Write the inner content to a new file
with open(xml_file_path,"w") as outputfile:
    outputfile.write(result_string)
with open(xml_file_path, 'a') as output_file:
    output_file.write(content_without_tags)



 # Open the file and read the content
with open(xml_file_path, 'r') as file:
    xml_content = file.readlines()

# Remove empty lines
xml_content = [line for line in xml_content if line.strip()]

# Write the modified content to a new file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(xml_content)

with open(xml_file_path, 'r') as file:
    xml_content = file.readlines()

# Remove lines 7 to 12
xml_content = xml_content[:6] + xml_content[12:]

# Write the modified content to a new file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(xml_content)

print(f'Modified XML written to {output_file_path}')
 
# Variables to store lines 4 and 5
line_4 = None
line_5 = None

# Read the XML file
with open(xml_file_path, 'r') as file:
    # Read each line until reaching line 5
    for i, line in enumerate(file):
        if i == 3:  # Line numbers are zero-based
            line_4 = line.strip()
        elif i == 4:
            line_5 = line.strip()
            break  # Stop reading after line 5
lines=line_4 + "/n" + line_5


# Extract the "status" variable for 'gale' using regular expression
gale_status_match = re.search(r'<gale\s+status="(.*?)"\s*/>', lines)
gale_status = gale_status_match.group(1) if gale_status_match else None

# Extract the "status" variable for 'small-craft' using regular expression
small_craft_status_match = re.search(r'<small-craft\s+status="(.*?)"\s*/>', lines)
small_craft_status = small_craft_status_match.group(1) if small_craft_status_match else None

new_content_line_4 = 'gale force:' + gale_status

# Read the content of the XML file
with open(xml_file_path, 'r') as file:
    xml_content = file.read()

# Split the content into lines
lines = xml_content.split('\n')

# Replace the content of line 4
if len(lines) > 4:
    lines[3] = new_content_line_4

# Join the lines back into a single string
modified_xml_content = '\n'.join(lines)

# Write the modified content back to the XML file
with open(xml_file_path, 'w') as file:
    file.write(modified_xml_content)

new_content_line_5="small_craft:"+ small_craft_status
line1 = xml_content.split('\n')

# Replace the content of line 5
if len(line1) > 5:
    lines[4] = new_content_line_5

# Join the lines back into a single string
_xml_content = '\n'.join(lines)

# Write the modified content back to the XML file
with open(xml_file_path, 'w') as file:
    file.write(_xml_content)


with open(xml_file_path, 'r') as file:
    __xml_content = file.read()

# Remove the </title> closing tag from the first line
__xml_content = __xml_content.replace('</title>', '', 1)

# Write the modified content back to the XML file
with open(xml_file_path, 'w') as file:
    file.write(__xml_content)
 

# Read the content of the XML file
with open(xml_file_path, 'r') as file:
    ___xml_content = file.readlines()

# Extract issued-time and until-time values using regular expressions
issued_match = re.search(r'<issued issued-time\s*=\s*"([^"]+)"', "".join(___xml_content))
until_match = re.search(r'<until until-time\s*=\s*"([^"]+)"', "".join(___xml_content))
metsit_match = re.search(r'<met-sit time\s*=\s*"([^"]+)"', "".join(xml_content))
# Check if matches were found
if metsit_match:
    metsit_time=metsit_match.group(1)
else:
    metsit_time= None

if issued_match:
    issued_time = issued_match.group(1)
    
else:
    issued_time = None

if until_match:
    until_time = until_match.group(1)
    
else:
    until_time = None

# Update lines 2 and 3 in the content
___xml_content[1] = f'until until-time="{until_time}"\n'
___xml_content[2] = f'issued issued-time="{issued_time}"\n'
___xml_content[5] = f'met-sit time="{metsit_time}"\n'
___xml_content[13:16] = ['\n', '\n', '\n']
# Write the modified content back into the file
with open(xml_file_path, 'w') as file:
    file.writelines(___xml_content)

file=open("weather.xml","a")
url="https://www.met.ie/Open_Data/json/warning_IRELAND.json"
page=urlopen(url)
html = page.read().decode("utf-8")
start_index= html.find("<body>") +len("<body>")
end_index = html.find("</body>")
title = html[start_index:end_index]
file.write(title)
file.close

new_lines = [
    '\n',
    '\n',
    '\n'
]

# Read the original content of the XML file
with open(xml_file_path, 'r') as file:
    lines = file.readlines()

# Insert the new lines after line 61 (index 60 in Python)
index_to_insert = 63
for new_line in new_lines:
    lines.insert(index_to_insert, new_line)
    index_to_insert += 1

# Write the modified content back to the XML file
with open(xml_file_path, 'w') as file:
    file.writelines(lines)


file=open("weather.xml", "a")
url = "https://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=53.277130;long=-6.144750"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<div class=folder id=folder3>") + len("<div class=folder id=folder3>")
end_index = html.find("</div class=folder id=folder3>")
title = html[start_index:end_index]
file.write(title)
file.close



def extract_and_remove_attributes(xml_line, attributes_to_keep):
    # Extract specified attributes using regular expression
    attribute_matches = re.findall(r'(\w+)="([^"]+)"', xml_line)

    # Create a modified line with specified attributes
    modified_line =  ' '.join([f'{key}="{value}"' for key, value in attribute_matches if key in attributes_to_keep]) + '\n'
    return modified_line

with open(xml_file_path, 'r') as file:
    content = file.read()

# Remove all { and } characters
content_without_braces = content.replace('{', '').replace('}', '')

# Write the modified content back to the XML file
with open(xml_file_path, 'w') as file:
    file.write(content_without_braces)

# Read the content of the file
with open(xml_file_path, 'r') as file:
    lines = file.readlines()

# Get the 17th line
line_number_to_modify = 66  # Python uses 0-based indexing
line_to_modify = lines[line_number_to_modify]

# Specify attributes to keep
attributes_to_keep = ['created']

# Extract and remove specified attributes
modified_line = extract_and_remove_attributes(line_to_modify, attributes_to_keep)

# Replace the 17th line with the modified version
lines[line_number_to_modify] = modified_line

# Write the modified content back into the file
with open(xml_file_path, 'w') as file:
    file.writelines(lines)



with open(xml_file_path, 'r') as file:
    xml_content = file.read()

# Find the position of <meta> tags and remove the content between them
start_tag_pos = xml_content.find('<meta>')
end_tag_pos = xml_content.find('</meta>', start_tag_pos) + len('</meta>')

if start_tag_pos != -1 and end_tag_pos != -1:
    modified_content = xml_content[:start_tag_pos] + xml_content[end_tag_pos:]
else:
    modified_content = xml_content


# Optionally, save the modified content back to the file
with open( xml_file_path, 'w') as modified_file:
    modified_file.write(modified_content)


with open(xml_file_path, 'r') as file:
    file_content = file.read()

# Remove all occurrences of '<' and '>'
modified_content = file_content.replace('<', '').replace('>', '')


# Optionally, save the modified content back to the file
with open(xml_file_path, 'w') as modified_file:
    modified_file.write(modified_content)


# Get today's date and time
today = datetime.datetime.now()

# Round up to the next hour
rounded_today = today+datetime.timedelta(hours=1)
rounded_today = rounded_today.replace(minute=0, second=0, microsecond=0)

# Format the date and time as year-month-day hour:minute:second
formatted_today = rounded_today.strftime('%Y-%m-%dT%H:%M:%SZ')

# Your variable to compare
current_date_time = formatted_today  # Replace this with your actual variable
print(current_date_time)
# Check if the variable matches today's rounded-up date and time
# Specify the path to your file


# Variable to search for
search_variable = 'from='
search_variable2="to="
found_lines=[]
with open(xml_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and current_date_time in line and line.count(current_date_time) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_lines.append(next(file).strip())

# Now found_lines contains the next 19 lines after the match
print("Found lines:")
for idx, line in enumerate(found_lines, start=1):
    print(f"{line}")