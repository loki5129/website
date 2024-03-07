# app.py
import sys
from flask import Flask, render_template, jsonify
sys.path.append('C:\\Users\\tjbwa\\Downloads\\website-main\\website-main')
from weather_data import *
app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    # Assuming you have some variables defined in your local scope
    # Collect all local variables in the current function
    local_var = globals()

    # Create a dictionary containing all variables
    data = {key: value for key, value in local_var.items() if key != 'data'}

    # Render the template and pass the data to it
    return render_template('template.html', data=data)

if __name__ == '__main__':
    app.run()
