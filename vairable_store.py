from flask import Flask, render_template, jsonify
# target_module.py

from weather_data import *


app = Flask(__name__)

@app.route('/')
def index():
    # Define your variables here
    python_variable1 = "Hello"
    python_variable2 = 42

    # Return a template that includes JavaScript code
    return render_template('index.html', python_variable1=python_variable1, python_variable2=python_variable2)

if __name__ == '__main__':
    app.run(debug=True)
