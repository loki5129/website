from urllib.request import urlopen
import re
import datetime
import math
file=open("weather.txt", "w")
url = "https://www.met.ie/Open_Data/xml/Met-Sea-area.xml"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<div class=folder id=folder3>") + len("<div class=folder id=folder3>")
end_index = html.find("</div class=folder id=folder3>")
title = html[start_index:end_index]
file.write(title)
file.close
  # Your XML file path
txt_file_path = 'weather.txt'
output_file_path = 'weather.txt'

first_11_lines = []

# Open the file and read the first 11 lines
with open(txt_file_path, 'r') as file:
    for _ in range(11):
        line = file.readline()
        first_11_lines.append(line)
        result_string = '\n'.join(first_11_lines)

    # Read the remaining content
    xml_content = file.read()

# Remove all XML tags using regular expressions
content_without_tags = re.sub(r'<.*?>', '', xml_content)

# Write the inner content to a new file
with open(txt_file_path,"w") as outputfile:
    outputfile.write(result_string)
with open(txt_file_path, 'a') as output_file:
    output_file.write(content_without_tags)



 # Open the file and read the content
with open(txt_file_path, 'r') as file:
    xml_content = file.readlines()

# Remove empty lines
xml_content = [line for line in xml_content if line.strip()]

# Write the modified content to a new file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(xml_content)

with open(txt_file_path, 'r') as file:
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
with open(txt_file_path, 'r') as file:
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
with open(txt_file_path, 'r') as file:
    xml_content = file.read()

# Split the content into lines
lines = xml_content.split('\n')

# Replace the content of line 4
if len(lines) > 4:
    lines[3] = new_content_line_4

# Join the lines back into a single string
modified_xml_content = '\n'.join(lines)

# Write the modified content back to the XML file
with open(txt_file_path, 'w') as file:
    file.write(modified_xml_content)

new_content_line_5="small_craft:"+ small_craft_status
line1 = xml_content.split('\n')

# Replace the content of line 5
if len(line1) > 5:
    lines[4] = new_content_line_5

# Join the lines back into a single string
_xml_content = '\n'.join(lines)

# Write the modified content back to the XML file
with open(txt_file_path, 'w') as file:
    file.write(_xml_content)


with open(txt_file_path, 'r') as file:
    __xml_content = file.read()

# Remove the </title> closing tag from the first line
__xml_content = __xml_content.replace('</title>', '', 1)

# Write the modified content back to the XML file
with open(txt_file_path, 'w') as file:
    file.write(__xml_content)
 

# Read the content of the XML file
with open(txt_file_path, 'r') as file:
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
with open(txt_file_path, 'w') as file:
    file.writelines(___xml_content)

file=open("weather.txt","a")
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
with open(txt_file_path, 'r') as file:
    lines = file.readlines()

# Insert the new lines after line 61 (index 60 in Python)
index_to_insert = 63
for new_line in new_lines:
    lines.insert(index_to_insert, new_line)
    index_to_insert += 1

# Write the modified content back to the XML file
with open(txt_file_path, 'w') as file:
    file.writelines(lines)


file=open("weather.txt", "a")
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

with open(txt_file_path, 'r') as file:
    content = file.read()

# Remove all { and } characters
content_without_braces = content.replace('{', '').replace('}', '')



def replace_created_line(file_path):
    # Read the contents of the XML file
    with open(file_path, 'r') as file:
        xml_content = file.readlines()

    # Define a regex pattern to match the created attribute
    pattern = re.compile(r'created="([^"]+)"')

    # Search for the created attribute in each line
    for line_number, line in enumerate(xml_content, start=1):
        match = pattern.search(line)
        if match:
            created_value = match.group(1)
            variable_line = f'created="{created_value}"'
            xml_content[line_number - 1] = variable_line
            return xml_content

    # Return None if the created attribute is not found
    return None

# Example usage
new_xml_content = replace_created_line(txt_file_path)

if new_xml_content is not None:
    # Write the updated content back to the file
    with open(txt_file_path, 'w') as file:
        file.writelines(new_xml_content)
    print(f'The "created" attribute line has been replaced in the XML file.')
else:
    print('The "created" attribute is not found in the XML file.')

with open(txt_file_path, 'r') as file:
    xml_content = file.read()

# Find the position of <meta> tags and remove the content between them
start_tag_pos = xml_content.find('<meta>')
end_tag_pos = xml_content.find('</meta>', start_tag_pos) + len('</meta>')

if start_tag_pos != -1 and end_tag_pos != -1:
    modified_content = xml_content[:start_tag_pos] + xml_content[end_tag_pos:]
else:
    modified_content = xml_content


# Optionally, save the modified content back to the file
with open( txt_file_path, 'w') as modified_file:
    modified_file.write(modified_content)


with open(txt_file_path, 'r') as file:
    file_content = file.read()


