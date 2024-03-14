
import re
import datetime
txt_file_path="output_file.txt"
# Get today's date and time
today = datetime.datetime.now()

# Round up to the next hour
rounded_today = today+datetime.timedelta(hours=1)
rounded_today = rounded_today.replace(minute=0, second=0, microsecond=0)

# Format the date and time as year-month-day hour:minute:second
formatted_today = rounded_today.strftime('%Y-%m-%dT%H:%M:%SZ')

# Your variable to compare
current_date_time = formatted_today  # Replace this with your actual variable
##print(current_date_time)
# Check if the variable matches today's rounded-up date and time
# Specify the path to your file
##print(formatted_h1)
# Variable to search for
search_variable = 'from='
search_variable2="to="
found_lines_c=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and current_date_time in line and line.count(current_date_time) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_lines_c.append(next(file).strip())

# Now found_lines contains the next 19 lines after the match
##print(found_lines_c)
#for idx, line in enumerate(found_lines, start=1):
   # #print(f"{line}")
celsius_pattern = re.compile(r'temperature.*?value="(.*?)"')
wind_d_pattern= re.compile(r'windDirection.*?name="(.*?)"')
wind_b_pattern= re.compile(r'windSpeed.*?mps="(.*?)"')
wind_bf_pattern=re.compile(r'windSpeed.*?beaufort="(.*?)"')
wind_g_pattern= re.compile(r'windGust.*?mps="(.*?)"')
celsius_value_c = [float(match.group(1)) for line in found_lines_c if (match := celsius_pattern.search(line))]
wind_d_value_c= [str(match.group(1)) for line in found_lines_c if (match := wind_d_pattern.search(line))]
wind_b_value_c = [float(match.group(1)) for line in found_lines_c if (match := wind_b_pattern.search(line))]
wind_b_c_float_values_c = [item for item in wind_b_value_c if isinstance(item, float)]
wind_b_k_value_c = [round(item * 1.944,1)for item in wind_b_c_float_values_c]
wind_g_value_c= [float(match.group(1)) for line in found_lines_c if (match := wind_g_pattern.search(line))]
wind_g_float_values_c = [item for item in wind_g_value_c if isinstance(item, float)]
wind_g_k_value_c=[round(item * 1.944,1) for item in wind_g_float_values_c]
wind_bf_value_c= [int(match.group(1)) for line in found_lines_c if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_c)
#print("wind direction: ",wind_d_value_c)
#print("wind blow in mps: ",wind_b_value_c)
#print("wind blow in kts: ",wind_b_k_value_c)
#print("beaufort scale: ",wind_bf_value_c)
#print("wind gust in mps: ",wind_g_value_c)
#print("wind gust in knots: ", wind_g_k_value_c)

h1=today+ datetime.timedelta(hours=2)
rounded_h1 = today+datetime.timedelta(hours=2)
rounded_h1_1 = rounded_h1.replace(minute=0, second=0, microsecond=0)
formatted_h1 = rounded_h1_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h1=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h1 in line and line.count(formatted_h1) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h1.append(next(file).strip())
##print(found_h1)
             
