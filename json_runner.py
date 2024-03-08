import json
from weather_data import *
def serialize(obj):
    if isinstance(obj, (int, float, str, list, dict, bool, type(None))):
        return obj
    elif callable(obj):
        return None  # Exclude callable objects (functions, classes, etc.)
    else:
        return str(obj)  # Convert other types to string

# Sample variables
var1 = 42
var2 = "Hello, World!"
var3 = [1, 2, 3]
var4 = {"key": "value"}

# Get all local variables and their values
all_variables = {var_name: var_value for var_name, var_value in locals().items()}

# Specify the JSON file path
json_file_path = "var.json"

# Write the variables to a JSON file using the custom serializer
with open(json_file_path, 'w') as json_file:
    json.dump(all_variables, json_file, default=serialize, indent=4)

print(f"All variables and values exported to {json_file_path}")
