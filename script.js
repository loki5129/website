
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

    variableArray.forEach(variable => {
    

      // Populate the variables object
      variablesObject[variable.key] = variable.value;
    });

    // Print the value of the variable with the key "h1"
    //console.log(`Value of variable with key "h1": ${variablesObject.h1}`);

    // Assign the value of the variable with the key "celsius_value_c" to the JavaScript variable
    const celsius_value_c = variablesObject.celsius_value_c;
    const wind_D_value_c = variablesObject.wind_d_value_c;
    const wind_B_value_c=variablesObject.wind_b_value_c;
    const wind_bk_value_c=variablesObject.wind_b_k_value_c;
    const wind_G_value_c=variablesObject.wind_g_value_c;
    const wind_GK_value_c = variablesObject.wind_g_k_value_c;
    const wind_BF_value_c = variablesObject.wind_bf_value_c;
    document.getElementById("temperature").textContent= celsius_value_c;
    document.getElementById("wind direction").textContent = wind_D_value_c;
    document.getElementById("wind speed in mps").textContent= wind_B_value_c;
    document.getElementById("wind speed in kts").textContent= wind_bk_value_c;
    document.getElementById("wind gust in mps").textContent = wind_G_value_c;
    document.getElementById("wind gust in kts").textContent = wind_GK_value_c;
    document.getElementById("beaufort scale").textContent = wind_BF_value_c;

    const celsius_value_h1 = variablesObject.celsius_value_h1;
const wind_D_value_h1 = variablesObject.wind_d_value_h1;
const wind_B_value_h1 = variablesObject.wind_b_value_h1;
const wind_bk_value_h1 = variablesObject.wind_b_k_value_h1;
const wind_G_value_h1 = variablesObject.wind_g_value_h1;
const wind_GK_value_h1 = variablesObject.wind_g_k_value_h1;
const wind_BF_value_h1 = variablesObject.wind_bf_value_h1;
document.getElementById("temperature h1").textContent = celsius_value_h1;
document.getElementById("wind direction h1").textContent = wind_D_value_h1;
document.getElementById("wind speed in mps h1").textContent = wind_B_value_h1;
document.getElementById("wind speed in kts h1").textContent = wind_bk_value_h1;
document.getElementById("wind gust in mps h1").textContent = wind_G_value_h1;
document.getElementById("wind gust in kts h1").textContent = wind_GK_value_h1;
document.getElementById("beaufort scale h1").textContent = wind_BF_value_h1;

 
const celsius_value_h2 = variablesObject.celsius_value_h2;
const wind_D_value_h2 = variablesObject.wind_d_value_h2;
const wind_B_value_h2 = variablesObject.wind_b_value_h2;
const wind_bk_value_h2 = variablesObject.wind_b_k_value_h2;
const wind_G_value_h2 = variablesObject.wind_g_value_h2;
const wind_GK_value_h2 = variablesObject.wind_g_k_value_h2;
const wind_BF_value_h2 = variablesObject.wind_bf_value_h2;
document.getElementById("temperature h2").textContent = celsius_value_h2 + "C";
document.getElementById("wind direction h2").textContent = wind_D_value_h2;
document.getElementById("wind speed in mps h2").textContent = wind_B_value_h2 + "mps";
document.getElementById("wind speed in kts h2").textContent = wind_bk_value_h2+ "kts";
document.getElementById("wind gust in mps h2").textContent = wind_G_value_h2+"mps";
document.getElementById("wind gust in kts h2").textContent = wind_GK_value_h2 + "kts";
document.getElementById("beaufort scale h2").textContent = wind_BF_value_h2;


const celsius_value_h3 = variablesObject.celsius_value_h3;
const wind_D_value_h3 = variablesObject.wind_d_value_h3;
const wind_B_value_h3 = variablesObject.wind_b_value_h3;
const wind_bk_value_h3 = variablesObject.wind_b_k_value_h3;
const wind_G_value_h3 = variablesObject.wind_g_value_h3;
const wind_GK_value_h3 = variablesObject.wind_g_k_value_h3;
const wind_BF_value_h3 = variablesObject.wind_bf_value_h3;


const celsius_value_h4 = variablesObject.celsius_value_h4;
const wind_D_value_h4 = variablesObject.wind_d_value_h4;
const wind_B_value_h4 = variablesObject.wind_b_value_h4;
const wind_bk_value_h4 = variablesObject.wind_b_k_value_h4;
const wind_G_value_h4 = variablesObject.wind_g_value_h4;
const wind_GK_value_h4 = variablesObject.wind_g_k_value_h4;
const wind_BF_value_h4 = variablesObject.wind_bf_value_h4;