modified_content = file_content.replace('<', '').replace('>', '')
with open(txt_file_path, 'w') as modified_file:
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
#print(current_date_time)
# Check if the variable matches today's rounded-up date and time
# Specify the path to your file
#print(formatted_h1)
# Variable to search for
search_variable = 'from='
search_variable2="to="
found_lines_c=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and current_date_time in line and line.count(current_date_time) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_lines_c.append(next(file).strip())

# Now found_lines contains the next 19 lines after the match
#print(found_lines_c)
#for idx, line in enumerate(found_lines, start=1):
   # print(f"{line}")
h1=today+ datetime.timedelta(hours=2)
rounded_h1 = today+datetime.timedelta(hours=2)
rounded_h1_1 = rounded_h1.replace(minute=0, second=0, microsecond=0)
formatted_h1 = rounded_h1_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h1=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h1 in line and line.count(formatted_h1) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h1.append(next(file).strip())
#print(found_h1)
                
h2=today+ datetime.timedelta(hours=3)
rounded_h2 = today+datetime.timedelta(hours=3)
rounded_h2_1 = rounded_h2.replace(minute=0, second=0, microsecond=0)
formatted_h2 = rounded_h2_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h2=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h2 in line and line.count(formatted_h2) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h2.append(next(file).strip())
#print(found_h2)

h3=today+ datetime.timedelta(hours=4)
rounded_h3 = today+datetime.timedelta(hours=4)
rounded_h3_1 = rounded_h3.replace(minute=0, second=0, microsecond=0)
formatted_h3 = rounded_h3_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h3=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h3 in line and line.count(formatted_h3) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h3.append(next(file).strip())
#print(found_h3)


h4=today+ datetime.timedelta(hours=5)
rounded_h4 = today+datetime.timedelta(hours=5)
rounded_h4_1 = rounded_h4.replace(minute=0, second=0, microsecond=0)
formatted_h4 = rounded_h4_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h4=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h4 in line and line.count(formatted_h4) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h4.append(next(file).strip())
#print(found_h4)
                
                
h5=today+ datetime.timedelta(hours=6)
rounded_h5 = today+datetime.timedelta(hours=6)
rounded_h5_1 = rounded_h5.replace(minute=0, second=0, microsecond=0)
formatted_h5 = rounded_h5_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h5=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h5 in line and line.count(formatted_h5) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h5.append(next(file).strip())
#print(found_h5)
                
h6=today+ datetime.timedelta(hours=7)
rounded_h6 = today+datetime.timedelta(hours=7)
rounded_h6_1 = rounded_h6.replace(minute=0, second=0, microsecond=0)
formatted_h6 = rounded_h6_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h6=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h6 in line and line.count(formatted_h6) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h6.append(next(file).strip())
#print(found_h6)
                

h7=today+ datetime.timedelta(hours=8)
rounded_h7 = today+datetime.timedelta(hours=8)
rounded_h7_1 = rounded_h7.replace(minute=0, second=0, microsecond=0)
formatted_h7 = rounded_h7_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h7=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h7 in line and line.count(formatted_h7) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h7.append(next(file).strip())
#print(found_h7)

h8=today+ datetime.timedelta(hours=9)
rounded_h8 = today+datetime.timedelta(hours=9)
rounded_h8_1 = rounded_h8.replace(minute=0, second=0, microsecond=0)
formatted_h8 = rounded_h8_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h8=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h8 in line and line.count(formatted_h8) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h8.append(next(file).strip())
#print(found_h8)
                

h9=today+ datetime.timedelta(hours=10)
rounded_h9 = today+datetime.timedelta(hours=10)
rounded_h9_1 = rounded_h9.replace(minute=0, second=0, microsecond=0)
formatted_h9 = rounded_h9_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h9=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h9 in line and line.count(formatted_h9) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h9.append(next(file).strip())
#print(found_h9)


h10=today+ datetime.timedelta(hours=11)
rounded_h10 = today+datetime.timedelta(hours=11)
rounded_h10_1 = rounded_h10.replace(minute=0, second=0, microsecond=0)
formatted_h10 = rounded_h10_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h10=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h10 in line and line.count(formatted_h10) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h10.append(next(file).strip())
#print(found_h10)


h11=today+ datetime.timedelta(hours=12)
rounded_h11 = today+datetime.timedelta(hours=12)
rounded_h11_1 = rounded_h11.replace(minute=0, second=0, microsecond=0)
formatted_h11 = rounded_h11_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h11=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h11 in line and line.count(formatted_h11) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h11.append(next(file).strip())
#print(found_h11)


h12=today+ datetime.timedelta(hours=13)
rounded_h12 = today+datetime.timedelta(hours=13)
rounded_h12_1 = rounded_h12.replace(minute=0, second=0, microsecond=0)
formatted_h12 = rounded_h12_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h12=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h12 in line and line.count(formatted_h12) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h12.append(next(file).strip())
#print(found_h12)
                

h13=today+ datetime.timedelta(hours=14)
rounded_h13 = today+datetime.timedelta(hours=14)
rounded_h13_1 = rounded_h13.replace(minute=0, second=0, microsecond=0)
formatted_h13 = rounded_h13_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h13=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h13 in line and line.count(formatted_h13) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h13.append(next(file).strip())
#print(found_h13)