celsius_value_h1 = [float(match.group(1)) for line in found_h1 if (match := celsius_pattern.search(line))]
wind_d_value_h1= [str(match.group(1)) for line in found_h1 if (match := wind_d_pattern.search(line))]
wind_b_value_h1 = [float(match.group(1)) for line in found_h1 if (match := wind_b_pattern.search(line))]
wind_b_h1_float_values_h1 = [item for item in wind_b_value_h1 if isinstance(item, float)]
wind_b_k_value_h1 = [item * 1.944 for item in wind_b_h1_float_values_h1]
wind_g_value_h1= [float(match.group(1)) for line in found_h1 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h1 = [item for item in wind_g_value_h1 if isinstance(item, float)]
wind_g_k_value_h1=[item * 1.944 for item in wind_g_float_values_h1]
wind_bf_value_h1= [int(match.group(1)) for line in found_h1 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h1)
#print("wind direction: ",wind_d_value_h1)
#print("wind blow in mps: ",wind_b_value_h1)
#print("wind blow in kts: ",wind_b_k_value_h1)
#print("beaufort scale: ",wind_bf_value_h1)
#print("wind gust in mps: ",wind_g_value_h1)
#print("wind gust in knots: ", wind_g_k_value_h1)

                
h2=today+ datetime.timedelta(hours=3)
rounded_h2 = today+datetime.timedelta(hours=3)
rounded_h2_1 = rounded_h2.replace(minute=0, second=0, microsecond=0)
formatted_h2 = rounded_h2_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h2=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h2 in line and line.count(formatted_h2) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h2.append(next(file).strip())
##print(found_h2)

             
celsius_value_h2 = [float(match.group(1)) for line in found_h2 if (match := celsius_pattern.search(line))]
wind_d_value_h2= [str(match.group(1)) for line in found_h2 if (match := wind_d_pattern.search(line))]
wind_b_value_h2 = [float(match.group(1)) for line in found_h2 if (match := wind_b_pattern.search(line))]
wind_b_h2_float_values_h2 = [item for item in wind_b_value_h2 if isinstance(item, float)]
wind_b_k_value_h2 = [item * 1.944 for item in wind_b_h2_float_values_h2]
wind_g_value_h2= [float(match.group(1)) for line in found_h2 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h2 = [item for item in wind_g_value_h2 if isinstance(item, float)]
wind_g_k_value_h2=[item * 1.944 for item in wind_g_float_values_h2]
wind_bf_value_h2= [int(match.group(1)) for line in found_h2 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h2)
#print("wind direction: ",wind_d_value_h2)
#print("wind blow in mps: ",wind_b_value_h2)
#print("wind blow in kts: ",wind_b_k_value_h2)
#print("beaufort scale: ",wind_bf_value_h2)
#print("wind gust in mps: ",wind_g_value_h2)
#print("wind gust in knots: ", wind_g_k_value_h2)

h3=today+ datetime.timedelta(hours=4)
rounded_h3 = today+datetime.timedelta(hours=4)
rounded_h3_1 = rounded_h3.replace(minute=0, second=0, microsecond=0)
formatted_h3 = rounded_h3_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h3=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h3 in line and line.count(formatted_h3) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h3.append(next(file).strip())
##print(found_h3)


celsius_value_h3 = [float(match.group(1)) for line in found_h3 if (match := celsius_pattern.search(line))]
wind_d_value_h3= [str(match.group(1)) for line in found_h3 if (match := wind_d_pattern.search(line))]
wind_b_value_h3 = [float(match.group(1)) for line in found_h3 if (match := wind_b_pattern.search(line))]
wind_b_h3_float_values_h3 = [item for item in wind_b_value_h3 if isinstance(item, float)]
wind_b_k_value_h3 = [item * 1.944 for item in wind_b_h3_float_values_h3]
wind_g_value_h3= [float(match.group(1)) for line in found_h3 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h3 = [item for item in wind_g_value_h3 if isinstance(item, float)]
wind_g_k_value_h3=[item * 1.944 for item in wind_g_float_values_h3]
wind_bf_value_h3= [int(match.group(1)) for line in found_h3 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h3)
#print("wind direction: ",wind_d_value_h3)
#print("wind blow in mps: ",wind_b_value_h3)
#print("wind blow in kts: ",wind_b_k_value_h3)
#print("beaufort scale: ",wind_bf_value_h3)
#print("wind gust in mps: ",wind_g_value_h3)
#print("wind gust in knots: ", wind_g_k_value_h3)

h4=today+ datetime.timedelta(hours=5)
rounded_h4 = today+datetime.timedelta(hours=5)
rounded_h4_1 = rounded_h4.replace(minute=0, second=0, microsecond=0)
formatted_h4 = rounded_h4_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h4=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h4 in line and line.count(formatted_h4) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h4.append(next(file).strip())
##print(found_h4)
                

celsius_value_h4 = [float(match.group(1)) for line in found_h4 if (match := celsius_pattern.search(line))]
wind_d_value_h4= [str(match.group(1)) for line in found_h4 if (match := wind_d_pattern.search(line))]
wind_b_value_h4 = [float(match.group(1)) for line in found_h4 if (match := wind_b_pattern.search(line))]
wind_b_h4_float_values_h4 = [item for item in wind_b_value_h4 if isinstance(item, float)]
wind_b_k_value_h4 = [item * 1.944 for item in wind_b_h4_float_values_h4]
wind_g_value_h4= [float(match.group(1)) for line in found_h4 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h4 = [item for item in wind_g_value_h4 if isinstance(item, float)]
wind_g_k_value_h4=[item * 1.944 for item in wind_g_float_values_h4]
wind_bf_value_h4= [int(match.group(1)) for line in found_h4 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h4)
#print("wind direction: ",wind_d_value_h4)
#print("wind blow in mps: ",wind_b_value_h4)
#print("wind blow in kts: ",wind_b_k_value_h4)
#print("beaufort scale: ",wind_bf_value_h4)
#print("wind gust in mps: ",wind_g_value_h4)
#print("wind gust in knots: ", wind_g_k_value_h4)                
                
h5=today+ datetime.timedelta(hours=6)
rounded_h5 = today+datetime.timedelta(hours=6)
rounded_h5_1 = rounded_h5.replace(minute=0, second=0, microsecond=0)
formatted_h5 = rounded_h5_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h5=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h5 in line and line.count(formatted_h5) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h5.append(next(file).strip())
##print(found_h5)
                

celsius_value_h5 = [float(match.group(1)) for line in found_h5 if (match := celsius_pattern.search(line))]
wind_d_value_h5= [str(match.group(1)) for line in found_h5 if (match := wind_d_pattern.search(line))]
wind_b_value_h5 = [float(match.group(1)) for line in found_h5 if (match := wind_b_pattern.search(line))]
wind_b_h5_float_values_h5 = [item for item in wind_b_value_h5 if isinstance(item, float)]
wind_b_k_value_h5 = [item * 1.944 for item in wind_b_h5_float_values_h5]
wind_g_value_h5= [float(match.group(1)) for line in found_h5 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h5 = [item for item in wind_g_value_h5 if isinstance(item, float)]
wind_g_k_value_h5=[item * 1.944 for item in wind_g_float_values_h5]
wind_bf_value_h5= [int(match.group(1)) for line in found_h5 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h5)
#print("wind direction: ",wind_d_value_h5)
#print("wind blow in mps: ",wind_b_value_h5)
#print("wind blow in kts: ",wind_b_k_value_h5)
#print("beaufort scale: ",wind_bf_value_h5)
#print("wind gust in mps: ",wind_g_value_h5)
#print("wind gust in knots: ", wind_g_k_value_h5)

h6=today+ datetime.timedelta(hours=7)
rounded_h6 = today+datetime.timedelta(hours=7)
rounded_h6_1 = rounded_h6.replace(minute=0, second=0, microsecond=0)
formatted_h6 = rounded_h6_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h6=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h6 in line and line.count(formatted_h6) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h6.append(next(file).strip())
##print(found_h6)
                

celsius_value_h6 = [float(match.group(1)) for line in found_h6 if (match := celsius_pattern.search(line))]
wind_d_value_h6= [str(match.group(1)) for line in found_h6 if (match := wind_d_pattern.search(line))]
wind_b_value_h6 = [float(match.group(1)) for line in found_h6 if (match := wind_b_pattern.search(line))]
wind_b_h6_float_values_h6 = [item for item in wind_b_value_h6 if isinstance(item, float)]
wind_b_k_value_h6 = [item * 1.944 for item in wind_b_h6_float_values_h6]
wind_g_value_h6= [float(match.group(1)) for line in found_h6 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h6 = [item for item in wind_g_value_h6 if isinstance(item, float)]
wind_g_k_value_h6=[item * 1.944 for item in wind_g_float_values_h6]
wind_bf_value_h6= [int(match.group(1)) for line in found_h6 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h6)
#print("wind direction: ",wind_d_value_h6)
#print("wind blow in mps: ",wind_b_value_h6)
#print("wind blow in kts: ",wind_b_k_value_h6)
#print("beaufort scale: ",wind_bf_value_h6)
#print("wind gust in mps: ",wind_g_value_h6)
#print("wind gust in knots: ", wind_g_k_value_h6)                
                

h7=today+ datetime.timedelta(hours=8)
rounded_h7 = today+datetime.timedelta(hours=8)
rounded_h7_1 = rounded_h7.replace(minute=0, second=0, microsecond=0)
formatted_h7 = rounded_h7_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h7=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h7 in line and line.count(formatted_h7) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h7.append(next(file).strip())
##print(found_h7)


celsius_value_h7 = [float(match.group(1)) for line in found_h7 if (match := celsius_pattern.search(line))]
wind_d_value_h7= [str(match.group(1)) for line in found_h7 if (match := wind_d_pattern.search(line))]
wind_b_value_h7 = [float(match.group(1)) for line in found_h7 if (match := wind_b_pattern.search(line))]
wind_b_h7_float_values_h7 = [item for item in wind_b_value_h7 if isinstance(item, float)]
wind_b_k_value_h7 = [item * 1.944 for item in wind_b_h7_float_values_h7]
wind_g_value_h7= [float(match.group(1)) for line in found_h7 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h7 = [item for item in wind_g_value_h7 if isinstance(item, float)]
wind_g_k_value_h7=[item * 1.944 for item in wind_g_float_values_h7]
wind_bf_value_h7= [int(match.group(1)) for line in found_h7 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h7)
#print("wind direction: ",wind_d_value_h7)
#print("wind blow in mps: ",wind_b_value_h7)
#print("wind blow in kts: ",wind_b_k_value_h7)
#print("beaufort scale: ",wind_bf_value_h7)
#print("wind gust in mps: ",wind_g_value_h7)
#print("wind gust in knots: ", wind_g_k_value_h7)

h8=today+ datetime.timedelta(hours=9)
rounded_h8 = today+datetime.timedelta(hours=9)
rounded_h8_1 = rounded_h8.replace(minute=0, second=0, microsecond=0)
formatted_h8 = rounded_h8_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h8=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h8 in line and line.count(formatted_h8) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h8.append(next(file).strip())
##print(found_h8)
                

celsius_value_h8 = [float(match.group(1)) for line in found_h8 if (match := celsius_pattern.search(line))]
wind_d_value_h8= [str(match.group(1)) for line in found_h8 if (match := wind_d_pattern.search(line))]
wind_b_value_h8 = [float(match.group(1)) for line in found_h8 if (match := wind_b_pattern.search(line))]
wind_b_h8_float_values_h8 = [item for item in wind_b_value_h8 if isinstance(item, float)]
wind_b_k_value_h8 = [item * 1.944 for item in wind_b_h8_float_values_h8]
wind_g_value_h8= [float(match.group(1)) for line in found_h8 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h8 = [item for item in wind_g_value_h8 if isinstance(item, float)]
wind_g_k_value_h8=[item * 1.944 for item in wind_g_float_values_h8]
wind_bf_value_h8= [int(match.group(1)) for line in found_h8 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h8)
#print("wind direction: ",wind_d_value_h8)
#print("wind blow in mps: ",wind_b_value_h8)
#print("wind blow in kts: ",wind_b_k_value_h8)
#print("beaufort scale: ",wind_bf_value_h8)
#print("wind gust in mps: ",wind_g_value_h8)
#print("wind gust in knots: ", wind_g_k_value_h8)

h9=today+ datetime.timedelta(hours=10)
rounded_h9 = today+datetime.timedelta(hours=10)
rounded_h9_1 = rounded_h9.replace(minute=0, second=0, microsecond=0)
formatted_h9 = rounded_h9_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h9=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h9 in line and line.count(formatted_h9) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h9.append(next(file).strip())
##print(found_h9)


celsius_value_h9 = [float(match.group(1)) for line in found_h9 if (match := celsius_pattern.search(line))]
wind_d_value_h9= [str(match.group(1)) for line in found_h9 if (match := wind_d_pattern.search(line))]
wind_b_value_h9 = [float(match.group(1)) for line in found_h9 if (match := wind_b_pattern.search(line))]
wind_b_h9_float_values_h9 = [item for item in wind_b_value_h9 if isinstance(item, float)]
wind_b_k_value_h9 = [item * 1.944 for item in wind_b_h9_float_values_h9]
wind_g_value_h9= [float(match.group(1)) for line in found_h9 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h9 = [item for item in wind_g_value_h9 if isinstance(item, float)]
wind_g_k_value_h9=[item * 1.944 for item in wind_g_float_values_h9]
wind_bf_value_h9= [int(match.group(1)) for line in found_h9 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h9)
#print("wind direction: ",wind_d_value_h9)
#print("wind blow in mps: ",wind_b_value_h9)
#print("wind blow in kts: ",wind_b_k_value_h9)
#print("beaufort scale: ",wind_bf_value_h9)
#print("wind gust in mps: ",wind_g_value_h9)
#print("wind gust in knots: ", wind_g_k_value_h9)

h10=today+ datetime.timedelta(hours=11)
rounded_h10 = today+datetime.timedelta(hours=11)
rounded_h10_1 = rounded_h10.replace(minute=0, second=0, microsecond=0)
formatted_h10 = rounded_h10_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h10=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h10 in line and line.count(formatted_h10) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h10.append(next(file).strip())
##print(found_h10)


celsius_value_h10 = [float(match.group(1)) for line in found_h10 if (match := celsius_pattern.search(line))]
wind_d_value_h10= [str(match.group(1)) for line in found_h10 if (match := wind_d_pattern.search(line))]
wind_b_value_h10 = [float(match.group(1)) for line in found_h10 if (match := wind_b_pattern.search(line))]
wind_b_h10_float_values_h10 = [item for item in wind_b_value_h10 if isinstance(item, float)]
wind_b_k_value_h10 = [item * 1.944 for item in wind_b_h10_float_values_h10]
wind_g_value_h10= [float(match.group(1)) for line in found_h10 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h10 = [item for item in wind_g_value_h10 if isinstance(item, float)]
wind_g_k_value_h10=[item * 1.944 for item in wind_g_float_values_h10]
wind_bf_value_h10= [int(match.group(1)) for line in found_h10 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h10)
#print("wind direction: ",wind_d_value_h10)
#print("wind blow in mps: ",wind_b_value_h10)
#print("wind blow in kts: ",wind_b_k_value_h10)
#print("beaufort scale: ",wind_bf_value_h10)
#print("wind gust in mps: ",wind_g_value_h10)
#print("wind gust in knots: ", wind_g_k_value_h10)

h11=today+ datetime.timedelta(hours=12)
rounded_h11 = today+datetime.timedelta(hours=12)
rounded_h11_1 = rounded_h11.replace(minute=0, second=0, microsecond=0)
formatted_h11 = rounded_h11_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h11=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h11 in line and line.count(formatted_h11) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h11.append(next(file).strip())
##print(found_h11)
                

celsius_value_h11 = [float(match.group(1)) for line in found_h11 if (match := celsius_pattern.search(line))]
wind_d_value_h11= [str(match.group(1)) for line in found_h11 if (match := wind_d_pattern.search(line))]
wind_b_value_h11 = [float(match.group(1)) for line in found_h11 if (match := wind_b_pattern.search(line))]
wind_b_h11_float_values_h11 = [item for item in wind_b_value_h11 if isinstance(item, float)]
wind_b_k_value_h11 = [item * 1.944 for item in wind_b_h11_float_values_h11]
wind_g_value_h11= [float(match.group(1)) for line in found_h11 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h11 = [item for item in wind_g_value_h11 if isinstance(item, float)]
wind_g_k_value_h11=[item * 1.944 for item in wind_g_float_values_h11]
wind_bf_value_h11= [int(match.group(1)) for line in found_h11 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h11)
#print("wind direction: ",wind_d_value_h11)
#print("wind blow in mps: ",wind_b_value_h11)
#print("wind blow in kts: ",wind_b_k_value_h11)
#print("beaufort scale: ",wind_bf_value_h11)
#print("wind gust in mps: ",wind_g_value_h11)
#print("wind gust in knots: ", wind_g_k_value_h11)

h12=today+ datetime.timedelta(hours=13)
rounded_h12 = today+datetime.timedelta(hours=13)
rounded_h12_1 = rounded_h12.replace(minute=0, second=0, microsecond=0)
formatted_h12 = rounded_h12_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h12=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h12 in line and line.count(formatted_h12) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h12.append(next(file).strip())
##print(found_h12)
                

celsius_value_h12 = [float(match.group(1)) for line in found_h12 if (match := celsius_pattern.search(line))]
wind_d_value_h12= [str(match.group(1)) for line in found_h12 if (match := wind_d_pattern.search(line))]
wind_b_value_h12 = [float(match.group(1)) for line in found_h12 if (match := wind_b_pattern.search(line))]
wind_b_h12_float_values_h12 = [item for item in wind_b_value_h12 if isinstance(item, float)]
wind_b_k_value_h12 = [item * 1.944 for item in wind_b_h12_float_values_h12]
wind_g_value_h12= [float(match.group(1)) for line in found_h12 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h12 = [item for item in wind_g_value_h12 if isinstance(item, float)]
wind_g_k_value_h12=[item * 1.944 for item in wind_g_float_values_h12]
wind_bf_value_h12= [int(match.group(1)) for line in found_h12 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h12)
#print("wind direction: ",wind_d_value_h12)
#print("wind blow in mps: ",wind_b_value_h12)
#print("wind blow in kts: ",wind_b_k_value_h12)
#print("beaufort scale: ",wind_bf_value_h12)
#print("wind gust in mps: ",wind_g_value_h12)
#print("wind gust in knots: ", wind_g_k_value_h12)                

h13=today+ datetime.timedelta(hours=14)
rounded_h13 = today+datetime.timedelta(hours=14)
rounded_h13_1 = rounded_h13.replace(minute=0, second=0, microsecond=0)
formatted_h13 = rounded_h13_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_h13=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_h13 in line and line.count(formatted_h13) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_h13.append(next(file).strip())
##print(found_h13)


celsius_value_h13 = [float(match.group(1)) for line in found_h13 if (match := celsius_pattern.search(line))]
wind_d_value_h13= [str(match.group(1)) for line in found_h13 if (match := wind_d_pattern.search(line))]
wind_b_value_h13 = [float(match.group(1)) for line in found_h13 if (match := wind_b_pattern.search(line))]
wind_b_h13_float_values_h13 = [item for item in wind_b_value_h13 if isinstance(item, float)]
wind_b_k_value_h13 = [item * 1.944 for item in wind_b_h13_float_values_h13]
wind_g_value_h13= [float(match.group(1)) for line in found_h13 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h13 = [item for item in wind_g_value_h13 if isinstance(item, float)]
wind_g_k_value_h13=[item * 1.944 for item in wind_g_float_values_h13]
wind_bf_value_h13= [int(match.group(1)) for line in found_h13 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h13)
#print("wind direction: ",wind_d_value_h13)
#print("wind blow in mps: ",wind_b_value_h13)
#print("wind blow in kts: ",wind_b_k_value_h13)
#print("beaufort scale: ",wind_bf_value_h13)
#print("wind gust in mps: ",wind_g_value_h13)
#print("wind gust in knots: ", wind_g_k_value_h13)

d2_h1=today+ datetime.timedelta(hours=15)
rounded_d2_h1 = today+datetime.timedelta(hours=15)
rounded_d2_h1_1 = rounded_d2_h1.replace(minute=0, second=0, microsecond=0)
formatted_d2_h1 = rounded_d2_h1_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h1=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h1 in line and line.count(formatted_d2_h1) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h1.append(next(file).strip())
##print(found_d2_h1)


celsius_value_d2_h1 = [float(match.group(1)) for line in found_d2_h1 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h1= [str(match.group(1)) for line in found_d2_h1 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h1 = [float(match.group(1)) for line in found_d2_h1 if (match := wind_b_pattern.search(line))]
wind_b_d2_h1_float_values_d2_h1 = [item for item in wind_b_value_d2_h1 if isinstance(item, float)]
wind_b_k_value_d2_h1 = [item * 1.944 for item in wind_b_d2_h1_float_values_d2_h1]
wind_g_value_d2_h1= [float(match.group(1)) for line in found_d2_h1 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h1 = [item for item in wind_g_value_d2_h1 if isinstance(item, float)]
wind_g_k_value_d2_h1=[item * 1.944 for item in wind_g_float_values_d2_h1]
wind_bf_value_d2_h1= [int(match.group(1)) for line in found_d2_h1 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h1)
#print("wind direction: ",wind_d_value_d2_h1)
#print("wind blow in mps: ",wind_b_value_d2_h1)
#print("wind blow in kts: ",wind_b_k_value_d2_h1)
#print("beaufort scale: ",wind_bf_value_d2_h1)
#print("wind gust in mps: ",wind_g_value_d2_h1)
#print("wind gust in knots: ", wind_g_k_value_d2_h1)

d2_h2=today+ datetime.timedelta(hours=16)
rounded_d2_h2 = today+datetime.timedelta(hours=16)
rounded_d2_h2_1 = rounded_d2_h2.replace(minute=0, second=0, microsecond=0)
formatted_d2_h2 = rounded_d2_h2_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h2=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h2 in line and line.count(formatted_d2_h2) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h2.append(next(file).strip())
##print(found_d2_h2)


celsius_value_d2_h2 = [float(match.group(1)) for line in found_d2_h2 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h2= [str(match.group(1)) for line in found_d2_h2 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h2 = [float(match.group(1)) for line in found_d2_h2 if (match := wind_b_pattern.search(line))]
wind_b_d2_h2_float_values_d2_h2 = [item for item in wind_b_value_d2_h2 if isinstance(item, float)]
wind_b_k_value_d2_h2 = [item * 1.944 for item in wind_b_d2_h2_float_values_d2_h2]
wind_g_value_d2_h2= [float(match.group(1)) for line in found_d2_h2 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h2 = [item for item in wind_g_value_d2_h2 if isinstance(item, float)]
wind_g_k_value_d2_h2=[item * 1.944 for item in wind_g_float_values_d2_h2]
wind_bf_value_d2_h2= [int(match.group(1)) for line in found_d2_h2 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h2)
#print("wind direction: ",wind_d_value_d2_h2)
#print("wind blow in mps: ",wind_b_value_d2_h2)
#print("wind blow in kts: ",wind_b_k_value_d2_h2)
#print("beaufort scale: ",wind_bf_value_d2_h2)
#print("wind gust in mps: ",wind_g_value_d2_h2)
#print("wind gust in knots: ", wind_g_k_value_d2_h2)

d2_h3=today+ datetime.timedelta(hours=17)
rounded_d2_h3 = today+datetime.timedelta(hours=17)
rounded_d2_h3_1 = rounded_d2_h3.replace(minute=0, second=0, microsecond=0)
formatted_d2_h3 = rounded_d2_h3_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h3=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h3 in line and line.count(formatted_d2_h3) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h3.append(next(file).strip())
##print(found_d2_h3)
                

celsius_value_d2_h3 = [float(match.group(1)) for line in found_d2_h3 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h3= [str(match.group(1)) for line in found_d2_h3 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h3 = [float(match.group(1)) for line in found_d2_h3 if (match := wind_b_pattern.search(line))]
wind_b_d2_h3_float_values_d2_h3 = [item for item in wind_b_value_d2_h3 if isinstance(item, float)]
wind_b_k_value_d2_h3 = [item * 1.944 for item in wind_b_d2_h3_float_values_d2_h3]
wind_g_value_d2_h3= [float(match.group(1)) for line in found_d2_h3 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h3 = [item for item in wind_g_value_d2_h3 if isinstance(item, float)]
wind_g_k_value_d2_h3=[item * 1.944 for item in wind_g_float_values_d2_h3]
wind_bf_value_d2_h3= [int(match.group(1)) for line in found_d2_h3 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h3)
#print("wind direction: ",wind_d_value_d2_h3)
#print("wind blow in mps: ",wind_b_value_d2_h3)
#print("wind blow in kts: ",wind_b_k_value_d2_h3)
#print("beaufort scale: ",wind_bf_value_d2_h3)
#print("wind gust in mps: ",wind_g_value_d2_h3)
#print("wind gust in knots: ", wind_g_k_value_d2_h3)                
                
d2_h4=today+ datetime.timedelta(hours=47)
rounded_d2_h4 = today+datetime.timedelta(hours=47)
rounded_d2_h4_1 = rounded_d2_h4.replace(minute=0, second=0, microsecond=0)
formatted_d2_h4 = rounded_d2_h4_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h4=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h4 in line and line.count(formatted_d2_h4) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h4.append(next(file).strip())
##print(found_d2_h4)


celsius_value_d2_h4 = [float(match.group(1)) for line in found_d2_h4 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h4= [str(match.group(1)) for line in found_d2_h4 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h4 = [float(match.group(1)) for line in found_d2_h4 if (match := wind_b_pattern.search(line))]
wind_b_d2_h4_float_values_d2_h4 = [item for item in wind_b_value_d2_h4 if isinstance(item, float)]
wind_b_k_value_d2_h4 = [item * 1.944 for item in wind_b_d2_h4_float_values_d2_h4]
wind_g_value_d2_h4= [float(match.group(1)) for line in found_d2_h4 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h4 = [item for item in wind_g_value_d2_h4 if isinstance(item, float)]
wind_g_k_value_d2_h4=[item * 1.944 for item in wind_g_float_values_d2_h4]
wind_bf_value_d2_h4= [int(match.group(1)) for line in found_d2_h4 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h4)
#print("wind direction: ",wind_d_value_d2_h4)
#print("wind blow in mps: ",wind_b_value_d2_h4)
#print("wind blow in kts: ",wind_b_k_value_d2_h4)
#print("beaufort scale: ",wind_bf_value_d2_h4)
#print("wind gust in mps: ",wind_g_value_d2_h4)
#print("wind gust in knots: ", wind_g_k_value_d2_h4)

d2_h5=today+ datetime.timedelta(hours=19)
rounded_d2_h5 = today+datetime.timedelta(hours=19)
rounded_d2_h5_1 = rounded_d2_h5.replace(minute=0, second=0, microsecond=0)
formatted_d2_h5 = rounded_d2_h5_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h5=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h5 in line and line.count(formatted_d2_h5) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h5.append(next(file).strip())
##print(found_d2_h5)


celsius_value_d2_h5 = [float(match.group(1)) for line in found_d2_h5 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h5= [str(match.group(1)) for line in found_d2_h5 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h5 = [float(match.group(1)) for line in found_d2_h5 if (match := wind_b_pattern.search(line))]
wind_b_d2_h5_float_values_d2_h5 = [item for item in wind_b_value_d2_h5 if isinstance(item, float)]
wind_b_k_value_d2_h5 = [item * 1.944 for item in wind_b_d2_h5_float_values_d2_h5]
wind_g_value_d2_h5= [float(match.group(1)) for line in found_d2_h5 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h5 = [item for item in wind_g_value_d2_h5 if isinstance(item, float)]
wind_g_k_value_d2_h5=[item * 1.944 for item in wind_g_float_values_d2_h5]
wind_bf_value_d2_h5= [int(match.group(1)) for line in found_d2_h5 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h5)
#print("wind direction: ",wind_d_value_d2_h5)
#print("wind blow in mps: ",wind_b_value_d2_h5)
#print("wind blow in kts: ",wind_b_k_value_d2_h5)
#print("beaufort scale: ",wind_bf_value_d2_h5)
#print("wind gust in mps: ",wind_g_value_d2_h5)
#print("wind gust in knots: ", wind_g_k_value_d2_h5)

d2_h6=today+ datetime.timedelta(hours=20)
rounded_d2_h6 = today+datetime.timedelta(hours=20)
rounded_d2_h6_1 = rounded_d2_h6.replace(minute=0, second=0, microsecond=0)
formatted_d2_h6 = rounded_d2_h6_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h6=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h6 in line and line.count(formatted_d2_h6) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h6.append(next(file).strip())
##print(found_d2_h6)


celsius_value_d2_h6 = [float(match.group(1)) for line in found_d2_h6 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h6= [str(match.group(1)) for line in found_d2_h6 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h6 = [float(match.group(1)) for line in found_d2_h6 if (match := wind_b_pattern.search(line))]
wind_b_d2_h6_float_values_d2_h6 = [item for item in wind_b_value_d2_h6 if isinstance(item, float)]
wind_b_k_value_d2_h6 = [item * 1.944 for item in wind_b_d2_h6_float_values_d2_h6]
wind_g_value_d2_h6= [float(match.group(1)) for line in found_d2_h6 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h6 = [item for item in wind_g_value_d2_h6 if isinstance(item, float)]
wind_g_k_value_d2_h6=[item * 1.944 for item in wind_g_float_values_d2_h6]
wind_bf_value_d2_h6= [int(match.group(1)) for line in found_d2_h6 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h6)
#print("wind direction: ",wind_d_value_d2_h6)
#print("wind blow in mps: ",wind_b_value_d2_h6)
#print("wind blow in kts: ",wind_b_k_value_d2_h6)
#print("beaufort scale: ",wind_bf_value_d2_h6)
#print("wind gust in mps: ",wind_g_value_d2_h6)
#print("wind gust in knots: ", wind_g_k_value_d2_h6)

d2_h7=today+ datetime.timedelta(hours=21)
rounded_d2_h7 = today+datetime.timedelta(hours=21)
rounded_d2_h7_1 = rounded_d2_h7.replace(minute=0, second=0, microsecond=0)
formatted_d2_h7 = rounded_d2_h7_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h7=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h7 in line and line.count(formatted_d2_h7) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h7.append(next(file).strip())
##print(found_d2_h7)


celsius_value_d2_h7 = [float(match.group(1)) for line in found_d2_h7 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h7= [str(match.group(1)) for line in found_d2_h7 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h7 = [float(match.group(1)) for line in found_d2_h7 if (match := wind_b_pattern.search(line))]
wind_b_d2_h7_float_values_d2_h7 = [item for item in wind_b_value_d2_h7 if isinstance(item, float)]
wind_b_k_value_d2_h7 = [item * 1.944 for item in wind_b_d2_h7_float_values_d2_h7]
wind_g_value_d2_h7= [float(match.group(1)) for line in found_d2_h7 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h7 = [item for item in wind_g_value_d2_h7 if isinstance(item, float)]
wind_g_k_value_d2_h7=[item * 1.944 for item in wind_g_float_values_d2_h7]
wind_bf_value_d2_h7= [int(match.group(1)) for line in found_d2_h7 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h7)
#print("wind direction: ",wind_d_value_d2_h7)
#print("wind blow in mps: ",wind_b_value_d2_h7)
#print("wind blow in kts: ",wind_b_k_value_d2_h7)
#print("beaufort scale: ",wind_bf_value_d2_h7)
#print("wind gust in mps: ",wind_g_value_d2_h7)
#print("wind gust in knots: ", wind_g_k_value_d2_h7)

d2_h8=today+ datetime.timedelta(hours=22)
rounded_d2_h8 = today+datetime.timedelta(hours=22)
rounded_d2_h8_1 = rounded_d2_h8.replace(minute=0, second=0, microsecond=0)
formatted_d2_h8 = rounded_d2_h8_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h8=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h8 in line and line.count(formatted_d2_h8) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h8.append(next(file).strip())
##print(found_d2_h8)


celsius_value_d2_h8 = [float(match.group(1)) for line in found_d2_h8 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h8= [str(match.group(1)) for line in found_d2_h8 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h8 = [float(match.group(1)) for line in found_d2_h8 if (match := wind_b_pattern.search(line))]
wind_b_d2_h8_float_values_d2_h8 = [item for item in wind_b_value_d2_h8 if isinstance(item, float)]
wind_b_k_value_d2_h8 = [item * 1.944 for item in wind_b_d2_h8_float_values_d2_h8]
wind_g_value_d2_h8= [float(match.group(1)) for line in found_d2_h8 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h8 = [item for item in wind_g_value_d2_h8 if isinstance(item, float)]
wind_g_k_value_d2_h8=[item * 1.944 for item in wind_g_float_values_d2_h8]
wind_bf_value_d2_h8= [int(match.group(1)) for line in found_d2_h8 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h8)
#print("wind direction: ",wind_d_value_d2_h8)
#print("wind blow in mps: ",wind_b_value_d2_h8)
#print("wind blow in kts: ",wind_b_k_value_d2_h8)
#print("beaufort scale: ",wind_bf_value_d2_h8)
#print("wind gust in mps: ",wind_g_value_d2_h8)
#print("wind gust in knots: ", wind_g_k_value_d2_h8)

d2_h9=today+ datetime.timedelta(hours=23)
rounded_d2_h9 = today+datetime.timedelta(hours=23)
rounded_d2_h9_1 = rounded_d2_h9.replace(minute=0, second=0, microsecond=0)
formatted_d2_h9 = rounded_d2_h9_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h9=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h9 in line and line.count(formatted_d2_h9) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h9.append(next(file).strip())
##print(found_d2_h9)
    

celsius_value_d2_h9 = [float(match.group(1)) for line in found_d2_h9 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h9= [str(match.group(1)) for line in found_d2_h9 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h9 = [float(match.group(1)) for line in found_d2_h9 if (match := wind_b_pattern.search(line))]
wind_b_d2_h9_float_values_d2_h9 = [item for item in wind_b_value_d2_h9 if isinstance(item, float)]
wind_b_k_value_d2_h9 = [item * 1.944 for item in wind_b_d2_h9_float_values_d2_h9]
wind_g_value_d2_h9= [float(match.group(1)) for line in found_d2_h9 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h9 = [item for item in wind_g_value_d2_h9 if isinstance(item, float)]
wind_g_k_value_d2_h9=[item * 1.944 for item in wind_g_float_values_d2_h9]
wind_bf_value_d2_h9= [int(match.group(1)) for line in found_d2_h9 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h9)
#print("wind direction: ",wind_d_value_d2_h9)
#print("wind blow in mps: ",wind_b_value_d2_h9)
#print("wind blow in kts: ",wind_b_k_value_d2_h9)
#print("beaufort scale: ",wind_bf_value_d2_h9)
#print("wind gust in mps: ",wind_g_value_d2_h9)
#print("wind gust in knots: ", wind_g_k_value_d2_h9)

d2_h10=today+ datetime.timedelta(hours=24)
rounded_d2_h10 = today+datetime.timedelta(hours=24)
rounded_d2_h10_1 = rounded_d2_h10.replace(minute=0, second=0, microsecond=0)
formatted_d2_h10 = rounded_d2_h10_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h10=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h10 in line and line.count(formatted_d2_h10) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h10.append(next(file).strip())
##print(found_d2_h10)
    

celsius_value_d2_h10 = [float(match.group(1)) for line in found_d2_h10 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h10= [str(match.group(1)) for line in found_d2_h10 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h10 = [float(match.group(1)) for line in found_d2_h10 if (match := wind_b_pattern.search(line))]
wind_b_d2_h10_float_values_d2_h10 = [item for item in wind_b_value_d2_h10 if isinstance(item, float)]
wind_b_k_value_d2_h10 = [item * 1.944 for item in wind_b_d2_h10_float_values_d2_h10]
wind_g_value_d2_h10= [float(match.group(1)) for line in found_d2_h10 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h10 = [item for item in wind_g_value_d2_h10 if isinstance(item, float)]
wind_g_k_value_d2_h10=[item * 1.944 for item in wind_g_float_values_d2_h10]
wind_bf_value_d2_h10= [int(match.group(1)) for line in found_d2_h10 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h10)
#print("wind direction: ",wind_d_value_d2_h10)
#print("wind blow in mps: ",wind_b_value_d2_h10)
#print("wind blow in kts: ",wind_b_k_value_d2_h10)
#print("beaufort scale: ",wind_bf_value_d2_h10)
#print("wind gust in mps: ",wind_g_value_d2_h10)
#print("wind gust in knots: ", wind_g_k_value_d2_h10)

d2_h11=today+ datetime.timedelta(hours=25)
rounded_d2_h11 = today+datetime.timedelta(hours=25)
rounded_d2_h11_1 = rounded_d2_h11.replace(minute=0, second=0, microsecond=0)
formatted_d2_h11 = rounded_d2_h11_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h11=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h11 in line and line.count(formatted_d2_h11) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h11.append(next(file).strip())
##print(found_d2_h11)
    

celsius_value_d2_h11 = [float(match.group(1)) for line in found_d2_h11 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h11= [str(match.group(1)) for line in found_d2_h11 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h11 = [float(match.group(1)) for line in found_d2_h11 if (match := wind_b_pattern.search(line))]
wind_b_d2_h11_float_values_d2_h11 = [item for item in wind_b_value_d2_h11 if isinstance(item, float)]
wind_b_k_value_d2_h11 = [item * 1.944 for item in wind_b_d2_h11_float_values_d2_h11]
wind_g_value_d2_h11= [float(match.group(1)) for line in found_d2_h11 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h11 = [item for item in wind_g_value_d2_h11 if isinstance(item, float)]
wind_g_k_value_d2_h11=[item * 1.944 for item in wind_g_float_values_d2_h11]
wind_bf_value_d2_h11= [int(match.group(1)) for line in found_d2_h11 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h11)
#print("wind direction: ",wind_d_value_d2_h11)
#print("wind blow in mps: ",wind_b_value_d2_h11)
#print("wind blow in kts: ",wind_b_k_value_d2_h11)
#print("beaufort scale: ",wind_bf_value_d2_h11)
#print("wind gust in mps: ",wind_g_value_d2_h11)
#print("wind gust in knots: ", wind_g_k_value_d2_h11)

d2_h12=today+ datetime.timedelta(hours=26)
rounded_d2_h12 = today+datetime.timedelta(hours=26)
rounded_d2_h12_1 = rounded_d2_h12.replace(minute=0, second=0, microsecond=0)
formatted_d2_h12 = rounded_d2_h12_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h12=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h12 in line and line.count(formatted_d2_h12) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h12.append(next(file).strip())
##print(found_d2_h12)
    

celsius_value_d2_h12 = [float(match.group(1)) for line in found_d2_h12 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h12= [str(match.group(1)) for line in found_d2_h12 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h12 = [float(match.group(1)) for line in found_d2_h12 if (match := wind_b_pattern.search(line))]
wind_b_d2_h12_float_values_d2_h12 = [item for item in wind_b_value_d2_h12 if isinstance(item, float)]
wind_b_k_value_d2_h12 = [item * 1.944 for item in wind_b_d2_h12_float_values_d2_h12]
wind_g_value_d2_h12= [float(match.group(1)) for line in found_d2_h12 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h12 = [item for item in wind_g_value_d2_h12 if isinstance(item, float)]
wind_g_k_value_d2_h12=[item * 1.944 for item in wind_g_float_values_d2_h12]
wind_bf_value_d2_h12= [int(match.group(1)) for line in found_d2_h12 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h12)
#print("wind direction: ",wind_d_value_d2_h12)
#print("wind blow in mps: ",wind_b_value_d2_h12)
#print("wind blow in kts: ",wind_b_k_value_d2_h12)
#print("beaufort scale: ",wind_bf_value_d2_h12)
#print("wind gust in mps: ",wind_g_value_d2_h12)
#print("wind gust in knots: ", wind_g_k_value_d2_h12)

d2_h13=today+ datetime.timedelta(hours=27)
rounded_d2_h13 = today+datetime.timedelta(hours=27)
rounded_d2_h13_1 = rounded_d2_h13.replace(minute=0, second=0, microsecond=0)
formatted_d2_h13 = rounded_d2_h13_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h13=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h13 in line and line.count(formatted_d2_h13) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h13.append(next(file).strip())
##print(found_d2_h13)

celsius_value_d2_h13 = [float(match.group(1)) for line in found_d2_h13 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h13= [str(match.group(1)) for line in found_d2_h13 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h13 = [float(match.group(1)) for line in found_d2_h13 if (match := wind_b_pattern.search(line))]
wind_b_d2_h13_float_values_d2_h13 = [item for item in wind_b_value_d2_h13 if isinstance(item, float)]
wind_b_k_value_d2_h13 = [item * 1.944 for item in wind_b_d2_h13_float_values_d2_h13]
wind_g_value_d2_h13= [float(match.group(1)) for line in found_d2_h13 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h13 = [item for item in wind_g_value_d2_h13 if isinstance(item, float)]
wind_g_k_value_d2_h13=[item * 1.944 for item in wind_g_float_values_d2_h13]
wind_bf_value_d2_h13= [int(match.group(1)) for line in found_d2_h13 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h13)
#print("wind direction: ",wind_d_value_d2_h13)
#print("wind blow in mps: ",wind_b_value_d2_h13)
#print("wind blow in kts: ",wind_b_k_value_d2_h13)
#print("beaufort scale: ",wind_bf_value_d2_h13)
#print("wind gust in mps: ",wind_g_value_d2_h13)
#print("wind gust in knots: ", wind_g_k_value_d2_h13)

d2_h14=today+ datetime.timedelta(hours=28)
rounded_d2_h14 = today+datetime.timedelta(hours=28)
rounded_d2_h14_1 = rounded_d2_h14.replace(minute=0, second=0, microsecond=0)
formatted_d2_h14 = rounded_d2_h14_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h14=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h14 in line and line.count(formatted_d2_h14) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h14.append(next(file).strip())
##print(found_d2_h14)


celsius_value_h2 = [float(match.group(1)) for line in found_h2 if (match := celsius_pattern.search(line))]
wind_d_value_h2= [str(match.group(1)) for line in found_h2 if (match := wind_d_pattern.search(line))]
wind_b_value_h2 = [float(match.group(1)) for line in found_h2 if (match := wind_b_pattern.search(line))]
wind_b_h2_float_values_h2 = [item for item in wind_b_value_h2 if isinstance(item, float)]
wind_b_k_value_h2 = [item * 1.944 for item in wind_b_h2_float_values_h2]
wind_g_value_h2= [float(match.group(1)) for line in found_h2 if (match := wind_g_pattern.search(line))]
wind_g_float_values_h2 = [item for item in wind_g_value_h2 if isinstance(item, float)]
wind_g_k_value_h2=[item * 1.944 for item in wind_g_float_values_h2]
wind_bf_value_h2= [int(match.group(1)) for line in found_h2 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_h2)
#print("wind direction: ",wind_d_value_h2)
#print("wind blow in mps: ",wind_b_value_h2)
#print("wind blow in kts: ",wind_b_k_value_h2)
#print("beaufort scale: ",wind_bf_value_h2)
#print("wind gust in mps: ",wind_g_value_h2)
#print("wind gust in knots: ", wind_g_k_value_h2)

d2_h14=today+ datetime.timedelta(hours=29)
rounded_d2_h14 = today+datetime.timedelta(hours=29)
rounded_d2_h14_1 = rounded_d2_h14.replace(minute=0, second=0, microsecond=0)
formatted_d2_h14 = rounded_d2_h14_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h14=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h14 in line and line.count(formatted_d2_h14) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h14.append(next(file).strip())
##print(found_d2_h14)
    

celsius_value_d2_h14 = [float(match.group(1)) for line in found_d2_h14 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h14= [str(match.group(1)) for line in found_d2_h14 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h14 = [float(match.group(1)) for line in found_d2_h14 if (match := wind_b_pattern.search(line))]
wind_b_d2_h14_float_values_d2_h14 = [item for item in wind_b_value_d2_h14 if isinstance(item, float)]
wind_b_k_value_d2_h14 = [item * 1.944 for item in wind_b_d2_h14_float_values_d2_h14]
wind_g_value_d2_h14= [float(match.group(1)) for line in found_d2_h14 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h14 = [item for item in wind_g_value_d2_h14 if isinstance(item, float)]
wind_g_k_value_d2_h14=[item * 1.944 for item in wind_g_float_values_d2_h14]
wind_bf_value_d2_h14= [int(match.group(1)) for line in found_d2_h14 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h14)
#print("wind direction: ",wind_d_value_d2_h14)
#print("wind blow in mps: ",wind_b_value_d2_h14)
#print("wind blow in kts: ",wind_b_k_value_d2_h14)
#print("beaufort scale: ",wind_bf_value_d2_h14)
#print("wind gust in mps: ",wind_g_value_d2_h14)
#print("wind gust in knots: ", wind_g_k_value_d2_h14)

d2_h15=today+ datetime.timedelta(hours=30)
rounded_d2_h15 = today+datetime.timedelta(hours=30)
rounded_d2_h15_1 = rounded_d2_h15.replace(minute=0, second=0, microsecond=0)
formatted_d2_h15 = rounded_d2_h15_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h15=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h15 in line and line.count(formatted_d2_h15) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h15.append(next(file).strip())
##print(found_d2_h15)


celsius_value_d2_h15 = [float(match.group(1)) for line in found_d2_h15 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h15= [str(match.group(1)) for line in found_d2_h15 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h15 = [float(match.group(1)) for line in found_d2_h15 if (match := wind_b_pattern.search(line))]
wind_b_d2_h15_float_values_d2_h15 = [item for item in wind_b_value_d2_h15 if isinstance(item, float)]
wind_b_k_value_d2_h15 = [item * 1.944 for item in wind_b_d2_h15_float_values_d2_h15]
wind_g_value_d2_h15= [float(match.group(1)) for line in found_d2_h15 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h15 = [item for item in wind_g_value_d2_h15 if isinstance(item, float)]
wind_g_k_value_d2_h15=[item * 1.944 for item in wind_g_float_values_d2_h15]
wind_bf_value_d2_h15= [int(match.group(1)) for line in found_d2_h15 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h15)
#print("wind direction: ",wind_d_value_d2_h15)
#print("wind blow in mps: ",wind_b_value_d2_h15)
#print("wind blow in kts: ",wind_b_k_value_d2_h15)
#print("beaufort scale: ",wind_bf_value_d2_h15)
#print("wind gust in mps: ",wind_g_value_d2_h15)
#print("wind gust in knots: ", wind_g_k_value_d2_h15)

d2_h16=today+ datetime.timedelta(hours=31)
rounded_d2_h16 = today+datetime.timedelta(hours=31)
rounded_d2_h16_1 = rounded_d2_h16.replace(minute=0, second=0, microsecond=0)
formatted_d2_h16 = rounded_d2_h16_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h16=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h16 in line and line.count(formatted_d2_h16) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h16.append(next(file).strip())
##print(found_d2_h16)


celsius_value_d2_h16 = [float(match.group(1)) for line in found_d2_h16 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h16= [str(match.group(1)) for line in found_d2_h16 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h16 = [float(match.group(1)) for line in found_d2_h16 if (match := wind_b_pattern.search(line))]
wind_b_d2_h16_float_values_d2_h16 = [item for item in wind_b_value_d2_h16 if isinstance(item, float)]
wind_b_k_value_d2_h16 = [item * 1.944 for item in wind_b_d2_h16_float_values_d2_h16]
wind_g_value_d2_h16= [float(match.group(1)) for line in found_d2_h16 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h16 = [item for item in wind_g_value_d2_h16 if isinstance(item, float)]
wind_g_k_value_d2_h16=[item * 1.944 for item in wind_g_float_values_d2_h16]
wind_bf_value_d2_h16= [int(match.group(1)) for line in found_d2_h16 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h16)
#print("wind direction: ",wind_d_value_d2_h16)
#print("wind blow in mps: ",wind_b_value_d2_h16)
#print("wind blow in kts: ",wind_b_k_value_d2_h16)
#print("beaufort scale: ",wind_bf_value_d2_h16)
#print("wind gust in mps: ",wind_g_value_d2_h16)
#print("wind gust in knots: ", wind_g_k_value_d2_h16)

d2_h17=today+ datetime.timedelta(hours=32)
rounded_d2_h17 = today+datetime.timedelta(hours=32)
rounded_d2_h17_1 = rounded_d2_h17.replace(minute=0, second=0, microsecond=0)
formatted_d2_h17 = rounded_d2_h17_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h17=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h17 in line and line.count(formatted_d2_h17) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h17.append(next(file).strip())
##print(found_d2_h17)


celsius_value_d2_h17 = [float(match.group(1)) for line in found_d2_h17 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h17= [str(match.group(1)) for line in found_d2_h17 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h17 = [float(match.group(1)) for line in found_d2_h17 if (match := wind_b_pattern.search(line))]
wind_b_d2_h17_float_values_d2_h17 = [item for item in wind_b_value_d2_h17 if isinstance(item, float)]
wind_b_k_value_d2_h17 = [item * 1.944 for item in wind_b_d2_h17_float_values_d2_h17]
wind_g_value_d2_h17= [float(match.group(1)) for line in found_d2_h17 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h17 = [item for item in wind_g_value_d2_h17 if isinstance(item, float)]
wind_g_k_value_d2_h17=[item * 1.944 for item in wind_g_float_values_d2_h17]
wind_bf_value_d2_h17= [int(match.group(1)) for line in found_d2_h17 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h17)
#print("wind direction: ",wind_d_value_d2_h17)
#print("wind blow in mps: ",wind_b_value_d2_h17)
#print("wind blow in kts: ",wind_b_k_value_d2_h17)
#print("beaufort scale: ",wind_bf_value_d2_h17)
#print("wind gust in mps: ",wind_g_value_d2_h17)
#print("wind gust in knots: ", wind_g_k_value_d2_h17)

d2_h18=today+ datetime.timedelta(hours=33)
rounded_d2_h18 = today+datetime.timedelta(hours=33)
rounded_d2_h18_1 = rounded_d2_h18.replace(minute=0, second=0, microsecond=0)
formatted_d2_h18 = rounded_d2_h18_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h18=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h18 in line and line.count(formatted_d2_h18) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h18.append(next(file).strip())
##print(found_d2_h18)

 
celsius_value_d2_h18 = [float(match.group(1)) for line in found_d2_h18 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h18= [str(match.group(1)) for line in found_d2_h18 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h18 = [float(match.group(1)) for line in found_d2_h18 if (match := wind_b_pattern.search(line))]
wind_b_d2_h18_float_values_d2_h18 = [item for item in wind_b_value_d2_h18 if isinstance(item, float)]
wind_b_k_value_d2_h18 = [item * 1.944 for item in wind_b_d2_h18_float_values_d2_h18]
wind_g_value_d2_h18= [float(match.group(1)) for line in found_d2_h18 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h18 = [item for item in wind_g_value_d2_h18 if isinstance(item, float)]
wind_g_k_value_d2_h18=[item * 1.944 for item in wind_g_float_values_d2_h18]
wind_bf_value_d2_h18= [int(match.group(1)) for line in found_d2_h18 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h18)
#print("wind direction: ",wind_d_value_d2_h18)
#print("wind blow in mps: ",wind_b_value_d2_h18)
#print("wind blow in kts: ",wind_b_k_value_d2_h18)
#print("beaufort scale: ",wind_bf_value_d2_h18)
#print("wind gust in mps: ",wind_g_value_d2_h18)
#print("wind gust in knots: ", wind_g_k_value_d2_h18)

d2_h19=today+ datetime.timedelta(hours=34)
rounded_d2_h19 = today+datetime.timedelta(hours=34)
rounded_d2_h19_1 = rounded_d2_h19.replace(minute=0, second=0, microsecond=0)
formatted_d2_h19 = rounded_d2_h19_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h19=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h19 in line and line.count(formatted_d2_h19) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h19.append(next(file).strip())
##print(found_d2_h19)


celsius_value_d2_h19 = [float(match.group(1)) for line in found_d2_h19 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h19= [str(match.group(1)) for line in found_d2_h19 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h19 = [float(match.group(1)) for line in found_d2_h19 if (match := wind_b_pattern.search(line))]
wind_b_d2_h19_float_values_d2_h19 = [item for item in wind_b_value_d2_h19 if isinstance(item, float)]
wind_b_k_value_d2_h19 = [item * 1.944 for item in wind_b_d2_h19_float_values_d2_h19]
wind_g_value_d2_h19= [float(match.group(1)) for line in found_d2_h19 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h19 = [item for item in wind_g_value_d2_h19 if isinstance(item, float)]
wind_g_k_value_d2_h19=[item * 1.944 for item in wind_g_float_values_d2_h19]
wind_bf_value_d2_h19= [int(match.group(1)) for line in found_d2_h19 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h19)
#print("wind direction: ",wind_d_value_d2_h19)
#print("wind blow in mps: ",wind_b_value_d2_h19)
#print("wind blow in kts: ",wind_b_k_value_d2_h19)
#print("beaufort scale: ",wind_bf_value_d2_h19)
#print("wind gust in mps: ",wind_g_value_d2_h19)
#print("wind gust in knots: ", wind_g_k_value_d2_h19)

d2_h20=today+ datetime.timedelta(hours=34)
rounded_d2_h20 = today+datetime.timedelta(hours=34)
rounded_d2_h20_1 = rounded_d2_h20.replace(minute=0, second=0, microsecond=0)
formatted_d2_h20 = rounded_d2_h20_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h20=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h20 in line and line.count(formatted_d2_h20) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h20.append(next(file).strip())
##print(found_d2_h20)


celsius_value_d2_h20 = [float(match.group(1)) for line in found_d2_h20 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h20= [str(match.group(1)) for line in found_d2_h20 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h20 = [float(match.group(1)) for line in found_d2_h20 if (match := wind_b_pattern.search(line))]
wind_b_d2_h20_float_values_d2_h20 = [item for item in wind_b_value_d2_h20 if isinstance(item, float)]
wind_b_k_value_d2_h20 = [item * 1.944 for item in wind_b_d2_h20_float_values_d2_h20]
wind_g_value_d2_h20= [float(match.group(1)) for line in found_d2_h20 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h20 = [item for item in wind_g_value_d2_h20 if isinstance(item, float)]
wind_g_k_value_d2_h20=[item * 1.944 for item in wind_g_float_values_d2_h20]
wind_bf_value_d2_h20= [int(match.group(1)) for line in found_d2_h20 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h20)
#print("wind direction: ",wind_d_value_d2_h20)
#print("wind blow in mps: ",wind_b_value_d2_h20)
#print("wind blow in kts: ",wind_b_k_value_d2_h20)
#print("beaufort scale: ",wind_bf_value_d2_h20)
#print("wind gust in mps: ",wind_g_value_d2_h20)
#print("wind gust in knots: ", wind_g_k_value_d2_h20)

d2_h21=today+ datetime.timedelta(hours=35)
rounded_d2_h21 = today+datetime.timedelta(hours=35)
rounded_d2_h21_1 = rounded_d2_h21.replace(minute=0, second=0, microsecond=0)
formatted_d2_h21 = rounded_d2_h21_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h21=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h21 in line and line.count(formatted_d2_h21) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h21.append(next(file).strip())
##print(found_d2_h21)


celsius_value_d2_h21 = [float(match.group(1)) for line in found_d2_h21 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h21= [str(match.group(1)) for line in found_d2_h21 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h21 = [float(match.group(1)) for line in found_d2_h21 if (match := wind_b_pattern.search(line))]
wind_b_d2_h21_float_values_d2_h21 = [item for item in wind_b_value_d2_h21 if isinstance(item, float)]
wind_b_k_value_d2_h21 = [item * 1.944 for item in wind_b_d2_h21_float_values_d2_h21]
wind_g_value_d2_h21= [float(match.group(1)) for line in found_d2_h21 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h21 = [item for item in wind_g_value_d2_h21 if isinstance(item, float)]
wind_g_k_value_d2_h21=[item * 1.944 for item in wind_g_float_values_d2_h21]
wind_bf_value_d2_h21= [int(match.group(1)) for line in found_d2_h21 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h21)
#print("wind direction: ",wind_d_value_d2_h21)
#print("wind blow in mps: ",wind_b_value_d2_h21)
#print("wind blow in kts: ",wind_b_k_value_d2_h21)
#print("beaufort scale: ",wind_bf_value_d2_h21)
#print("wind gust in mps: ",wind_g_value_d2_h21)
#print("wind gust in knots: ", wind_g_k_value_d2_h21)

d2_h22=today+ datetime.timedelta(hours=36)
rounded_d2_h22 = today+datetime.timedelta(hours=36)
rounded_d2_h22_1 = rounded_d2_h22.replace(minute=0, second=0, microsecond=0)
formatted_d2_h22 = rounded_d2_h22_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h22=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h22 in line and line.count(formatted_d2_h22) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h22.append(next(file).strip())
##print(found_d2_h22)

celsius_value_d2_h22 = [float(match.group(1)) for line in found_d2_h22 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h22= [str(match.group(1)) for line in found_d2_h22 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h22 = [float(match.group(1)) for line in found_d2_h22 if (match := wind_b_pattern.search(line))]
wind_b_d2_h22_float_values_d2_h22 = [item for item in wind_b_value_d2_h22 if isinstance(item, float)]
wind_b_k_value_d2_h22 = [item * 1.944 for item in wind_b_d2_h22_float_values_d2_h22]
wind_g_value_d2_h22= [float(match.group(1)) for line in found_d2_h22 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h22 = [item for item in wind_g_value_d2_h22 if isinstance(item, float)]
wind_g_k_value_d2_h22=[item * 1.944 for item in wind_g_float_values_d2_h22]
wind_bf_value_d2_h22= [int(match.group(1)) for line in found_d2_h22 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h22)
#print("wind direction: ",wind_d_value_d2_h22)
#print("wind blow in mps: ",wind_b_value_d2_h22)
#print("wind blow in kts: ",wind_b_k_value_d2_h22)
#print("beaufort scale: ",wind_bf_value_d2_h22)
#print("wind gust in mps: ",wind_g_value_d2_h22)
#print("wind gust in knots: ", wind_g_k_value_d2_h22)

d2_h23=today+ datetime.timedelta(hours=37)
rounded_d2_h23 = today+datetime.timedelta(hours=37)
rounded_d2_h23_1 = rounded_d2_h23.replace(minute=0, second=0, microsecond=0)
formatted_d2_h23 = rounded_d2_h23_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h23=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h23 in line and line.count(formatted_d2_h23) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h23.append(next(file).strip())
##print(found_d2_h23)


celsius_value_d2_h23 = [float(match.group(1)) for line in found_d2_h23 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h23= [str(match.group(1)) for line in found_d2_h23 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h23 = [float(match.group(1)) for line in found_d2_h23 if (match := wind_b_pattern.search(line))]
wind_b_d2_h23_float_values_d2_h23 = [item for item in wind_b_value_d2_h23 if isinstance(item, float)]
wind_b_k_value_d2_h23 = [item * 1.944 for item in wind_b_d2_h23_float_values_d2_h23]
wind_g_value_d2_h23= [float(match.group(1)) for line in found_d2_h23 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h23 = [item for item in wind_g_value_d2_h23 if isinstance(item, float)]
wind_g_k_value_d2_h23=[item * 1.944 for item in wind_g_float_values_d2_h23]
wind_bf_value_d2_h23= [int(match.group(1)) for line in found_d2_h23 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h23)
#print("wind direction: ",wind_d_value_d2_h23)
#print("wind blow in mps: ",wind_b_value_d2_h23)
#print("wind blow in kts: ",wind_b_k_value_d2_h23)
#print("beaufort scale: ",wind_bf_value_d2_h23)
#print("wind gust in mps: ",wind_g_value_d2_h23)
#print("wind gust in knots: ", wind_g_k_value_d2_h23)

d2_h24=today+ datetime.timedelta(hours=38)
rounded_d2_h24 = today+datetime.timedelta(hours=38)
rounded_d2_h24_1 = rounded_d2_h24.replace(minute=0, second=0, microsecond=0)
formatted_d2_h24 = rounded_d2_h24_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d2_h24=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d2_h24 in line and line.count(formatted_d2_h24) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d2_h24.append(next(file).strip())
##print(found_d2_h24)


celsius_value_d2_h24 = [float(match.group(1)) for line in found_d2_h24 if (match := celsius_pattern.search(line))]
wind_d_value_d2_h24= [str(match.group(1)) for line in found_d2_h24 if (match := wind_d_pattern.search(line))]
wind_b_value_d2_h24 = [float(match.group(1)) for line in found_d2_h24 if (match := wind_b_pattern.search(line))]
wind_b_d2_h24_float_values_d2_h24 = [item for item in wind_b_value_d2_h24 if isinstance(item, float)]
wind_b_k_value_d2_h24 = [item * 1.944 for item in wind_b_d2_h24_float_values_d2_h24]
wind_g_value_d2_h24= [float(match.group(1)) for line in found_d2_h24 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d2_h24 = [item for item in wind_g_value_d2_h24 if isinstance(item, float)]
wind_g_k_value_d2_h24=[item * 1.944 for item in wind_g_float_values_d2_h24]
wind_bf_value_d2_h24= [int(match.group(1)) for line in found_d2_h24 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d2_h24)
#print("wind direction: ",wind_d_value_d2_h24)
#print("wind blow in mps: ",wind_b_value_d2_h24)
#print("wind blow in kts: ",wind_b_k_value_d2_h24)
#print("beaufort scale: ",wind_bf_value_d2_h24)
#print("wind gust in mps: ",wind_g_value_d2_h24)
#print("wind gust in knots: ", wind_g_k_value_d2_h24)

d3_h1=today+ datetime.timedelta(hours=39)
rounded_d3_h1 = today+datetime.timedelta(hours=39)
rounded_d3_h1_1 = rounded_d3_h1.replace(minute=0, second=0, microsecond=0)
formatted_d3_h1 = rounded_d3_h1_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h1=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h1 in line and line.count(formatted_d3_h1) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h1.append(next(file).strip())
##print(found_d3_h1)
                

celsius_value_d3_h1 = [float(match.group(1)) for line in found_d3_h1 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h1= [str(match.group(1)) for line in found_d3_h1 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h1 = [float(match.group(1)) for line in found_d3_h1 if (match := wind_b_pattern.search(line))]
wind_b_d3_h1_float_values_d3_h1 = [item for item in wind_b_value_d3_h1 if isinstance(item, float)]
wind_b_k_value_d3_h1 = [item * 1.944 for item in wind_b_d3_h1_float_values_d3_h1]
wind_g_value_d3_h1= [float(match.group(1)) for line in found_d3_h1 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h1 = [item for item in wind_g_value_d3_h1 if isinstance(item, float)]
wind_g_k_value_d3_h1=[item * 1.944 for item in wind_g_float_values_d3_h1]
wind_bf_value_d3_h1= [int(match.group(1)) for line in found_d3_h1 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h1)
#print("wind direction: ",wind_d_value_d3_h1)
#print("wind blow in mps: ",wind_b_value_d3_h1)
#print("wind blow in kts: ",wind_b_k_value_d3_h1)
#print("beaufort scale: ",wind_bf_value_d3_h1)
#print("wind gust in mps: ",wind_g_value_d3_h1)
#print("wind gust in knots: ", wind_g_k_value_d3_h1)

d3_h2=today+ datetime.timedelta(hours=40)
rounded_d3_h2 = today+datetime.timedelta(hours=40)
rounded_d3_h2_1 = rounded_d3_h2.replace(minute=0, second=0, microsecond=0)
formatted_d3_h2 = rounded_d3_h2_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h2=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h2 in line and line.count(formatted_d3_h2) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h2.append(next(file).strip())
##print(found__d3_h2)


celsius_value_d3_h2 = [float(match.group(1)) for line in found_d3_h2 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h2= [str(match.group(1)) for line in found_d3_h2 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h2 = [float(match.group(1)) for line in found_d3_h2 if (match := wind_b_pattern.search(line))]
wind_b_d3_h2_float_values_d3_h2 = [item for item in wind_b_value_d3_h2 if isinstance(item, float)]
wind_b_k_value_d3_h2 = [item * 1.944 for item in wind_b_d3_h2_float_values_d3_h2]
wind_g_value_d3_h2= [float(match.group(1)) for line in found_d3_h2 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h2 = [item for item in wind_g_value_d3_h2 if isinstance(item, float)]
wind_g_k_value_d3_h2=[item * 1.944 for item in wind_g_float_values_d3_h2]
wind_bf_value_d3_h2= [int(match.group(1)) for line in found_d3_h2 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h2)
#print("wind direction: ",wind_d_value_d3_h2)
#print("wind blow in mps: ",wind_b_value_d3_h2)
#print("wind blow in kts: ",wind_b_k_value_d3_h2)
#print("beaufort scale: ",wind_bf_value_d3_h2)
#print("wind gust in mps: ",wind_g_value_d3_h2)
#print("wind gust in knots: ", wind_g_k_value_d3_h2)

d3_h3=today+ datetime.timedelta(hours=41)
rounded_d3_h3 = today+datetime.timedelta(hours=41)
rounded_d3_h3_1 = rounded_d3_h3.replace(minute=0, second=0, microsecond=0)
formatted_d3_h3 = rounded_d3_h3_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h3=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h3 in line and line.count(formatted_d3_h3) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h3.append(next(file).strip())
##print(found_d3_h3)


celsius_value_d3_h3 = [float(match.group(1)) for line in found_d3_h3 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h3= [str(match.group(1)) for line in found_d3_h3 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h3 = [float(match.group(1)) for line in found_d3_h3 if (match := wind_b_pattern.search(line))]
wind_b_d3_h3_float_values_d3_h3 = [item for item in wind_b_value_d3_h3 if isinstance(item, float)]
wind_b_k_value_d3_h3 = [item * 1.944 for item in wind_b_d3_h3_float_values_d3_h3]
wind_g_value_d3_h3= [float(match.group(1)) for line in found_d3_h3 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h3 = [item for item in wind_g_value_d3_h3 if isinstance(item, float)]
wind_g_k_value_d3_h3=[item * 1.944 for item in wind_g_float_values_d3_h3]
wind_bf_value_d3_h3= [int(match.group(1)) for line in found_d3_h3 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h3)
#print("wind direction: ",wind_d_value_d3_h3)
#print("wind blow in mps: ",wind_b_value_d3_h3)
#print("wind blow in kts: ",wind_b_k_value_d3_h3)
#print("beaufort scale: ",wind_bf_value_d3_h3)
#print("wind gust in mps: ",wind_g_value_d3_h3)
#print("wind gust in knots: ", wind_g_k_value_d3_h3) 

d3_h4=today+ datetime.timedelta(hours=42)
rounded_d3_h4 = today+datetime.timedelta(hours=42)
rounded_d3_h4_1 = rounded_d3_h4.replace(minute=0, second=0, microsecond=0)
formatted_d3_h4 = rounded_d3_h4_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h4=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h4 in line and line.count(formatted_d3_h4) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h4.append(next(file).strip())
##print(found_d3_h4)


d3_h5=today+ datetime.timedelta(hours=43)
rounded_d3_h5 = today+datetime.timedelta(hours=43)
rounded_d3_h5_1 = rounded_d3_h5.replace(minute=0, second=0, microsecond=0)
formatted_d3_h5 = rounded_d3_h5_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h5=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h5 in line and line.count(formatted_d3_h5) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h5.append(next(file).strip())
##print(found_d3_h5)

d3_h6=today+ datetime.timedelta(hours=44)
rounded_d3_h6 = today+datetime.timedelta(hours=44)
rounded_d3_h6_1 = rounded_d3_h6.replace(minute=0, second=0, microsecond=0)
formatted_d3_h6 = rounded_d3_h6_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h6=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h6 in line and line.count(formatted_d3_h6) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h6.append(next(file).strip())
##print(found_d3_h6)

d3_h7=today+ datetime.timedelta(hours=45)
rounded_d3_h7 = today+datetime.timedelta(hours=45)
rounded_d3_h7_1 = rounded_d3_h7.replace(minute=0, second=0, microsecond=0)
formatted_d3_h7 = rounded_d3_h7_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h7=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h7 in line and line.count(formatted_d3_h7) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h7.append(next(file).strip())
##print(found_d3_h7)

d3_h8=today+ datetime.timedelta(hours=46)
rounded_d3_h8 = today+datetime.timedelta(hours=46)
rounded_d3_h8_1 = rounded_d3_h8.replace(minute=0, second=0, microsecond=0)
formatted_d3_h8 = rounded_d3_h8_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h8=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h8 in line and line.count(formatted_d3_h8) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h8.append(next(file).strip())
##print(found_d3_h8)

d3_h9=today+ datetime.timedelta(hours=47)
rounded_d3_h9 = today+datetime.timedelta(hours=47)
rounded_d3_h9_1 = rounded_d3_h9.replace(minute=0, second=0, microsecond=0)
formatted_d3_h9 = rounded_d3_h9_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h9=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h9 in line and line.count(formatted_d3_h9) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h9.append(next(file).strip())
##print(found_d3_h9)

d3_h10=today+ datetime.timedelta(hours=48)
rounded_d3_h10 = today+datetime.timedelta(hours=48)
rounded_d3_h10_1 = rounded_d3_h10.replace(minute=0, second=0, microsecond=0)
formatted_d3_h10 = rounded_d3_h10_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h10=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h10 in line and line.count(formatted_d3_h10) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h10.append(next(file).strip())
##print(found_d3_h10)

d3_h11=today+ datetime.timedelta(hours=49)
rounded_d3_h11 = today+datetime.timedelta(hours=49)
rounded_d3_h11_1 = rounded_d3_h11.replace(minute=0, second=0, microsecond=0)
formatted_d3_h11 = rounded_d3_h11_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h11=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h11 in line and line.count(formatted_d3_h11) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h11.append(next(file).strip())
##print(found_d3_h11)

d3_h12=today+ datetime.timedelta(hours=50)
rounded_d3_h12 = today+datetime.timedelta(hours=50)
rounded_d3_h12_1 = rounded_d3_h12.replace(minute=0, second=0, microsecond=0)
formatted_d3_h12 = rounded_d3_h12_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h12=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h12 in line and line.count(formatted_d3_h12) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h12.append(next(file).strip())
##print(found_d3_h12)
d3_h13=today+ datetime.timedelta(hours=51)
rounded_d3_h13 = today+datetime.timedelta(hours=51)
rounded_d3_h13_1 = rounded_d3_h13.replace(minute=0, second=0, microsecond=0)
formatted_d3_h13 = rounded_d3_h13_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h13=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h13 in line and line.count(formatted_d3_h13) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h13.append(next(file).strip())
##print(found_d3_h13)
d3_h14=today+ datetime.timedelta(hours=52)
rounded_d3_h14 = today+datetime.timedelta(hours=52)
rounded_d3_h14_1 = rounded_d3_h14.replace(minute=0, second=0, microsecond=0)
formatted_d3_h14 = rounded_d3_h14_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h14=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h14 in line and line.count(formatted_d3_h14) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h14.append(next(file).strip())
##print(found_d3_h14)
d3_h15=today+ datetime.timedelta(hours=53)
rounded_d3_h15 = today+datetime.timedelta(hours=53)
rounded_d3_h15_1 = rounded_d3_h15.replace(minute=0, second=0, microsecond=0)
formatted_d3_h15 = rounded_d3_h15_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h15=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h15 in line and line.count(formatted_d3_h15) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h15.append(next(file).strip())
##print(found_d3_h15)
                
celsius_value_d3_h15 = [float(match.group(1)) for line in found_d3_h15 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h15= [str(match.group(1)) for line in found_d3_h15 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h15 = [float(match.group(1)) for line in found_d3_h15 if (match := wind_b_pattern.search(line))]
wind_b_d3_h15_float_values_d3_h15 = [item for item in wind_b_value_d3_h15 if isinstance(item, float)]
wind_b_k_value_d3_h15 = [item * 1.944 for item in wind_b_d3_h15_float_values_d3_h15]
wind_g_value_d3_h15= [float(match.group(1)) for line in found_d3_h15 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h15 = [item for item in wind_g_value_d3_h15 if isinstance(item, float)]
wind_g_k_value_d3_h15=[item * 1.944 for item in wind_g_float_values_d3_h15]
wind_bf_value_d3_h15= [int(match.group(1)) for line in found_d3_h15 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h15)
#print("wind direction: ",wind_d_value_d3_h15)
#print("wind blow in mps: ",wind_b_value_d3_h15)
#print("wind blow in kts: ",wind_b_k_value_d3_h15)
#print("beaufort scale: ",wind_bf_value_d3_h15)
#print("wind gust in mps: ",wind_g_value_d3_h15)
#print("wind gust in knots: ", wind_g_k_value_d3_h15)

d3_h16=today+ datetime.timedelta(hours=54)
rounded_d3_h16 = today+datetime.timedelta(hours=54)
rounded_d3_h16_1 = rounded_d3_h16.replace(minute=0, second=0, microsecond=0)
formatted_d3_h16 = rounded_d3_h16_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h16=[]

with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h16 in line and line.count(formatted_d3_h16) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h16.append(next(file).strip())
##print(found_d3_h16)
                
celsius_value_d3_h16 = [float(match.group(1)) for line in found_d3_h16 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h16= [str(match.group(1)) for line in found_d3_h16 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h16 = [float(match.group(1)) for line in found_d3_h16 if (match := wind_b_pattern.search(line))]
wind_b_d3_h16_float_values_d3_h16 = [item for item in wind_b_value_d3_h16 if isinstance(item, float)]
wind_b_k_value_d3_h16 = [item * 1.944 for item in wind_b_d3_h16_float_values_d3_h16]
wind_g_value_d3_h16= [float(match.group(1)) for line in found_d3_h16 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h16 = [item for item in wind_g_value_d3_h16 if isinstance(item, float)]
wind_g_k_value_d3_h16=[item * 1.944 for item in wind_g_float_values_d3_h16]
wind_bf_value_d3_h16= [int(match.group(1)) for line in found_d3_h16 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h16)
#print("wind direction: ",wind_d_value_d3_h16)
#print("wind blow in mps: ",wind_b_value_d3_h16)
#print("wind blow in kts: ",wind_b_k_value_d3_h16)
#print("beaufort scale: ",wind_bf_value_d3_h16)
#print("wind gust in mps: ",wind_g_value_d3_h16)
#print("wind gust in knots: ", wind_g_k_value_d3_h16)

d3_h17=today+ datetime.timedelta(hours=55)
rounded_d3_h17 = today+datetime.timedelta(hours=55)
rounded_d3_h17_1 = rounded_d3_h17.replace(minute=0, second=0, microsecond=0)
formatted_d3_h17 = rounded_d3_h17_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h17=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h17 in line and line.count(formatted_d3_h17) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h17.append(next(file).strip())
##print(found_d3_h17)
                
celsius_value_d3_h17 = [float(match.group(1)) for line in found_d3_h17 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h17= [str(match.group(1)) for line in found_d3_h17 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h17 = [float(match.group(1)) for line in found_d3_h17 if (match := wind_b_pattern.search(line))]
wind_b_d3_h17_float_values_d3_h17 = [item for item in wind_b_value_d3_h17 if isinstance(item, float)]
wind_b_k_value_d3_h17 = [item * 1.944 for item in wind_b_d3_h17_float_values_d3_h17]
wind_g_value_d3_h17= [float(match.group(1)) for line in found_d3_h17 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h17 = [item for item in wind_g_value_d3_h17 if isinstance(item, float)]
wind_g_k_value_d3_h17=[item * 1.944 for item in wind_g_float_values_d3_h17]
wind_bf_value_d3_h17= [int(match.group(1)) for line in found_d3_h17 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h17)
#print("wind direction: ",wind_d_value_d3_h17)
#print("wind blow in mps: ",wind_b_value_d3_h17)
#print("wind blow in kts: ",wind_b_k_value_d3_h17)
#print("beaufort scale: ",wind_bf_value_d3_h17)
#print("wind gust in mps: ",wind_g_value_d3_h17)
#print("wind gust in knots: ", wind_g_k_value_d3_h17)

d3_h18=today+ datetime.timedelta(hours=56)
rounded_d3_h18 = today+datetime.timedelta(hours=56)
rounded_d3_h18_1 = rounded_d3_h18.replace(minute=0, second=0, microsecond=0)
formatted_d3_h18 = rounded_d3_h18_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h18=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h18 in line and line.count(formatted_d3_h18) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h18.append(next(file).strip())
##print(found_d3_h18)
                
celsius_value_d3_h18 = [float(match.group(1)) for line in found_d3_h18 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h18= [str(match.group(1)) for line in found_d3_h18 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h18 = [float(match.group(1)) for line in found_d3_h18 if (match := wind_b_pattern.search(line))]
wind_b_d3_h18_float_values_d3_h18 = [item for item in wind_b_value_d3_h18 if isinstance(item, float)]
wind_b_k_value_d3_h18 = [item * 1.944 for item in wind_b_d3_h18_float_values_d3_h18]
wind_g_value_d3_h18= [float(match.group(1)) for line in found_d3_h18 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h18 = [item for item in wind_g_value_d3_h18 if isinstance(item, float)]
wind_g_k_value_d3_h18=[item * 1.944 for item in wind_g_float_values_d3_h18]
wind_bf_value_d3_h18= [int(match.group(1)) for line in found_d3_h18 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h18)
#print("wind direction: ",wind_d_value_d3_h18)
#print("wind blow in mps: ",wind_b_value_d3_h18)
#print("wind blow in kts: ",wind_b_k_value_d3_h18)
#print("beaufort scale: ",wind_bf_value_d3_h18)
#print("wind gust in mps: ",wind_g_value_d3_h18)
#print("wind gust in knots: ", wind_g_k_value_d3_h18)
d3_h19=today+ datetime.timedelta(hours=57)
rounded_d3_h19 = today+datetime.timedelta(hours=57)
rounded_d3_h19_1 = rounded_d3_h19.replace(minute=0, second=0, microsecond=0)
formatted_d3_h19 = rounded_d3_h19_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h19=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h19 in line and line.count(formatted_d3_h19) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h19.append(next(file).strip())
##print(found_d3_h19)
                

celsius_value_d3_h19 = [float(match.group(1)) for line in found_d3_h19 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h19= [str(match.group(1)) for line in found_d3_h19 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h19 = [float(match.group(1)) for line in found_d3_h19 if (match := wind_b_pattern.search(line))]
wind_b_d3_h19_float_values_d3_h19 = [item for item in wind_b_value_d3_h19 if isinstance(item, float)]
wind_b_k_value_d3_h19 = [item * 1.944 for item in wind_b_d3_h19_float_values_d3_h19]
wind_g_value_d3_h19= [float(match.group(1)) for line in found_d3_h19 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h19 = [item for item in wind_g_value_d3_h19 if isinstance(item, float)]
wind_g_k_value_d3_h19=[item * 1.944 for item in wind_g_float_values_d3_h19]
wind_bf_value_d3_h19= [int(match.group(1)) for line in found_d3_h19 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h19)
#print("wind direction: ",wind_d_value_d3_h19)
#print("wind blow in mps: ",wind_b_value_d3_h19)
#print("wind blow in kts: ",wind_b_k_value_d3_h19)
#print("beaufort scale: ",wind_bf_value_d3_h19)
#print("wind gust in mps: ",wind_g_value_d3_h19)
#print("wind gust in knots: ", wind_g_k_value_d3_h19)

d3_h20=today+ datetime.timedelta(hours=58)
rounded_d3_h20 = today+datetime.timedelta(hours=58)
rounded_d3_h20_1 = rounded_d3_h20.replace(minute=0, second=0, microsecond=0)
formatted_d3_h20 = rounded_d3_h20_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h20=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h20 in line and line.count(formatted_d3_h20) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h20.append(next(file).strip())
##print(found_d3_h20)
                

celsius_value_d3_h20 = [float(match.group(1)) for line in found_d3_h20 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h20= [str(match.group(1)) for line in found_d3_h20 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h20 = [float(match.group(1)) for line in found_d3_h20 if (match := wind_b_pattern.search(line))]
wind_b_d3_h20_float_values_d3_h20 = [item for item in wind_b_value_d3_h20 if isinstance(item, float)]
wind_b_k_value_d3_h20 = [item * 1.944 for item in wind_b_d3_h20_float_values_d3_h20]
wind_g_value_d3_h20= [float(match.group(1)) for line in found_d3_h20 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h20 = [item for item in wind_g_value_d3_h20 if isinstance(item, float)]
wind_g_k_value_d3_h20=[item * 1.944 for item in wind_g_float_values_d3_h20]
wind_bf_value_d3_h20= [int(match.group(1)) for line in found_d3_h20 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h20)
#print("wind direction: ",wind_d_value_d3_h20)
#print("wind blow in mps: ",wind_b_value_d3_h20)
#print("wind blow in kts: ",wind_b_k_value_d3_h20)
#print("beaufort scale: ",wind_bf_value_d3_h20)
#print("wind gust in mps: ",wind_g_value_d3_h20)
#print("wind gust in knots: ", wind_g_k_value_d3_h20)

d3_h21=today+ datetime.timedelta(hours=59)
rounded_d3_h21 = today+datetime.timedelta(hours=59)
rounded_d3_h21_1 = rounded_d3_h21.replace(minute=0, second=0, microsecond=0)
formatted_d3_h21 = rounded_d3_h21_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h21=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h21 in line and line.count(formatted_d3_h21) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h21.append(next(file).strip())
##print(found_d3_h21)


celsius_value_d3_h21 = [float(match.group(1)) for line in found_d3_h21 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h21= [str(match.group(1)) for line in found_d3_h21 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h21 = [float(match.group(1)) for line in found_d3_h21 if (match := wind_b_pattern.search(line))]
wind_b_d3_h21_float_values_d3_h21 = [item for item in wind_b_value_d3_h21 if isinstance(item, float)]
wind_b_k_value_d3_h21 = [item * 1.944 for item in wind_b_d3_h21_float_values_d3_h21]
wind_g_value_d3_h21= [float(match.group(1)) for line in found_d3_h21 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h21 = [item for item in wind_g_value_d3_h21 if isinstance(item, float)]
wind_g_k_value_d3_h21=[item * 1.944 for item in wind_g_float_values_d3_h21]
wind_bf_value_d3_h21= [int(match.group(1)) for line in found_d3_h21 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h21)
#print("wind direction: ",wind_d_value_d3_h21)
#print("wind blow in mps: ",wind_b_value_d3_h21)
#print("wind blow in kts: ",wind_b_k_value_d3_h21)
#print("beaufort scale: ",wind_bf_value_d3_h21)
#print("wind gust in mps: ",wind_g_value_d3_h21)
#print("wind gust in knots: ", wind_g_k_value_d3_h21)

d3_h22=today+ datetime.timedelta(hours=60)
rounded_d3_h22 = today+datetime.timedelta(hours=60)
rounded_d3_h22_1 = rounded_d3_h22.replace(minute=0, second=0, microsecond=0)
formatted_d3_h22 = rounded_d3_h22_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d3_h22=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d3_h22 in line and line.count(formatted_d3_h22) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d3_h22.append(next(file).strip())
##print(found_d3_h22)


celsius_value_d3_h22 = [float(match.group(1)) for line in found_d3_h22 if (match := celsius_pattern.search(line))]
wind_d_value_d3_h22= [str(match.group(1)) for line in found_d3_h22 if (match := wind_d_pattern.search(line))]
wind_b_value_d3_h22 = [float(match.group(1)) for line in found_d3_h22 if (match := wind_b_pattern.search(line))]
wind_b_d3_h22_float_values_d3_h22 = [item for item in wind_b_value_d3_h22 if isinstance(item, float)]
wind_b_k_value_d3_h22 = [item * 1.944 for item in wind_b_d3_h22_float_values_d3_h22]
wind_g_value_d3_h22= [float(match.group(1)) for line in found_d3_h22 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d3_h22 = [item for item in wind_g_value_d3_h22 if isinstance(item, float)]
wind_g_k_value_d3_h22=[item * 1.944 for item in wind_g_float_values_d3_h22]
wind_bf_value_d3_h22= [int(match.group(1)) for line in found_d3_h22 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d3_h22)
#print("wind direction: ",wind_d_value_d3_h22)
#print("wind blow in mps: ",wind_b_value_d3_h22)
#print("wind blow in kts: ",wind_b_k_value_d3_h22)
#print("beaufort scale: ",wind_bf_value_d3_h22)
#print("wind gust in mps: ",wind_g_value_d3_h22)
#print("wind gust in knots: ", wind_g_k_value_d3_h22)

d4_h1=today+ datetime.timedelta(hours=61)
rounded_d4_h1 = today+datetime.timedelta(hours=61)
rounded_d4_h1_1 = rounded_d4_h1.replace(minute=0, second=0, microsecond=0)
formatted_d4_h1 = rounded_d4_h1_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h1=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h1 in line and line.count(formatted_d4_h1) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h1.append(next(file).strip())
##print(found_d4_h1)          


celsius_value_d4_h1 = [float(match.group(1)) for line in found_d4_h1 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h1= [str(match.group(1)) for line in found_d4_h1 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h1 = [float(match.group(1)) for line in found_d4_h1 if (match := wind_b_pattern.search(line))]
wind_b_d4_h1_float_values_d4_h1 = [item for item in wind_b_value_d4_h1 if isinstance(item, float)]
wind_b_k_value_d4_h1 = [item * 1.944 for item in wind_b_d4_h1_float_values_d4_h1]
wind_g_value_d4_h1= [float(match.group(1)) for line in found_d4_h1 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h1 = [item for item in wind_g_value_d4_h1 if isinstance(item, float)]
wind_g_k_value_d4_h1=[item * 1.944 for item in wind_g_float_values_d4_h1]
wind_bf_value_d4_h1= [int(match.group(1)) for line in found_d4_h1 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h1)
#print("wind direction: ",wind_d_value_d4_h1)
#print("wind blow in mps: ",wind_b_value_d4_h1)
#print("wind blow in kts: ",wind_b_k_value_d4_h1)
#print("beaufort scale: ",wind_bf_value_d4_h1)
#print("wind gust in mps: ",wind_g_value_d4_h1)
#print("wind gust in knots: ", wind_g_k_value_d4_h1)

d4_h2=today+ datetime.timedelta(hours=62)
rounded_d4_h2 = today+datetime.timedelta(hours=62)
rounded_d4_h2_1 = rounded_d4_h2.replace(minute=0, second=0, microsecond=0)
formatted_d4_h2 = rounded_d4_h2_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h2=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h2 in line and line.count(formatted_d4_h2) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h2.append(next(file).strip())
##print(found_d4_h2)          


celsius_value_d4_h2 = [float(match.group(1)) for line in found_d4_h2 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h2= [str(match.group(1)) for line in found_d4_h2 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h2 = [float(match.group(1)) for line in found_d4_h2 if (match := wind_b_pattern.search(line))]
wind_b_d4_h2_float_values_d4_h2 = [item for item in wind_b_value_d4_h2 if isinstance(item, float)]
wind_b_k_value_d4_h2 = [item * 1.944 for item in wind_b_d4_h2_float_values_d4_h2]
wind_g_value_d4_h2= [float(match.group(1)) for line in found_d4_h2 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h2 = [item for item in wind_g_value_d4_h2 if isinstance(item, float)]
wind_g_k_value_d4_h2=[item * 1.944 for item in wind_g_float_values_d4_h2]
wind_bf_value_d4_h2= [int(match.group(1)) for line in found_d4_h2 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h2)
#print("wind direction: ",wind_d_value_d4_h2)
#print("wind blow in mps: ",wind_b_value_d4_h2)
#print("wind blow in kts: ",wind_b_k_value_d4_h2)
#print("beaufort scale: ",wind_bf_value_d4_h2)
#print("wind gust in mps: ",wind_g_value_d4_h2)
#print("wind gust in knots: ", wind_g_k_value_d4_h2)

d4_h3=today+ datetime.timedelta(hours=63)
rounded_d4_h3 = today+datetime.timedelta(hours=63)
rounded_d4_h3_1 = rounded_d4_h3.replace(minute=0, second=0, microsecond=0)
formatted_d4_h3 = rounded_d4_h3_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h3=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h3 in line and line.count(formatted_d4_h3) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h3.append(next(file).strip())
##print(found_d4_h3)          


celsius_value_d4_h3 = [float(match.group(1)) for line in found_d4_h3 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h3= [str(match.group(1)) for line in found_d4_h3 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h3 = [float(match.group(1)) for line in found_d4_h3 if (match := wind_b_pattern.search(line))]
wind_b_d4_h3_float_values_d4_h3 = [item for item in wind_b_value_d4_h3 if isinstance(item, float)]
wind_b_k_value_d4_h3 = [item * 1.944 for item in wind_b_d4_h3_float_values_d4_h3]
wind_g_value_d4_h3= [float(match.group(1)) for line in found_d4_h3 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h3 = [item for item in wind_g_value_d4_h3 if isinstance(item, float)]
wind_g_k_value_d4_h3=[item * 1.944 for item in wind_g_float_values_d4_h3]
wind_bf_value_d4_h3= [int(match.group(1)) for line in found_d4_h3 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h3)
#print("wind direction: ",wind_d_value_d4_h3)
#print("wind blow in mps: ",wind_b_value_d4_h3)
#print("wind blow in kts: ",wind_b_k_value_d4_h3)
#print("beaufort scale: ",wind_bf_value_d4_h3)
#print("wind gust in mps: ",wind_g_value_d4_h3)
#print("wind gust in knots: ", wind_g_k_value_d4_h3)

d4_h4=today+ datetime.timedelta(hours=64)
rounded_d4_h4 = today+datetime.timedelta(hours=64)
rounded_d4_h4_1 = rounded_d4_h4.replace(minute=0, second=0, microsecond=0)
formatted_d4_h4 = rounded_d4_h4_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h4=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h4 in line and line.count(formatted_d4_h4) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h4.append(next(file).strip())
##print(found_d4_h4)          


celsius_value_d4_h4 = [float(match.group(1)) for line in found_d4_h4 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h4= [str(match.group(1)) for line in found_d4_h4 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h4 = [float(match.group(1)) for line in found_d4_h4 if (match := wind_b_pattern.search(line))]
wind_b_d4_h4_float_values_d4_h4 = [item for item in wind_b_value_d4_h4 if isinstance(item, float)]
wind_b_k_value_d4_h4 = [item * 1.944 for item in wind_b_d4_h4_float_values_d4_h4]
wind_g_value_d4_h4= [float(match.group(1)) for line in found_d4_h4 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h4 = [item for item in wind_g_value_d4_h4 if isinstance(item, float)]
wind_g_k_value_d4_h4=[item * 1.944 for item in wind_g_float_values_d4_h4]
wind_bf_value_d4_h4= [int(match.group(1)) for line in found_d4_h4 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h4)
#print("wind direction: ",wind_d_value_d4_h4)
#print("wind blow in mps: ",wind_b_value_d4_h4)
#print("wind blow in kts: ",wind_b_k_value_d4_h4)
#print("beaufort scale: ",wind_bf_value_d4_h4)
#print("wind gust in mps: ",wind_g_value_d4_h4)
#print("wind gust in knots: ", wind_g_k_value_d4_h4)

d4_h5=today+ datetime.timedelta(hours=65)
rounded_d4_h5 = today+datetime.timedelta(hours=65)
rounded_d4_h5_1 = rounded_d4_h5.replace(minute=0, second=0, microsecond=0)
formatted_d4_h5 = rounded_d4_h5_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h5=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h5 in line and line.count(formatted_d4_h5) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h5.append(next(file).strip())
##print(found_d4_h5)          


celsius_value_d4_h5 = [float(match.group(1)) for line in found_d4_h5 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h5= [str(match.group(1)) for line in found_d4_h5 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h5 = [float(match.group(1)) for line in found_d4_h5 if (match := wind_b_pattern.search(line))]
wind_b_d4_h5_float_values_d4_h5 = [item for item in wind_b_value_d4_h5 if isinstance(item, float)]
wind_b_k_value_d4_h5 = [item * 1.944 for item in wind_b_d4_h5_float_values_d4_h5]
wind_g_value_d4_h5= [float(match.group(1)) for line in found_d4_h5 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h5 = [item for item in wind_g_value_d4_h5 if isinstance(item, float)]
wind_g_k_value_d4_h5=[item * 1.944 for item in wind_g_float_values_d4_h5]
wind_bf_value_d4_h5= [int(match.group(1)) for line in found_d4_h5 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h5)
#print("wind direction: ",wind_d_value_d4_h5)
#print("wind blow in mps: ",wind_b_value_d4_h5)
#print("wind blow in kts: ",wind_b_k_value_d4_h5)
#print("beaufort scale: ",wind_bf_value_d4_h5)
#print("wind gust in mps: ",wind_g_value_d4_h5)
#print("wind gust in knots: ", wind_g_k_value_d4_h5)

d4_h6=today+ datetime.timedelta(hours=66)
rounded_d4_h6 = today+datetime.timedelta(hours=66)
rounded_d4_h6_1 = rounded_d4_h6.replace(minute=0, second=0, microsecond=0)
formatted_d4_h6 = rounded_d4_h6_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h6=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h6 in line and line.count(formatted_d4_h6) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h6.append(next(file).strip())
##print(found_d4_h6)          


celsius_value_d4_h6 = [float(match.group(1)) for line in found_d4_h6 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h6= [str(match.group(1)) for line in found_d4_h6 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h6 = [float(match.group(1)) for line in found_d4_h6 if (match := wind_b_pattern.search(line))]
wind_b_d4_h6_float_values_d4_h6 = [item for item in wind_b_value_d4_h6 if isinstance(item, float)]
wind_b_k_value_d4_h6 = [item * 1.944 for item in wind_b_d4_h6_float_values_d4_h6]
wind_g_value_d4_h6= [float(match.group(1)) for line in found_d4_h6 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h6 = [item for item in wind_g_value_d4_h6 if isinstance(item, float)]
wind_g_k_value_d4_h6=[item * 1.944 for item in wind_g_float_values_d4_h6]
wind_bf_value_d4_h6= [int(match.group(1)) for line in found_d4_h6 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h6)
#print("wind direction: ",wind_d_value_d4_h6)
#print("wind blow in mps: ",wind_b_value_d4_h6)
#print("wind blow in kts: ",wind_b_k_value_d4_h6)
#print("beaufort scale: ",wind_bf_value_d4_h6)
#print("wind gust in mps: ",wind_g_value_d4_h6)
#print("wind gust in knots: ", wind_g_k_value_d4_h6)

d4_h7=today+ datetime.timedelta(hours=67)
rounded_d4_h7 = today+datetime.timedelta(hours=67)
rounded_d4_h7_1 = rounded_d4_h7.replace(minute=0, second=0, microsecond=0)
formatted_d4_h7 = rounded_d4_h7_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h7=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h7 in line and line.count(formatted_d4_h7) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h7.append(next(file).strip())
##print(found_d4_h7)          


celsius_value_d4_h7 = [float(match.group(1)) for line in found_d4_h7 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h7= [str(match.group(1)) for line in found_d4_h7 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h7 = [float(match.group(1)) for line in found_d4_h7 if (match := wind_b_pattern.search(line))]
wind_b_d4_h7_float_values_d4_h7 = [item for item in wind_b_value_d4_h7 if isinstance(item, float)]
wind_b_k_value_d4_h7 = [item * 1.944 for item in wind_b_d4_h7_float_values_d4_h7]
wind_g_value_d4_h7= [float(match.group(1)) for line in found_d4_h7 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h7 = [item for item in wind_g_value_d4_h7 if isinstance(item, float)]
wind_g_k_value_d4_h7=[item * 1.944 for item in wind_g_float_values_d4_h7]
wind_bf_value_d4_h7= [int(match.group(1)) for line in found_d4_h7 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h7)
#print("wind direction: ",wind_d_value_d4_h7)
#print("wind blow in mps: ",wind_b_value_d4_h7)
#print("wind blow in kts: ",wind_b_k_value_d4_h7)
#print("beaufort scale: ",wind_bf_value_d4_h7)
#print("wind gust in mps: ",wind_g_value_d4_h7)
#print("wind gust in knots: ", wind_g_k_value_d4_h7)

d4_h8=today+ datetime.timedelta(hours=68)
rounded_d4_h8 = today+datetime.timedelta(hours=68)
rounded_d4_h8_1 = rounded_d4_h8.replace(minute=0, second=0, microsecond=0)
formatted_d4_h8 = rounded_d4_h8_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h8=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h8 in line and line.count(formatted_d4_h8) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h8.append(next(file).strip())
##print(found_d4_h8)          


celsius_value_d4_h8 = [float(match.group(1)) for line in found_d4_h8 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h8= [str(match.group(1)) for line in found_d4_h8 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h8 = [float(match.group(1)) for line in found_d4_h8 if (match := wind_b_pattern.search(line))]
wind_b_d4_h8_float_values_d4_h8 = [item for item in wind_b_value_d4_h8 if isinstance(item, float)]
wind_b_k_value_d4_h8 = [item * 1.944 for item in wind_b_d4_h8_float_values_d4_h8]
wind_g_value_d4_h8= [float(match.group(1)) for line in found_d4_h8 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h8 = [item for item in wind_g_value_d4_h8 if isinstance(item, float)]
wind_g_k_value_d4_h8=[item * 1.944 for item in wind_g_float_values_d4_h8]
wind_bf_value_d4_h8= [int(match.group(1)) for line in found_d4_h8 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h8)
#print("wind direction: ",wind_d_value_d4_h8)
#print("wind blow in mps: ",wind_b_value_d4_h8)
#print("wind blow in kts: ",wind_b_k_value_d4_h8)
#print("beaufort scale: ",wind_bf_value_d4_h8)
#print("wind gust in mps: ",wind_g_value_d4_h8)
#print("wind gust in knots: ", wind_g_k_value_d4_h8)

d4_h9=today+ datetime.timedelta(hours=69)
rounded_d4_h9 = today+datetime.timedelta(hours=69)
rounded_d4_h9_1 = rounded_d4_h9.replace(minute=0, second=0, microsecond=0)
formatted_d4_h9 = rounded_d4_h9_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h9=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h9 in line and line.count(formatted_d4_h9) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h9.append(next(file).strip())
##print(found_d4_h9)          


celsius_value_d4_h9 = [float(match.group(1)) for line in found_d4_h9 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h9= [str(match.group(1)) for line in found_d4_h9 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h9 = [float(match.group(1)) for line in found_d4_h9 if (match := wind_b_pattern.search(line))]
wind_b_d4_h9_float_values_d4_h9 = [item for item in wind_b_value_d4_h9 if isinstance(item, float)]
wind_b_k_value_d4_h9 = [item * 1.944 for item in wind_b_d4_h9_float_values_d4_h9]
wind_g_value_d4_h9= [float(match.group(1)) for line in found_d4_h9 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h9 = [item for item in wind_g_value_d4_h9 if isinstance(item, float)]
wind_g_k_value_d4_h9=[item * 1.944 for item in wind_g_float_values_d4_h9]
wind_bf_value_d4_h9= [int(match.group(1)) for line in found_d4_h9 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h9)
#print("wind direction: ",wind_d_value_d4_h9)
#print("wind blow in mps: ",wind_b_value_d4_h9)
#print("wind blow in kts: ",wind_b_k_value_d4_h9)
#print("beaufort scale: ",wind_bf_value_d4_h9)
#print("wind gust in mps: ",wind_g_value_d4_h9)
#print("wind gust in knots: ", wind_g_k_value_d4_h9)

d4_h10=today+ datetime.timedelta(hours=70)
rounded_d4_h10 = today+datetime.timedelta(hours=70)
rounded_d4_h10_1 = rounded_d4_h10.replace(minute=0, second=0, microsecond=0)
formatted_d4_h10 = rounded_d4_h10_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h10=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h10 in line and line.count(formatted_d4_h10) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h10.append(next(file).strip())
##print(found_d4_h10)          


celsius_value_d4_h10 = [float(match.group(1)) for line in found_d4_h10 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h10= [str(match.group(1)) for line in found_d4_h10 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h10 = [float(match.group(1)) for line in found_d4_h10 if (match := wind_b_pattern.search(line))]
wind_b_d4_h10_float_values_d4_h10 = [item for item in wind_b_value_d4_h10 if isinstance(item, float)]
wind_b_k_value_d4_h10 = [item * 1.944 for item in wind_b_d4_h10_float_values_d4_h10]
wind_g_value_d4_h10= [float(match.group(1)) for line in found_d4_h10 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h10 = [item for item in wind_g_value_d4_h10 if isinstance(item, float)]
wind_g_k_value_d4_h10=[item * 1.944 for item in wind_g_float_values_d4_h10]
wind_bf_value_d4_h10= [int(match.group(1)) for line in found_d4_h10 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h10)
#print("wind direction: ",wind_d_value_d4_h10)
#print("wind blow in mps: ",wind_b_value_d4_h10)
#print("wind blow in kts: ",wind_b_k_value_d4_h10)
#print("beaufort scale: ",wind_bf_value_d4_h10)
#print("wind gust in mps: ",wind_g_value_d4_h10)
#print("wind gust in knots: ", wind_g_k_value_d4_h10)

d4_h11=today+ datetime.timedelta(hours=71)
rounded_d4_h11 = today+datetime.timedelta(hours=71)
rounded_d4_h11_1 = rounded_d4_h11.replace(minute=0, second=0, microsecond=0)
formatted_d4_h11 = rounded_d4_h11_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h11=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h11 in line and line.count(formatted_d4_h11) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h11.append(next(file).strip())
##print(found_d4_h11)          


celsius_value_d4_h11 = [float(match.group(1)) for line in found_d4_h11 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h11= [str(match.group(1)) for line in found_d4_h11 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h11 = [float(match.group(1)) for line in found_d4_h11 if (match := wind_b_pattern.search(line))]
wind_b_d4_h11_float_values_d4_h11 = [item for item in wind_b_value_d4_h11 if isinstance(item, float)]
wind_b_k_value_d4_h11 = [item * 1.944 for item in wind_b_d4_h11_float_values_d4_h11]
wind_g_value_d4_h11= [float(match.group(1)) for line in found_d4_h11 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h11 = [item for item in wind_g_value_d4_h11 if isinstance(item, float)]
wind_g_k_value_d4_h11=[item * 1.944 for item in wind_g_float_values_d4_h11]
wind_bf_value_d4_h11= [int(match.group(1)) for line in found_d4_h11 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h11)
#print("wind direction: ",wind_d_value_d4_h11)
#print("wind blow in mps: ",wind_b_value_d4_h11)
#print("wind blow in kts: ",wind_b_k_value_d4_h11)
#print("beaufort scale: ",wind_bf_value_d4_h11)
#print("wind gust in mps: ",wind_g_value_d4_h11)
#print("wind gust in knots: ", wind_g_k_value_d4_h11)

d4_h12=today+ datetime.timedelta(hours=72)
rounded_d4_h12 = today+datetime.timedelta(hours=72)
rounded_d4_h12_1 = rounded_d4_h12.replace(minute=0, second=0, microsecond=0)
formatted_d4_h12 = rounded_d4_h12_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h12=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h12 in line and line.count(formatted_d4_h12) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h12.append(next(file).strip())
##print(found_d4_h12)          


celsius_value_d4_h12 = [float(match.group(1)) for line in found_d4_h12 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h12= [str(match.group(1)) for line in found_d4_h12 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h12 = [float(match.group(1)) for line in found_d4_h12 if (match := wind_b_pattern.search(line))]
wind_b_d4_h12_float_values_d4_h12 = [item for item in wind_b_value_d4_h12 if isinstance(item, float)]
wind_b_k_value_d4_h12 = [item * 1.944 for item in wind_b_d4_h12_float_values_d4_h12]
wind_g_value_d4_h12= [float(match.group(1)) for line in found_d4_h12 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h12 = [item for item in wind_g_value_d4_h12 if isinstance(item, float)]
wind_g_k_value_d4_h12=[item * 1.944 for item in wind_g_float_values_d4_h12]
wind_bf_value_d4_h12= [int(match.group(1)) for line in found_d4_h12 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h12)
#print("wind direction: ",wind_d_value_d4_h12)
#print("wind blow in mps: ",wind_b_value_d4_h12)
#print("wind blow in kts: ",wind_b_k_value_d4_h12)
#print("beaufort scale: ",wind_bf_value_d4_h12)
#print("wind gust in mps: ",wind_g_value_d4_h12)
#print("wind gust in knots: ", wind_g_k_value_d4_h12)

d4_h13=today+ datetime.timedelta(hours=73)
rounded_d4_h13 = today+datetime.timedelta(hours=73)
rounded_d4_h13_1 = rounded_d4_h13.replace(minute=0, second=0, microsecond=0)
formatted_d4_h13 = rounded_d4_h13_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h13=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h13 in line and line.count(formatted_d4_h13) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h13.append(next(file).strip())
##print(found_d4_h13)          


celsius_value_d4_h13 = [float(match.group(1)) for line in found_d4_h13 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h13= [str(match.group(1)) for line in found_d4_h13 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h13 = [float(match.group(1)) for line in found_d4_h13 if (match := wind_b_pattern.search(line))]
wind_b_d4_h13_float_values_d4_h13 = [item for item in wind_b_value_d4_h13 if isinstance(item, float)]
wind_b_k_value_d4_h13 = [item * 1.944 for item in wind_b_d4_h13_float_values_d4_h13]
wind_g_value_d4_h13= [float(match.group(1)) for line in found_d4_h13 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h13 = [item for item in wind_g_value_d4_h13 if isinstance(item, float)]
wind_g_k_value_d4_h13=[item * 1.944 for item in wind_g_float_values_d4_h13]
wind_bf_value_d4_h13= [int(match.group(1)) for line in found_d4_h13 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h13)
#print("wind direction: ",wind_d_value_d4_h13)
#print("wind blow in mps: ",wind_b_value_d4_h13)
#print("wind blow in kts: ",wind_b_k_value_d4_h13)
#print("beaufort scale: ",wind_bf_value_d4_h13)
#print("wind gust in mps: ",wind_g_value_d4_h13)
#print("wind gust in knots: ", wind_g_k_value_d4_h13)

d4_h14=today+ datetime.timedelta(hours=74)
rounded_d4_h14 = today+datetime.timedelta(hours=74)
rounded_d4_h14_1 = rounded_d4_h14.replace(minute=0, second=0, microsecond=0)
formatted_d4_h14 = rounded_d4_h14_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h14=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h14 in line and line.count(formatted_d4_h14) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h14.append(next(file).strip())
##print(found_d4_h14)          


celsius_value_d4_h14 = [float(match.group(1)) for line in found_d4_h14 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h14= [str(match.group(1)) for line in found_d4_h14 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h14 = [float(match.group(1)) for line in found_d4_h14 if (match := wind_b_pattern.search(line))]
wind_b_d4_h14_float_values_d4_h14 = [item for item in wind_b_value_d4_h14 if isinstance(item, float)]
wind_b_k_value_d4_h14 = [item * 1.944 for item in wind_b_d4_h14_float_values_d4_h14]
wind_g_value_d4_h14= [float(match.group(1)) for line in found_d4_h14 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h14 = [item for item in wind_g_value_d4_h14 if isinstance(item, float)]
wind_g_k_value_d4_h14=[item * 1.944 for item in wind_g_float_values_d4_h14]
wind_bf_value_d4_h14= [int(match.group(1)) for line in found_d4_h14 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h14)
#print("wind direction: ",wind_d_value_d4_h14)
#print("wind blow in mps: ",wind_b_value_d4_h14)
#print("wind blow in kts: ",wind_b_k_value_d4_h14)
#print("beaufort scale: ",wind_bf_value_d4_h14)
#print("wind gust in mps: ",wind_g_value_d4_h14)
#print("wind gust in knots: ", wind_g_k_value_d4_h14)

d4_h15=today+ datetime.timedelta(hours=75)
rounded_d4_h15 = today+datetime.timedelta(hours=75)
rounded_d4_h15_1 = rounded_d4_h15.replace(minute=0, second=0, microsecond=0)
formatted_d4_h15 = rounded_d4_h15_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h15=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h15 in line and line.count(formatted_d4_h15) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h15.append(next(file).strip())
##print(found_d4_h15)          


celsius_value_d4_h15 = [float(match.group(1)) for line in found_d4_h15 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h15= [str(match.group(1)) for line in found_d4_h15 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h15 = [float(match.group(1)) for line in found_d4_h15 if (match := wind_b_pattern.search(line))]
wind_b_d4_h15_float_values_d4_h15 = [item for item in wind_b_value_d4_h15 if isinstance(item, float)]
wind_b_k_value_d4_h15 = [item * 1.944 for item in wind_b_d4_h15_float_values_d4_h15]
wind_g_value_d4_h15= [float(match.group(1)) for line in found_d4_h15 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h15 = [item for item in wind_g_value_d4_h15 if isinstance(item, float)]
wind_g_k_value_d4_h15=[item * 1.944 for item in wind_g_float_values_d4_h15]
wind_bf_value_d4_h15= [int(match.group(1)) for line in found_d4_h15 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h15)
#print("wind direction: ",wind_d_value_d4_h15)
#print("wind blow in mps: ",wind_b_value_d4_h15)
#print("wind blow in kts: ",wind_b_k_value_d4_h15)
#print("beaufort scale: ",wind_bf_value_d4_h15)
#print("wind gust in mps: ",wind_g_value_d4_h15)
#print("wind gust in knots: ", wind_g_k_value_d4_h15)

d4_h16=today+ datetime.timedelta(hours=76)
rounded_d4_h16 = today+datetime.timedelta(hours=76)
rounded_d4_h16_1 = rounded_d4_h16.replace(minute=0, second=0, microsecond=0)
formatted_d4_h16 = rounded_d4_h16_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h16=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h16 in line and line.count(formatted_d4_h16) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h16.append(next(file).strip())
##print(found_d4_h16)          


celsius_value_d4_h16 = [float(match.group(1)) for line in found_d4_h16 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h16= [str(match.group(1)) for line in found_d4_h16 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h16 = [float(match.group(1)) for line in found_d4_h16 if (match := wind_b_pattern.search(line))]
wind_b_d4_h16_float_values_d4_h16 = [item for item in wind_b_value_d4_h16 if isinstance(item, float)]
wind_b_k_value_d4_h16 = [item * 1.944 for item in wind_b_d4_h16_float_values_d4_h16]
wind_g_value_d4_h16= [float(match.group(1)) for line in found_d4_h16 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h16 = [item for item in wind_g_value_d4_h16 if isinstance(item, float)]
wind_g_k_value_d4_h16=[item * 1.944 for item in wind_g_float_values_d4_h16]
wind_bf_value_d4_h16= [int(match.group(1)) for line in found_d4_h16 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h16)
#print("wind direction: ",wind_d_value_d4_h16)
#print("wind blow in mps: ",wind_b_value_d4_h16)
#print("wind blow in kts: ",wind_b_k_value_d4_h16)
#print("beaufort scale: ",wind_bf_value_d4_h16)
#print("wind gust in mps: ",wind_g_value_d4_h16)
#print("wind gust in knots: ", wind_g_k_value_d4_h16)

d4_h17=today+ datetime.timedelta(hours=77)
rounded_d4_h17 = today+datetime.timedelta(hours=77)
rounded_d4_h17_1 = rounded_d4_h17.replace(minute=0, second=0, microsecond=0)
formatted_d4_h17 = rounded_d4_h17_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h17=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h17 in line and line.count(formatted_d4_h17) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h17.append(next(file).strip())
##print(found_d4_h17)          


celsius_value_d4_h17 = [float(match.group(1)) for line in found_d4_h17 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h17= [str(match.group(1)) for line in found_d4_h17 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h17 = [float(match.group(1)) for line in found_d4_h17 if (match := wind_b_pattern.search(line))]
wind_b_d4_h17_float_values_d4_h17 = [item for item in wind_b_value_d4_h17 if isinstance(item, float)]
wind_b_k_value_d4_h17 = [item * 1.944 for item in wind_b_d4_h17_float_values_d4_h17]
wind_g_value_d4_h17= [float(match.group(1)) for line in found_d4_h17 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h17 = [item for item in wind_g_value_d4_h17 if isinstance(item, float)]
wind_g_k_value_d4_h17=[item * 1.944 for item in wind_g_float_values_d4_h17]
wind_bf_value_d4_h17= [int(match.group(1)) for line in found_d4_h17 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h17)
#print("wind direction: ",wind_d_value_d4_h17)
#print("wind blow in mps: ",wind_b_value_d4_h17)
#print("wind blow in kts: ",wind_b_k_value_d4_h17)
#print("beaufort scale: ",wind_bf_value_d4_h17)
#print("wind gust in mps: ",wind_g_value_d4_h17)
#print("wind gust in knots: ", wind_g_k_value_d4_h17)

d4_h18=today+ datetime.timedelta(hours=78)
rounded_d4_h18 = today+datetime.timedelta(hours=78)
rounded_d4_h18_1 = rounded_d4_h18.replace(minute=0, second=0, microsecond=0)
formatted_d4_h18 = rounded_d4_h18_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h18=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h18 in line and line.count(formatted_d4_h18) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h18.append(next(file).strip())
##print(found_d4_h18)          


celsius_value_d4_h18 = [float(match.group(1)) for line in found_d4_h18 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h18= [str(match.group(1)) for line in found_d4_h18 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h18 = [float(match.group(1)) for line in found_d4_h18 if (match := wind_b_pattern.search(line))]
wind_b_d4_h18_float_values_d4_h18 = [item for item in wind_b_value_d4_h18 if isinstance(item, float)]
wind_b_k_value_d4_h18 = [item * 1.944 for item in wind_b_d4_h18_float_values_d4_h18]
wind_g_value_d4_h18= [float(match.group(1)) for line in found_d4_h18 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h18 = [item for item in wind_g_value_d4_h18 if isinstance(item, float)]
wind_g_k_value_d4_h18=[item * 1.944 for item in wind_g_float_values_d4_h18]
wind_bf_value_d4_h18= [int(match.group(1)) for line in found_d4_h18 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h18)
#print("wind direction: ",wind_d_value_d4_h18)
#print("wind blow in mps: ",wind_b_value_d4_h18)
#print("wind blow in kts: ",wind_b_k_value_d4_h18)
#print("beaufort scale: ",wind_bf_value_d4_h18)
#print("wind gust in mps: ",wind_g_value_d4_h18)
#print("wind gust in knots: ", wind_g_k_value_d4_h18)

d4_h19=today+ datetime.timedelta(hours=79)
rounded_d4_h19 = today+datetime.timedelta(hours=79)
rounded_d4_h19_1 = rounded_d4_h19.replace(minute=0, second=0, microsecond=0)
formatted_d4_h19 = rounded_d4_h19_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h19=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h19 in line and line.count(formatted_d4_h19) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h19.append(next(file).strip())
##print(found_d4_h19)          


celsius_value_d4_h19 = [float(match.group(1)) for line in found_d4_h19 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h19= [str(match.group(1)) for line in found_d4_h19 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h19 = [float(match.group(1)) for line in found_d4_h19 if (match := wind_b_pattern.search(line))]
wind_b_d4_h19_float_values_d4_h19 = [item for item in wind_b_value_d4_h19 if isinstance(item, float)]
wind_b_k_value_d4_h19 = [item * 1.944 for item in wind_b_d4_h19_float_values_d4_h19]
wind_g_value_d4_h19= [float(match.group(1)) for line in found_d4_h19 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h19 = [item for item in wind_g_value_d4_h19 if isinstance(item, float)]
wind_g_k_value_d4_h19=[item * 1.944 for item in wind_g_float_values_d4_h19]
wind_bf_value_d4_h19= [int(match.group(1)) for line in found_d4_h19 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h19)
#print("wind direction: ",wind_d_value_d4_h19)
#print("wind blow in mps: ",wind_b_value_d4_h19)
#print("wind blow in kts: ",wind_b_k_value_d4_h19)
#print("beaufort scale: ",wind_bf_value_d4_h19)
#print("wind gust in mps: ",wind_g_value_d4_h19)
#print("wind gust in knots: ", wind_g_k_value_d4_h19)

d4_h20=today+ datetime.timedelta(hours=80)
rounded_d4_h20 = today+datetime.timedelta(hours=80)
rounded_d4_h20_1 = rounded_d4_h20.replace(minute=0, second=0, microsecond=0)
formatted_d4_h20 = rounded_d4_h20_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h20=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h20 in line and line.count(formatted_d4_h20) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h20.append(next(file).strip())
##print(found_d4_h20)          


celsius_value_d4_h20 = [float(match.group(1)) for line in found_d4_h20 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h20= [str(match.group(1)) for line in found_d4_h20 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h20 = [float(match.group(1)) for line in found_d4_h20 if (match := wind_b_pattern.search(line))]
wind_b_d4_h20_float_values_d4_h20 = [item for item in wind_b_value_d4_h20 if isinstance(item, float)]
wind_b_k_value_d4_h20 = [item * 1.944 for item in wind_b_d4_h20_float_values_d4_h20]
wind_g_value_d4_h20= [float(match.group(1)) for line in found_d4_h20 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h20 = [item for item in wind_g_value_d4_h20 if isinstance(item, float)]
wind_g_k_value_d4_h20=[item * 1.944 for item in wind_g_float_values_d4_h20]
wind_bf_value_d4_h20= [int(match.group(1)) for line in found_d4_h20 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h20)
#print("wind direction: ",wind_d_value_d4_h20)
#print("wind blow in mps: ",wind_b_value_d4_h20)
#print("wind blow in kts: ",wind_b_k_value_d4_h20)
#print("beaufort scale: ",wind_bf_value_d4_h20)
#print("wind gust in mps: ",wind_g_value_d4_h20)
#print("wind gust in knots: ", wind_g_k_value_d4_h20)

d4_h21=today+ datetime.timedelta(hours=81)
rounded_d4_h21 = today+datetime.timedelta(hours=81)
rounded_d4_h21_1 = rounded_d4_h21.replace(minute=0, second=0, microsecond=0)
formatted_d4_h21 = rounded_d4_h21_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h21=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h21 in line and line.count(formatted_d4_h21) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h21.append(next(file).strip())
##print(found_d4_h21)          


celsius_value_d4_h21 = [float(match.group(1)) for line in found_d4_h21 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h21= [str(match.group(1)) for line in found_d4_h21 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h21 = [float(match.group(1)) for line in found_d4_h21 if (match := wind_b_pattern.search(line))]
wind_b_d4_h21_float_values_d4_h21 = [item for item in wind_b_value_d4_h21 if isinstance(item, float)]
wind_b_k_value_d4_h21 = [item * 1.944 for item in wind_b_d4_h21_float_values_d4_h21]
wind_g_value_d4_h21= [float(match.group(1)) for line in found_d4_h21 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h21 = [item for item in wind_g_value_d4_h21 if isinstance(item, float)]
wind_g_k_value_d4_h21=[item * 1.944 for item in wind_g_float_values_d4_h21]
wind_bf_value_d4_h21= [int(match.group(1)) for line in found_d4_h21 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h21)
#print("wind direction: ",wind_d_value_d4_h21)
#print("wind blow in mps: ",wind_b_value_d4_h21)
#print("wind blow in kts: ",wind_b_k_value_d4_h21)
#print("beaufort scale: ",wind_bf_value_d4_h21)
#print("wind gust in mps: ",wind_g_value_d4_h21)
#print("wind gust in knots: ", wind_g_k_value_d4_h21)

d4_h22=today+ datetime.timedelta(hours=82)
rounded_d4_h22 = today+datetime.timedelta(hours=82)
rounded_d4_h22_1 = rounded_d4_h22.replace(minute=0, second=0, microsecond=0)
formatted_d4_h22 = rounded_d4_h22_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h22=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h22 in line and line.count(formatted_d4_h22) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h22.append(next(file).strip())
##print("d_22",found_d4_h22)          


celsius_value_d4_h22 = [float(match.group(1)) for line in found_d4_h22 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h22= [str(match.group(1)) for line in found_d4_h22 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h22 = [float(match.group(1)) for line in found_d4_h22 if (match := wind_b_pattern.search(line))]
wind_b_d4_h22_float_values_d4_h22 = [item for item in wind_b_value_d4_h22 if isinstance(item, float)]
wind_b_k_value_d4_h22 = [item * 1.944 for item in wind_b_d4_h22_float_values_d4_h22]
wind_g_value_d4_h22= [float(match.group(1)) for line in found_d4_h22 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h22 = [item for item in wind_g_value_d4_h22 if isinstance(item, float)]
wind_g_k_value_d4_h22=[item * 1.944 for item in wind_g_float_values_d4_h22]
wind_bf_value_d4_h22= [int(match.group(1)) for line in found_d4_h22 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h22)
#print("wind direction: ",wind_d_value_d4_h22)
#print("wind blow in mps: ",wind_b_value_d4_h22)
#print("wind blow in kts: ",wind_b_k_value_d4_h22)
#print("beaufort scale: ",wind_bf_value_d4_h22)
#print("wind gust in mps: ",wind_g_value_d4_h22)
#print("wind gust in knots: ", wind_g_k_value_d4_h22)

d4_h23=today+ datetime.timedelta(hours=83)
rounded_d4_h23 = today+datetime.timedelta(hours=83)
rounded_d4_h23_1 = rounded_d4_h23.replace(minute=0, second=0, microsecond=0)
formatted_d4_h23 = rounded_d4_h23_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h23=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h23 in line and line.count(formatted_d4_h23) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h23.append(next(file).strip())
##print(found_d4_h23)          


celsius_value_d4_h23 = [float(match.group(1)) for line in found_d4_h23 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h23= [str(match.group(1)) for line in found_d4_h23 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h23 = [float(match.group(1)) for line in found_d4_h23 if (match := wind_b_pattern.search(line))]
wind_b_d4_h23_float_values_d4_h23 = [item for item in wind_b_value_d4_h23 if isinstance(item, float)]
wind_b_k_value_d4_h23 = [item * 1.944 for item in wind_b_d4_h23_float_values_d4_h23]
wind_g_value_d4_h23= [float(match.group(1)) for line in found_d4_h23 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h23 = [item for item in wind_g_value_d4_h23 if isinstance(item, float)]
wind_g_k_value_d4_h23=[item * 1.944 for item in wind_g_float_values_d4_h23]
wind_bf_value_d4_h23= [int(match.group(1)) for line in found_d4_h23 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h23)
#print("wind direction: ",wind_d_value_d4_h23)
#print("wind blow in mps: ",wind_b_value_d4_h23)
#print("wind blow in kts: ",wind_b_k_value_d4_h23)
#print("beaufort scale: ",wind_bf_value_d4_h23)
#print("wind gust in mps: ",wind_g_value_d4_h23)
#print("wind gust in knots: ", wind_g_k_value_d4_h23)

d4_h24=today+ datetime.timedelta(hours=84)
rounded_d4_h24 = today+datetime.timedelta(hours=84)
rounded_d4_h24_1 = rounded_d4_h24.replace(minute=0, second=0, microsecond=0)
formatted_d4_h24 = rounded_d4_h24_1.strftime('%Y-%m-%dT%H:%M:%SZ')
found_d4_h24=[]
with open(txt_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_variable and search_variable2 in line and formatted_d4_h24 in line and line.count(formatted_d4_h24) == 2:
            #print(f"Line {line_number}: {line.strip()}")
            for _ in range(19):
                found_d4_h24.append(next(file).strip())
##print(found_d4_h24)          


celsius_value_d4_h24 = [float(match.group(1)) for line in found_d4_h24 if (match := celsius_pattern.search(line))]
wind_d_value_d4_h24= [str(match.group(1)) for line in found_d4_h24 if (match := wind_d_pattern.search(line))]
wind_b_value_d4_h24 = [float(match.group(1)) for line in found_d4_h24 if (match := wind_b_pattern.search(line))]
wind_b_d4_h24_float_values_d4_h24 = [item for item in wind_b_value_d4_h24 if isinstance(item, float)]
wind_b_k_value_d4_h24 = [item * 1.944 for item in wind_b_d4_h24_float_values_d4_h24]
wind_g_value_d4_h24= [float(match.group(1)) for line in found_d4_h24 if (match := wind_g_pattern.search(line))]
wind_g_float_values_d4_h24 = [item for item in wind_g_value_d4_h24 if isinstance(item, float)]
wind_g_k_value_d4_h24=[item * 1.944 for item in wind_g_float_values_d4_h24]
wind_bf_value_d4_h24= [int(match.group(1)) for line in found_d4_h24 if (match := wind_bf_pattern.search(line))]
#print("Celsius values:", celsius_value_d4_h24)
#print("wind direction: ",wind_d_value_d4_h24)
#print("wind blow in mps: ",wind_b_value_d4_h24)
#print("wind blow in kts: ",wind_b_k_value_d4_h24)
#print("beaufort scale: ",wind_bf_value_d4_h24)
#print("wind gust in mps: ",wind_g_value_d4_h24)
#print("wind gust in knots: ", wind_g_k_value_d4_h24)
# Example Python file (example_file.py)

global_var = "I am a global variable"

def my_function():
    local_var = "I am a local variable"
    print(local_var)

# List all variables in the file
#all_variables = [var for var in dir() if not callable(globals()[var]) and not var.startswith("__")]

# Print the list of variables
#print("All Variables with Count:")
#for count, variable in enumerate(all_variables, 1):
  #print(f"{count}. {variable}")
