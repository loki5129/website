
// Function to fetch JSON data
async function fetchJsonData(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to fetch JSON: ${response.statusText}`);
  }
  return response.json();
}

// URL of the external JSON file
const jsonUrl = 'pot.json';  // Replace with the actual path to your JSON file

// Fetch JSON data
fetchJsonData(jsonUrl)
  .then(variableArray => {
    // Create an object to hold variables
    const variablesObject = {};

    // Display variables in the HTML and populate the variables object
    const variablesList = document.getElementById('variablesList');
    variableArray.forEach(variable => {
      const listItem = document.createElement('li');
      listItem.textContent = `${variable.key}: ${JSON.stringify(variable.value)}`;
      variablesList.appendChild(listItem);

      // Populate the variables object
      variablesObject[variable.key] = variable.value;
    });

    // Print the value of the variable with the key "h1"
    console.log(`Value of variable with key "h1": ${variablesObject.h1}`);

    // Assign the value of the variable with the key "celsius_value_c" to the JavaScript variable
    const celsius_value_c = variablesObject.celsius_value_c;
    console.log(`Value of celsius_value_c: ${celsius_value_c}`);

    const wind_d_value_c = variablesObject.wind_d_value_c;
    console.log(`Value of celsius_value_c: ${wind_d_value_c}`);
    const wind_b_mps_value_c = variablesObject.wind_b_value_c;
    console.log(`Value of celsius_value_c: ${wind_b_mps_value_c}`);
    const wind_b_k_value_c = variablesObject.wind_b_k_value_c;
    console.log(`Value of celsius_value_c: ${wind_b_k_value_c}`);
    const wind_g_mps_value_c = variablesObject.wind_g_value_c;
    console.log(`Value of celsius_value_c: ${wind_g_mps_value_c}`);
    const wind_g_k_value_c = variablesObject.wind_g_k_value_c;
    console.log(`Value of celsius_value_c: ${wind_g_k_value_c}`);
    const wind_bf_value_c = variablesObject.wind_bf_value_c;
    console.log(`Value of celsius_value_c: ${wind_bf_value_c}`);
    
    


    console.log('Variables displayed successfully!');
  })
  .catch(error => console.error(error));