d2_h1=today+ datetime.timedelta(hours=15)
rounded_d2_h1 = today+datetime.timedelta(hours=15)
rounded_d2_h1_1 = rounded_d2_h1.replace(minute=0, second=0, microsecond=0)
formatted_d2_h1 = rounded_d2_h1_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h1=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h1 in line and line.count(formatted_d2_h1) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h1.append(next(file).strip())
#print(found_d2_h1)

d2_h2=today+ datetime.timedelta(hours=16)
rounded_d2_h2 = today+datetime.timedelta(hours=16)
rounded_d2_h2_1 = rounded_d2_h2.replace(minute=0, second=0, microsecond=0)
formatted_d2_h2 = rounded_d2_h2_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h2=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h2 in line and line.count(formatted_d2_h2) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h2.append(next(file).strip())
#print(found_d2_h2)
                
d2_h3=today+ datetime.timedelta(hours=17)
rounded_d2_h3 = today+datetime.timedelta(hours=17)
rounded_d2_h3_1 = rounded_d2_h3.replace(minute=0, second=0, microsecond=0)
formatted_d2_h3 = rounded_d2_h3_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h3=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h3 in line and line.count(formatted_d2_h3) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h3.append(next(file).strip())
#print(found_d2_h3)
                
d2_h4=today+ datetime.timedelta(hours=47)
rounded_d2_h4 = today+datetime.timedelta(hours=47)
rounded_d2_h4_1 = rounded_d2_h4.replace(minute=0, second=0, microsecond=0)
formatted_d2_h4 = rounded_d2_h4_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h4=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h4 in line and line.count(formatted_d2_h4) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h4.append(next(file).strip())
#print(found_d2_h4)
    
d2_h5=today+ datetime.timedelta(hours=19)
rounded_d2_h5 = today+datetime.timedelta(hours=19)
rounded_d2_h5_1 = rounded_d2_h5.replace(minute=0, second=0, microsecond=0)
formatted_d2_h5 = rounded_d2_h5_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h5=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h5 in line and line.count(formatted_d2_h5) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h5.append(next(file).strip())
#print(found_d2_h5)


d2_h6=today+ datetime.timedelta(hours=48)
rounded_d2_h6 = today+datetime.timedelta(hours=20)
rounded_d2_h6_1 = rounded_d2_h6.replace(minute=0, second=0, microsecond=0)
formatted_d2_h6 = rounded_d2_h6_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h6=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h6 in line and line.count(formatted_d2_h6) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h6.append(next(file).strip())
#print(found_d2_h6)
       
d2_h6=today+ datetime.timedelta(hours=21)
rounded_d2_h6 = today+datetime.timedelta(hours=21)
rounded_d2_h6_1 = rounded_d2_h6.replace(minute=0, second=0, microsecond=0)
formatted_d2_h6 = rounded_d2_h6_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h6=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h6 in line and line.count(formatted_d2_h6) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h6.append(next(file).strip())
#print(found_d2_h6)


d2_h7=today+ datetime.timedelta(hours=22)
rounded_d2_h7 = today+datetime.timedelta(hours=22)
rounded_d2_h7_1 = rounded_d2_h7.replace(minute=0, second=0, microsecond=0)
formatted_d2_h7 = rounded_d2_h7_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h7=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h7 in line and line.count(formatted_d2_h7) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h7.append(next(file).strip())
#print(found_d2_h7)
       
d2_h8=today+ datetime.timedelta(hours=23)
rounded_d2_h8 = today+datetime.timedelta(hours=23)
rounded_d2_h8_1 = rounded_d2_h8.replace(minute=0, second=0, microsecond=0)
formatted_d2_h8 = rounded_d2_h8_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h8=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h8 in line and line.count(formatted_d2_h8) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h8.append(next(file).strip())
#print(found_d2_h8)
    

    d2_h9=today+ datetime.timedelta(hours=24)
rounded_d2_h9 = today+datetime.timedelta(hours=24)
rounded_d2_h9_1 = rounded_d2_h9.replace(minute=0, second=0, microsecond=0)
formatted_d2_h9 = rounded_d2_h9_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h9=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h9 in line and line.count(formatted_d2_h9) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h9.append(next(file).strip())
#print(found_d2_h9)
    

    d2_h10=today+ datetime.timedelta(hours=25)
rounded_d2_h10 = today+datetime.timedelta(hours=25)
rounded_d2_h10_1 = rounded_d2_h10.replace(minute=0, second=0, microsecond=0)
formatted_d2_h10 = rounded_d2_h10_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h10=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h10 in line and line.count(formatted_d2_h10) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h10.append(next(file).strip())
#print(found_d2_h10)
    

    d2_h11=today+ datetime.timedelta(hours=26)
