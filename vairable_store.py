from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Define your variables here
    variable1 = "Hello"
    variable2 = "World"
    variable3 = 42
    
    # Pass all variables to the HTML template
    return render_template('index.html', variables=dict(variable1=variable1, variable2=variable2, variable3=variable3))

if __name__ == '__main__':
    app.run(debug=True)
