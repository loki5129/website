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


def separate_object_parts(json_object):
    separated_objects = [{"key": key, "value": value} for key, value in json_object.items()]
    return separated_objects

def write_objects_to_file(objects, output_file):
    with open(output_file, 'w') as file:
        json.dump(objects, file, indent=2)

def main():
    file_path = "var.json"
    output_file = "pot.json"

    try:
        with open(file_path, 'r') as file:
            json_str = file.read()
            json_object = json.loads(json_str)
            if isinstance(json_object, dict):
                separated_objects = separate_object_parts(json_object)
                #print("Separated object parts:")
                #for obj in separated_objects:
                    #print(json.dumps(obj, indent=2))

                write_objects_to_file(separated_objects, output_file)
                print(f"Separated objects written to {output_file}")
            else:
                print("The content of the file is not a valid JSON object.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check if the file contains a valid JSON object.")

if __name__ == "__main__":
    main()