rounded_d2_h11 = today+datetime.timedelta(hours=26)
rounded_d2_h11_1 = rounded_d2_h11.replace(minute=0, second=0, microsecond=0)
formatted_d2_h11 = rounded_d2_h11_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h11=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h11 in line and line.count(formatted_d2_h11) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h11.append(next(file).strip())
#print(found_d2_h11)
    

    d2_h12=today+ datetime.timedelta(hours=27)
rounded_d2_h12 = today+datetime.timedelta(hours=27)
rounded_d2_h12_1 = rounded_d2_h12.replace(minute=0, second=0, microsecond=0)
formatted_d2_h12 = rounded_d2_h12_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h12=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h12 in line and line.count(formatted_d2_h12) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h12.append(next(file).strip())
#print(found_d2_h12)
    
    d2_h13=today+ datetime.timedelta(hours=28)
rounded_d2_h13 = today+datetime.timedelta(hours=28)
rounded_d2_h13_1 = rounded_d2_h13.replace(minute=0, second=0, microsecond=0)
formatted_d2_h13 = rounded_d2_h13_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h13=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h13 in line and line.count(formatted_d2_h13) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h13.append(next(file).strip())
#print(found_d2_h13)


d2_h14=today+ datetime.timedelta(hours=29)
rounded_d2_h14 = today+datetime.timedelta(hours=29)
rounded_d2_h14_1 = rounded_d2_h14.replace(minute=0, second=0, microsecond=0)
formatted_d2_h14 = rounded_d2_h14_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h14=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h14 in line and line.count(formatted_d2_h14) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h14.append(next(file).strip())
#print(found_d2_h14)
    
d2_h15=today+ datetime.timedelta(hours=30)
rounded_d2_h15 = today+datetime.timedelta(hours=30)
rounded_d2_h15_1 = rounded_d2_h15.replace(minute=0, second=0, microsecond=0)
formatted_d2_h15 = rounded_d2_h15_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h15=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h15 in line and line.count(formatted_d2_h15) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h15.append(next(file).strip())
#print(found_d2_h15)


d2_h16=today+ datetime.timedelta(hours=31)
rounded_d2_h16 = today+datetime.timedelta(hours=31)
rounded_d2_h16_1 = rounded_d2_h16.replace(minute=0, second=0, microsecond=0)
formatted_d2_h16 = rounded_d2_h16_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h16=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h16 in line and line.count(formatted_d2_h16) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h16.append(next(file).strip())
#print(found_d2_h16)
    
d2_h17=today+ datetime.timedelta(hours=32)
rounded_d2_h17 = today+datetime.timedelta(hours=32)
rounded_d2_h17_1 = rounded_d2_h17.replace(minute=0, second=0, microsecond=0)
formatted_d2_h17 = rounded_d2_h17_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h17=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h17 in line and line.count(formatted_d2_h17) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h17.append(next(file).strip())
#print(found_d2_h17)

d2_h18=today+ datetime.timedelta(hours=33)
rounded_d2_h18 = today+datetime.timedelta(hours=33)
rounded_d2_h18_1 = rounded_d2_h18.replace(minute=0, second=0, microsecond=0)
formatted_d2_h18 = rounded_d2_h18_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h18=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h18 in line and line.count(formatted_d2_h18) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h18.append(next(file).strip())
#print(found_d2_h18)
    
d2_h19=today+ datetime.timedelta(hours=34)
rounded_d2_h19 = today+datetime.timedelta(hours=34)
rounded_d2_h19_1 = rounded_d2_h19.replace(minute=0, second=0, microsecond=0)
formatted_d2_h19 = rounded_d2_h19_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h19=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h19 in line and line.count(formatted_d2_h19) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h19.append(next(file).strip())
#print(found_d2_h19)
    
d2_h20=today+ datetime.timedelta(hours=34)
rounded_d2_h20 = today+datetime.timedelta(hours=34)
rounded_d2_h20_1 = rounded_d2_h20.replace(minute=0, second=0, microsecond=0)
formatted_d2_h20 = rounded_d2_h20_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h20=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h20 in line and line.count(formatted_d2_h20) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h20.append(next(file).strip())
#print(found_d2_h20)
    
d2_h21=today+ datetime.timedelta(hours=35)
rounded_d2_h21 = today+datetime.timedelta(hours=35)
rounded_d2_h21_1 = rounded_d2_h21.replace(minute=0, second=0, microsecond=0)
formatted_d2_h21 = rounded_d2_h21_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h21=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h21 in line and line.count(formatted_d2_h21) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h21.append(next(file).strip())
#print(found_d2_h21)
        
d2_h22=today+ datetime.timedelta(hours=36)
rounded_d2_h22 = today+datetime.timedelta(hours=36)
rounded_d2_h22_1 = rounded_d2_h22.replace(minute=0, second=0, microsecond=0)
formatted_d2_h22 = rounded_d2_h22_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h22=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h22 in line and line.count(formatted_d2_h22) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h22.append(next(file).strip())
#print(found_d2_h22)

