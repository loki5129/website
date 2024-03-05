// read_variables.js

const { execSync } = require('child_process');

// Run the Python script and capture its output
const pythonScriptPath = 'weather_data.py';
const pythonCommand = `python3 ${pythonScriptPath}`;
const pythonOutput = execSync(pythonCommand, { encoding: 'utf-8' });

// Parse the Python output (assuming it's a valid JSON)
const pythonVariables = JSON.parse(pythonOutput);
function test(){
 var link = pythonVariables.txt_file_path
 document.getElementById("test").innerHTML = link;
}
// Access the variables
console.log('Variable 1:', pythonVariables.txt_file_path);