const celsius_value_h5 = variablesObject.celsius_value_h5;
const wind_D_value_h5 = variablesObject.wind_d_value_h5;
const wind_B_value_h5 = variablesObject.wind_b_value_h5;
const wind_bk_value_h5 = variablesObject.wind_b_k_value_h5;
const wind_G_value_h5 = variablesObject.wind_g_value_h5;
const wind_GK_value_h5 = variablesObject.wind_g_k_value_h5;
const wind_BF_value_h5 = variablesObject.wind_bf_value_h5;

const celsius_value_h6 = variablesObject.celsius_value_h6;
const wind_D_value_h6 = variablesObject.wind_d_value_h6;
const wind_B_value_h6 = variablesObject.wind_b_value_h6;
const wind_bk_value_h6 = variablesObject.wind_b_k_value_h6;
const wind_G_value_h6 = variablesObject.wind_g_value_h6;
const wind_GK_value_h6 = variablesObject.wind_g_k_value_h6;
const wind_BF_value_h6 = variablesObject.wind_bf_value_h6;

const celsius_value_h7 = variablesObject.celsius_value_h7;
const wind_D_value_h7 = variablesObject.wind_d_value_h7;
const wind_B_value_h7 = variablesObject.wind_b_value_h7;
const wind_bk_value_h7 = variablesObject.wind_b_k_value_h7;
const wind_G_value_h7 = variablesObject.wind_g_value_h7;
const wind_GK_value_h7 = variablesObject.wind_g_k_value_h7;
const wind_BF_value_h7 = variablesObject.wind_bf_value_h7;

const celsius_value_h8 = variablesObject.celsius_value_h8;
const wind_D_value_h8 = variablesObject.wind_d_value_h8;
const wind_B_value_h8 = variablesObject.wind_b_value_h8;
const wind_bk_value_h8 = variablesObject.wind_b_k_value_h8;
const wind_G_value_h8 = variablesObject.wind_g_value_h8;
const wind_GK_value_h8 = variablesObject.wind_g_k_value_h8;
const wind_BF_value_h8 = variablesObject.wind_bf_value_h8;

const celsius_value_h9 = variablesObject.celsius_value_h9;
const wind_D_value_h9 = variablesObject.wind_d_value_h9;
const wind_B_value_h9 = variablesObject.wind_b_value_h9;
const wind_bk_value_h9 = variablesObject.wind_b_k_value_h9;
const wind_G_value_h9 = variablesObject.wind_g_value_h9;
const wind_GK_value_h9 = variablesObject.wind_g_k_value_h9;
const wind_BF_value_h9 = variablesObject.wind_bf_value_h9;

const celsius_value_h10 = variablesObject.celsius_value_h10;
const wind_D_value_h10 = variablesObject.wind_d_value_h10;
const wind_B_value_h10 = variablesObject.wind_b_value_h10;
const wind_bk_value_h10 = variablesObject.wind_b_k_value_h10;
const wind_G_value_h10 = variablesObject.wind_g_value_h10;
const wind_GK_value_h10 = variablesObject.wind_g_k_value_h10;
const wind_BF_value_h10 = variablesObject.wind_bf_value_h10;

const celsius_value_h11 = variablesObject.celsius_value_h11;
const wind_D_value_h11 = variablesObject.wind_d_value_h11;
const wind_B_value_h11 = variablesObject.wind_b_value_h11;
const wind_bk_value_h11 = variablesObject.wind_b_k_value_h11;
const wind_G_value_h11 = variablesObject.wind_g_value_h11;
const wind_GK_value_h11 = variablesObject.wind_g_k_value_h11;
const wind_BF_value_h11 = variablesObject.wind_bf_value_h11;

const celsius_value_h12 = variablesObject.celsius_value_h12;
const wind_D_value_h12 = variablesObject.wind_d_value_h12;
const wind_B_value_h12 = variablesObject.wind_b_value_h12;
const wind_bk_value_h12 = variablesObject.wind_b_k_value_h12;
const wind_G_value_h12 = variablesObject.wind_g_value_h12;
const wind_GK_value_h12 = variablesObject.wind_g_k_value_h12;
const wind_BF_value_h12 = variablesObject.wind_bf_value_h12;

const celsius_value_h13 = variablesObject.celsius_value_h13;
const wind_D_value_h13 = variablesObject.wind_d_value_h13;
const wind_B_value_h13 = variablesObject.wind_b_value_h13;
const wind_bk_value_h13 = variablesObject.wind_b_k_value_h13;
const wind_G_value_h13 = variablesObject.wind_g_value_h13;
const wind_GK_value_h13 = variablesObject.wind_g_k_value_h13;
const wind_BF_value_h13 = variablesObject.wind_bf_value_h13;
    console.log('Variables displayed successfully!');
  })
  .catch(error => console.error(error));