d2_h23=today+ datetime.timedelta(hours=37)
rounded_d2_h23 = today+datetime.timedelta(hours=37)
rounded_d2_h23_1 = rounded_d2_h23.replace(minute=0, second=0, microsecond=0)
formatted_d2_h23 = rounded_d2_h23_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h23=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h23 in line and line.count(formatted_d2_h23) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h23.append(next(file).strip())
#print(found_d2_h23)


d2_h24=today+ datetime.timedelta(hours=38)
rounded_d2_h24 = today+datetime.timedelta(hours=38)
rounded_d2_h24_1 = rounded_d2_h24.replace(minute=0, second=0, microsecond=0)
formatted_d2_h24 = rounded_d2_h24_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h24=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h24 in line and line.count(formatted_d2_h24) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h24.append(next(file).strip())
#print(found_d2_h24)
                
d3_h1=today+ datetime.timedelta(hours=39)
rounded_d3_h1 = today+datetime.timedelta(hours=39)
rounded_d3_h1_1 = rounded_d3_h1.replace(minute=0, second=0, microsecond=0)
formatted_d3_h1 = rounded_d3_h1_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h1=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h1 in line and line.count(formatted_d3_h1) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h1.append(next(file).strip())
#print(found_d3_h1)

d3_h2=today+ datetime.timedelta(hours=40)
rounded_d3_h2 = today+datetime.timedelta(hours=40)
rounded_d3_h2_1 = rounded_d3_h2.replace(minute=0, second=0, microsecond=0)
formatted_d3_h2 = rounded_d3_h2_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h2=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h2 in line and line.count(formatted_d3_h2) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h2.append(next(file).strip())
#print(found__d3_h2)

d3_h3=today+ datetime.timedelta(hours=41)
rounded_d3_h3 = today+datetime.timedelta(hours=41)
rounded_d3_h3_1 = rounded_d3_h3.replace(minute=0, second=0, microsecond=0)
formatted_d3_h3 = rounded_d3_h3_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h3=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h3 in line and line.count(formatted_d3_h3) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h3.append(next(file).strip())
#print(found_d3_h3)
                
d3_h4=today+ datetime.timedelta(hours=42)
rounded_d3_h4 = today+datetime.timedelta(hours=42)
rounded_d3_h4_1 = rounded_d3_h4.replace(minute=0, second=0, microsecond=0)
formatted_d3_h4 = rounded_d3_h4_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h4=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h4 in line and line.count(formatted_d3_h4) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h4.append(next(file).strip())
#print(found_d3_h4)


d3_h5=today+ datetime.timedelta(hours=43)
rounded_d3_h5 = today+datetime.timedelta(hours=43)
rounded_d3_h5_1 = rounded_d3_h5.replace(minute=0, second=0, microsecond=0)
formatted_d3_h5 = rounded_d3_h5_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h5=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h5 in line and line.count(formatted_d3_h5) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h5.append(next(file).strip())
#print(found_d3_h5)

d3_h6=today+ datetime.timedelta(hours=44)
rounded_d3_h6 = today+datetime.timedelta(hours=44)
rounded_d3_h6_1 = rounded_d3_h6.replace(minute=0, second=0, microsecond=0)
formatted_d3_h6 = rounded_d3_h6_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h6=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h6 in line and line.count(formatted_d3_h6) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h6.append(next(file).strip())
#print(found_d3_h6)

d3_h7=today+ datetime.timedelta(hours=45)
rounded_d3_h7 = today+datetime.timedelta(hours=45)
rounded_d3_h7_1 = rounded_d3_h7.replace(minute=0, second=0, microsecond=0)
formatted_d3_h7 = rounded_d3_h7_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h7=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h7 in line and line.count(formatted_d3_h7) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h7.append(next(file).strip())
#print(found_d3_h7)

d3_h8=today+ datetime.timedelta(hours=46)
rounded_d3_h8 = today+datetime.timedelta(hours=46)
rounded_d3_h8_1 = rounded_d3_h8.replace(minute=0, second=0, microsecond=0)
formatted_d3_h8 = rounded_d3_h8_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h8=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h8 in line and line.count(formatted_d3_h8) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h8.append(next(file).strip())
#print(found_d3_h8)

d3_h9=today+ datetime.timedelta(hours=47)
rounded_d3_h9 = today+datetime.timedelta(hours=47)
rounded_d3_h9_1 = rounded_d3_h9.replace(minute=0, second=0, microsecond=0)
formatted_d3_h9 = rounded_d3_h9_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h9=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h9 in line and line.count(formatted_d3_h9) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h9.append(next(file).strip())
#print(found_d3_h9)

d3_h10=today+ datetime.timedelta(hours=48)
rounded_d3_h10 = today+datetime.timedelta(hours=48)
rounded_d3_h10_1 = rounded_d3_h10.replace(minute=0, second=0, microsecond=0)
formatted_d3_h10 = rounded_d3_h10_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h10=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h10 in line and line.count(formatted_d3_h10) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h10.append(next(file).strip())
#print(found_d3_h10)

d3_h11=today+ datetime.timedelta(hours=49)
rounded_d3_h11 = today+datetime.timedelta(hours=49)
rounded_d3_h11_1 = rounded_d3_h11.replace(minute=0, second=0, microsecond=0)
formatted_d3_h11 = rounded_d3_h11_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h11=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h11 in line and line.count(formatted_d3_h11) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h11.append(next(file).strip())
#print(found_d3_h11)

d3_h12=today+ datetime.timedelta(hours=50)
rounded_d3_h12 = today+datetime.timedelta(hours=50)
rounded_d3_h12_1 = rounded_d3_h12.replace(minute=0, second=0, microsecond=0)
formatted_d3_h12 = rounded_d3_h12_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h12=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h12 in line and line.count(formatted_d3_h12) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h12.append(next(file).strip())
#print(found_d3_h12)
d3_h13=today+ datetime.timedelta(hours=51)
rounded_d3_h13 = today+datetime.timedelta(hours=51)
rounded_d3_h13_1 = rounded_d3_h13.replace(minute=0, second=0, microsecond=0)
formatted_d3_h13 = rounded_d3_h13_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h13=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h13 in line and line.count(formatted_d3_h13) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h13.append(next(file).strip())
#print(found_d3_h13)
d3_h14=today+ datetime.timedelta(hours=52)
rounded_d3_h14 = today+datetime.timedelta(hours=52)
rounded_d3_h14_1 = rounded_d3_h14.replace(minute=0, second=0, microsecond=0)
formatted_d3_h14 = rounded_d3_h14_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h14=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h14 in line and line.count(formatted_d3_h14) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h14.append(next(file).strip())
#print(found_d3_h14)
d3_h15=today+ datetime.timedelta(hours=53)
rounded_d3_h15 = today+datetime.timedelta(hours=53)
rounded_d3_h15_1 = rounded_d3_h15.replace(minute=0, second=0, microsecond=0)
formatted_d3_h15 = rounded_d3_h15_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h15=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h15 in line and line.count(formatted_d3_h15) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h15.append(next(file).strip())
#print(found_d3_h15)
d3_h16=today+ datetime.timedelta(hours=54)
rounded_d3_h16 = today+datetime.timedelta(hours=54)
rounded_d3_h16_1 = rounded_d3_h16.replace(minute=0, second=0, microsecond=0)
formatted_d3_h16 = rounded_d3_h16_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h16=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h16 in line and line.count(formatted_d3_h16) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h16.append(next(file).strip())
#print(found_d3_h16)
d3_h17=today+ datetime.timedelta(hours=55)
rounded_d3_h17 = today+datetime.timedelta(hours=55)
rounded_d3_h17_1 = rounded_d3_h17.replace(minute=0, second=0, microsecond=0)
formatted_d3_h17 = rounded_d3_h17_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h17=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h17 in line and line.count(formatted_d3_h17) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h17.append(next(file).strip())
#print(found_d3_h17)
d3_h18=today+ datetime.timedelta(hours=56)
rounded_d3_h18 = today+datetime.timedelta(hours=56)
rounded_d3_h18_1 = rounded_d3_h18.replace(minute=0, second=0, microsecond=0)
formatted_d3_h18 = rounded_d3_h18_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h18=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h18 in line and line.count(formatted_d3_h18) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h18.append(next(file).strip())
#print(found_d3_h18)
d3_h18=today+ datetime.timedelta(hours=57)
rounded_d3_h18 = today+datetime.timedelta(hours=57)
rounded_d3_h18_1 = rounded_d3_h18.replace(minute=0, second=0, microsecond=0)
formatted_d3_h18 = rounded_d3_h18_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h18=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h18 in line and line.count(formatted_d3_h18) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h18.append(next(file).strip())
#print(found_d3_h18)
d3_h19=today+ datetime.timedelta(hours=58)
rounded_d3_h19 = today+datetime.timedelta(hours=58)
rounded_d3_h19_1 = rounded_d3_h19.replace(minute=0, second=0, microsecond=0)
formatted_d3_h19 = rounded_d3_h19_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h19=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h19 in line and line.count(formatted_d3_h19) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h19.append(next(file).strip())
#print(found_d3_h19)
d3_h20=today+ datetime.timedelta(hours=59)
rounded_d3_h20 = today+datetime.timedelta(hours=59)
rounded_d3_h20_1 = rounded_d3_h20.replace(minute=0, second=0, microsecond=0)
formatted_d3_h20 = rounded_d3_h20_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h20=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h20 in line and line.count(formatted_d3_h20) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h20.append(next(file).strip())
#print(found_d3_h20)
d3_h21=today+ datetime.timedelta(hours=60)
rounded_d3_h21 = today+datetime.timedelta(hours=60)
rounded_d3_h21_1 = rounded_d3_h21.replace(minute=0, second=0, microsecond=0)
formatted_d3_h21 = rounded_d3_h21_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h21=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h21 in line and line.count(formatted_d3_h21) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h21.append(next(file).strip())
#print(found_d3_h21)

d4_h1=today+ datetime.timedelta(hours=61)
rounded_d4_h1 = today+datetime.timedelta(hours=61)
rounded_d4_h1_1 = rounded_d4_h1.replace(minute=0, second=0, microsecond=0)
formatted_d4_h1 = rounded_d4_h1_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h1=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h1 in line and line.count(formatted_d4_h1) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h1.append(next(file).strip())
#print(found_d4_h1)          
 
d4_h2=today+ datetime.timedelta(hours=62)
rounded_d4_h2 = today+datetime.timedelta(hours=62)
rounded_d4_h2_1 = rounded_d4_h2.replace(minute=0, second=0, microsecond=0)
formatted_d4_h2 = rounded_d4_h2_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h2=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h2 in line and line.count(formatted_d4_h2) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h2.append(next(file).strip())
#print(found_d4_h2)          


d4_h3=today+ datetime.timedelta(hours=63)
rounded_d4_h3 = today+datetime.timedelta(hours=63)
rounded_d4_h3_1 = rounded_d4_h3.replace(minute=0, second=0, microsecond=0)
formatted_d4_h3 = rounded_d4_h3_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h3=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h3 in line and line.count(formatted_d4_h3) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h3.append(next(file).strip())
#print(found_d4_h3)          

d4_h4=today+ datetime.timedelta(hours=64)
rounded_d4_h4 = today+datetime.timedelta(hours=64)
rounded_d4_h4_1 = rounded_d4_h4.replace(minute=0, second=0, microsecond=0)
formatted_d4_h4 = rounded_d4_h4_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h4=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h4 in line and line.count(formatted_d4_h4) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h4.append(next(file).strip())
#print(found_d4_h4)          

d4_h5=today+ datetime.timedelta(hours=65)
rounded_d4_h5 = today+datetime.timedelta(hours=65)
rounded_d4_h5_1 = rounded_d4_h5.replace(minute=0, second=0, microsecond=0)
formatted_d4_h5 = rounded_d4_h5_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h5=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h5 in line and line.count(formatted_d4_h5) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h5.append(next(file).strip())
#print(found_d4_h5)          

d4_h6=today+ datetime.timedelta(hours=66)
rounded_d4_h6 = today+datetime.timedelta(hours=66)
rounded_d4_h6_1 = rounded_d4_h6.replace(minute=0, second=0, microsecond=0)
formatted_d4_h6 = rounded_d4_h6_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h6=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h6 in line and line.count(formatted_d4_h6) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h6.append(next(file).strip())
#print(found_d4_h6)          

d4_h7=today+ datetime.timedelta(hours=67)
rounded_d4_h7 = today+datetime.timedelta(hours=67)
rounded_d4_h7_1 = rounded_d4_h7.replace(minute=0, second=0, microsecond=0)
formatted_d4_h7 = rounded_d4_h7_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h7=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h7 in line and line.count(formatted_d4_h7) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h7.append(next(file).strip())
#print(found_d4_h7)          

d4_h8=today+ datetime.timedelta(hours=68)
rounded_d4_h8 = today+datetime.timedelta(hours=68)
rounded_d4_h8_1 = rounded_d4_h8.replace(minute=0, second=0, microsecond=0)
formatted_d4_h8 = rounded_d4_h8_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h8=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h8 in line and line.count(formatted_d4_h8) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h8.append(next(file).strip())
#print(found_d4_h8)          

d4_h9=today+ datetime.timedelta(hours=69)
rounded_d4_h9 = today+datetime.timedelta(hours=69)
rounded_d4_h9_1 = rounded_d4_h9.replace(minute=0, second=0, microsecond=0)
formatted_d4_h9 = rounded_d4_h9_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h9=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h9 in line and line.count(formatted_d4_h9) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h9.append(next(file).strip())
#print(found_d4_h9)          

d4_h10=today+ datetime.timedelta(hours=70)
rounded_d4_h10 = today+datetime.timedelta(hours=70)
rounded_d4_h10_1 = rounded_d4_h10.replace(minute=0, second=0, microsecond=0)
formatted_d4_h10 = rounded_d4_h10_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h10=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h10 in line and line.count(formatted_d4_h10) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h10.append(next(file).strip())
#print(found_d4_h10)          

d4_h11=today+ datetime.timedelta(hours=71)
rounded_d4_h11 = today+datetime.timedelta(hours=71)
rounded_d4_h11_1 = rounded_d4_h11.replace(minute=0, second=0, microsecond=0)
formatted_d4_h11 = rounded_d4_h11_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h11=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h11 in line and line.count(formatted_d4_h11) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h11.append(next(file).strip())
#print(found_d4_h11)          

d4_h12=today+ datetime.timedelta(hours=72)
rounded_d4_h12 = today+datetime.timedelta(hours=72)
rounded_d4_h12_1 = rounded_d4_h12.replace(minute=0, second=0, microsecond=0)
formatted_d4_h12 = rounded_d4_h12_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h12=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h12 in line and line.count(formatted_d4_h12) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h12.append(next(file).strip())
#print(found_d4_h12)          

d4_h13=today+ datetime.timedelta(hours=73)
rounded_d4_h13 = today+datetime.timedelta(hours=73)
rounded_d4_h13_1 = rounded_d4_h13.replace(minute=0, second=0, microsecond=0)
formatted_d4_h13 = rounded_d4_h13_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h13=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h13 in line and line.count(formatted_d4_h13) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h13.append(next(file).strip())
#print(found_d4_h13)          

d4_h14=today+ datetime.timedelta(hours=74)
rounded_d4_h14 = today+datetime.timedelta(hours=74)
rounded_d4_h14_1 = rounded_d4_h14.replace(minute=0, second=0, microsecond=0)
formatted_d4_h14 = rounded_d4_h14_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h14=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h14 in line and line.count(formatted_d4_h14) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h14.append(next(file).strip())
#print(found_d4_h14)          

d4_h15=today+ datetime.timedelta(hours=75)
rounded_d4_h15 = today+datetime.timedelta(hours=75)
rounded_d4_h15_1 = rounded_d4_h15.replace(minute=0, second=0, microsecond=0)
formatted_d4_h15 = rounded_d4_h15_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h15=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h15 in line and line.count(formatted_d4_h15) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h15.append(next(file).strip())
#print(found_d4_h15)          

d4_h16=today+ datetime.timedelta(hours=76)
rounded_d4_h16 = today+datetime.timedelta(hours=76)
rounded_d4_h16_1 = rounded_d4_h16.replace(minute=0, second=0, microsecond=0)
formatted_d4_h16 = rounded_d4_h16_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h16=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h16 in line and line.count(formatted_d4_h16) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h16.append(next(file).strip())
#print(found_d4_h16)          

d4_h17=today+ datetime.timedelta(hours=77)
rounded_d4_h17 = today+datetime.timedelta(hours=77)
rounded_d4_h17_1 = rounded_d4_h17.replace(minute=0, second=0, microsecond=0)
formatted_d4_h17 = rounded_d4_h17_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h17=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h17 in line and line.count(formatted_d4_h17) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h17.append(next(file).strip())
#print(found_d4_h17)          

d4_h18=today+ datetime.timedelta(hours=78)
rounded_d4_h18 = today+datetime.timedelta(hours=78)
rounded_d4_h18_1 = rounded_d4_h18.replace(minute=0, second=0, microsecond=0)
formatted_d4_h18 = rounded_d4_h18_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h18=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h18 in line and line.count(formatted_d4_h18) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h18.append(next(file).strip())
#print(found_d4_h18)          

d4_h19=today+ datetime.timedelta(hours=79)
rounded_d4_h19 = today+datetime.timedelta(hours=79)
rounded_d4_h19_1 = rounded_d4_h19.replace(minute=0, second=0, microsecond=0)
formatted_d4_h19 = rounded_d4_h19_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h19=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h19 in line and line.count(formatted_d4_h19) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h19.append(next(file).strip())
#print(found_d4_h19)          

d4_h20=today+ datetime.timedelta(hours=80)
rounded_d4_h20 = today+datetime.timedelta(hours=80)
rounded_d4_h20_1 = rounded_d4_h20.replace(minute=0, second=0, microsecond=0)
formatted_d4_h20 = rounded_d4_h20_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h20=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h20 in line and line.count(formatted_d4_h20) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h20.append(next(file).strip())
#print(found_d4_h20)          

d4_h21=today+ datetime.timedelta(hours=81)
rounded_d4_h21 = today+datetime.timedelta(hours=81)
rounded_d4_h21_1 = rounded_d4_h21.replace(minute=0, second=0, microsecond=0)
formatted_d4_h21 = rounded_d4_h21_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h21=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h21 in line and line.count(formatted_d4_h21) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h21.append(next(file).strip())
#print(found_d4_h21)          

d4_h22=today+ datetime.timedelta(hours=82)
rounded_d4_h22 = today+datetime.timedelta(hours=82)
rounded_d4_h22_1 = rounded_d4_h22.replace(minute=0, second=0, microsecond=0)
formatted_d4_h22 = rounded_d4_h22_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h22=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h22 in line and line.count(formatted_d4_h22) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h22.append(next(file).strip())
#print(found_d4_h22)          

d4_h23=today+ datetime.timedelta(hours=83)
rounded_d4_h23 = today+datetime.timedelta(hours=83)
rounded_d4_h23_1 = rounded_d4_h23.replace(minute=0, second=0, microsecond=0)
formatted_d4_h23 = rounded_d4_h23_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h23=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h23 in line and line.count(formatted_d4_h23) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h23.append(next(file).strip())
#print(found_d4_h23)          

d4_h24=today+ datetime.timedelta(hours=84)
rounded_d4_h24 = today+datetime.timedelta(hours=84)
rounded_d4_h24_1 = rounded_d4_h24.replace(minute=0, second=0, microsecond=0)
formatted_d4_h24 = rounded_d4_h24_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h24=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h24 in line and line.count(formatted_d4_h24) == 2:
            print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h24.append(next(file).strip())
#print(found_d4_h24)          
                                                                                                                                                                                                                                              