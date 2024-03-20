
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

const d = new Date();
let hour = d.getHours() +1;
console.log(hour);

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

    function resetNumber(number) {
      return number % 24;
    }
    
  

    
    
    // Example usage:


document.getElementById("date").textContent= hour +":00";
hour = hour +1 
hour = resetNumber(hour)
document.getElementById("1time").textContent= hour +":00";
hour = hour +1 ;
hour = resetNumber(hour);
document.getElementById("2time").textContent= hour +":00";
hour = hour +1;
hour = resetNumber(hour);
document.getElementById("3time").textContent= hour +":00";
hour = hour +1;
hour = resetNumber(hour);
document.getElementById("4time").textContent= hour +":00";
hour = hour +1;
hour = resetNumber(hour);
document.getElementById("5time").textContent= hour +":00";
hour = hour +1;
hour = resetNumber(hour);
document.getElementById("6time").textContent= hour +":00";
hour = hour +1;
hour = resetNumber(hour);
document.getElementById("7time").textContent= hour +":00";
hour = hour +1;
hour = resetNumber(hour);
document.getElementById("8time").textContent= hour +":00";
hour = hour +1;
hour = resetNumber(hour);
document.getElementById("9time").textContent= hour +":00";
    const celsius_value_c = variablesObject.celsius_value_c;
    const wind_D_value_c = variablesObject.wind_d_value_c;
    const wind_B_value_c=variablesObject.wind_b_value_c;
    const wind_bk_value_c=variablesObject.wind_b_k_value_c;
    const wind_G_value_c=variablesObject.wind_g_value_c;
    const wind_GK_value_c = variablesObject.wind_g_k_value_c;
    const wind_BF_value_c = variablesObject.wind_bf_value_c;
    document.getElementById("temperature").textContent= celsius_value_c + "C";
    document.getElementById("wind direction").textContent = wind_D_value_c ;
    document.getElementById("wind speed in mps").textContent= wind_B_value_c + "mps";
    document.getElementById("wind speed in kts").textContent= wind_bk_value_c + "kts";
    document.getElementById("wind gust in mps").textContent = wind_G_value_c + "mps";
    document.getElementById("wind gust in kts").textContent = wind_GK_value_c + "kts";
    document.getElementById("beaufort scale").textContent = wind_BF_value_c;

    const celsius_value_h1 = variablesObject.celsius_value_h1;
const wind_D_value_h1 = variablesObject.wind_d_value_h1;
const wind_B_value_h1 = variablesObject.wind_b_value_h1;
const wind_bk_value_h1 = variablesObject.wind_b_k_value_h1;
const wind_G_value_h1 = variablesObject.wind_g_value_h1;
const wind_GK_value_h1 = variablesObject.wind_g_k_value_h1;
const wind_BF_value_h1 = variablesObject.wind_bf_value_h1;
document.getElementById("temperature h1").textContent = celsius_value_h1 + "C";
document.getElementById("wind direction h1").textContent = wind_D_value_h1;
document.getElementById("wind speed in mps h1").textContent = wind_B_value_h1 + "mps";
document.getElementById("wind speed in kts h1").textContent = wind_bk_value_h1 + "kts";
document.getElementById("wind gust in mps h1").textContent = wind_G_value_h1 + "mps";
document.getElementById("wind gust in kts h1").textContent = wind_GK_value_h1 + "kts";
document.getElementById("beaufort scale h1").textContent = wind_BF_value_h1;

const celsius_value_h2 = variablesObject.celsius_value_h2;
const wind_D_value_h2 = variablesObject.wind_d_value_h2;
console.log(wind_BF_value_h1);
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

document.getElementById("temperature h3").textContent = celsius_value_h3 + "C";
document.getElementById("wind direction h3").textContent = wind_D_value_h3;
document.getElementById("wind speed in mps h3").textContent = wind_B_value_h3 + "mps";
document.getElementById("wind speed in kts h3").textContent = wind_bk_value_h3+ "kts";
document.getElementById("wind gust in mps h3").textContent = wind_G_value_h3+"mps";
document.getElementById("wind gust in kts h3").textContent = wind_GK_value_h3 + "kts";
document.getElementById("beaufort scale h3").textContent = wind_BF_value_h3;


const celsius_value_h4 = variablesObject.celsius_value_h4;
const wind_D_value_h4 = variablesObject.wind_d_value_h4;
const wind_B_value_h4 = variablesObject.wind_b_value_h4;
const wind_bk_value_h4 = variablesObject.wind_b_k_value_h4;
const wind_G_value_h4 = variablesObject.wind_g_value_h4;
const wind_GK_value_h4 = variablesObject.wind_g_k_value_h4;
const wind_BF_value_h4 = variablesObject.wind_bf_value_h4;

document.getElementById("temperature h4").textContent = celsius_value_h4 + "C";
document.getElementById("wind direction h4").textContent = wind_D_value_h4;
document.getElementById("wind speed in mps h4").textContent = wind_B_value_h4 + "mps";
document.getElementById("wind speed in kts h4").textContent = wind_bk_value_h4+ "kts";
document.getElementById("wind gust in mps h4").textContent = wind_G_value_h4+"mps";
document.getElementById("wind gust in kts h4").textContent = wind_GK_value_h4 + "kts";
document.getElementById("beaufort scale h4").textContent = wind_BF_value_h4;


const celsius_value_h5 = variablesObject.celsius_value_h5;
const wind_D_value_h5 = variablesObject.wind_d_value_h5;
const wind_B_value_h5 = variablesObject.wind_b_value_h5;
const wind_bk_value_h5 = variablesObject.wind_b_k_value_h5;
const wind_G_value_h5 = variablesObject.wind_g_value_h5;
const wind_GK_value_h5 = variablesObject.wind_g_k_value_h5;
const wind_BF_value_h5 = variablesObject.wind_bf_value_h5;

document.getElementById("temperature h5").textContent = celsius_value_h5 + "C";
document.getElementById("wind direction h5").textContent = wind_D_value_h5;
document.getElementById("wind speed in mps h5").textContent = wind_B_value_h5 + "mps";
document.getElementById("wind speed in kts h5").textContent = wind_bk_value_h5+ "kts";
document.getElementById("wind gust in mps h5").textContent = wind_G_value_h5+"mps";
document.getElementById("wind gust in kts h5").textContent = wind_GK_value_h5 + "kts";
document.getElementById("beaufort scale h5").textContent = wind_BF_value_h5;

const celsius_value_h6 = variablesObject.celsius_value_h6;
const wind_D_value_h6 = variablesObject.wind_d_value_h6;
const wind_B_value_h6 = variablesObject.wind_b_value_h6;
const wind_bk_value_h6 = variablesObject.wind_b_k_value_h6;
const wind_G_value_h6 = variablesObject.wind_g_value_h6;
const wind_GK_value_h6 = variablesObject.wind_g_k_value_h6;
const wind_BF_value_h6 = variablesObject.wind_bf_value_h6;
document.getElementById("temperature h6").textContent = celsius_value_h6 + "C";
document.getElementById("wind direction h6").textContent = wind_D_value_h6;
document.getElementById("wind speed in mps h6").textContent = wind_B_value_h6 + "mps";
document.getElementById("wind speed in kts h6").textContent = wind_bk_value_h6+ "kts";
document.getElementById("wind gust in mps h6").textContent = wind_G_value_h6+"mps";
document.getElementById("wind gust in kts h6").textContent = wind_GK_value_h6 + "kts";
document.getElementById("beaufort scale h6").textContent = wind_BF_value_h6;


const celsius_value_h7 = variablesObject.celsius_value_h7;
const wind_D_value_h7 = variablesObject.wind_d_value_h7;
const wind_B_value_h7 = variablesObject.wind_b_value_h7;
const wind_bk_value_h7 = variablesObject.wind_b_k_value_h7;
const wind_G_value_h7 = variablesObject.wind_g_value_h7;
const wind_GK_value_h7 = variablesObject.wind_g_k_value_h7;
const wind_BF_value_h7 = variablesObject.wind_bf_value_h7;
document.getElementById("temperature h7").textContent = celsius_value_h7 + "C";
document.getElementById("wind direction h7").textContent = wind_D_value_h7;
document.getElementById("wind speed in mps h7").textContent = wind_B_value_h7 + "mps";
document.getElementById("wind speed in kts h7").textContent = wind_bk_value_h7+ "kts";
document.getElementById("wind gust in mps h7").textContent = wind_G_value_h7+"mps";
document.getElementById("wind gust in kts h7").textContent = wind_GK_value_h7 + "kts";
document.getElementById("beaufort scale h7").textContent = wind_BF_value_h7;

const celsius_value_h8 = variablesObject.celsius_value_h8;
const wind_D_value_h8 = variablesObject.wind_d_value_h8;
const wind_B_value_h8 = variablesObject.wind_b_value_h8;
const wind_bk_value_h8 = variablesObject.wind_b_k_value_h8;
const wind_G_value_h8 = variablesObject.wind_g_value_h8;
const wind_GK_value_h8 = variablesObject.wind_g_k_value_h8;
const wind_BF_value_h8 = variablesObject.wind_bf_value_h8;
document.getElementById("temperature h8").textContent = celsius_value_h8 + "C";
document.getElementById("wind direction h8").textContent = wind_D_value_h8;
document.getElementById("wind speed in mps h8").textContent = wind_B_value_h8 + "mps";
document.getElementById("wind speed in kts h8").textContent = wind_bk_value_h8+ "kts";
document.getElementById("wind gust in mps h8").textContent = wind_G_value_h8+"mps";
document.getElementById("wind gust in kts h8").textContent = wind_GK_value_h8 + "kts";
document.getElementById("beaufort scale h8").textContent = wind_BF_value_h8;


const celsius_value_h9 = variablesObject.celsius_value_h9;
const wind_D_value_h9 = variablesObject.wind_d_value_h9;
const wind_B_value_h9 = variablesObject.wind_b_value_h9;
const wind_bk_value_h9 = variablesObject.wind_b_k_value_h9;
const wind_G_value_h9 = variablesObject.wind_g_value_h9;
const wind_GK_value_h9 = variablesObject.wind_g_k_value_h9;
const wind_BF_value_h9 = variablesObject.wind_bf_value_h9;
document.getElementById("temperature h9").textContent = celsius_value_h9 + "C";
document.getElementById("wind direction h9").textContent = wind_D_value_h9;
document.getElementById("wind speed in mps h9").textContent = wind_B_value_h9 + "mps";
document.getElementById("wind speed in kts h9").textContent = wind_bk_value_h9+ "kts";
document.getElementById("wind gust in mps h9").textContent = wind_G_value_h9+"mps";
document.getElementById("wind gust in kts h9").textContent = wind_GK_value_h9 + "kts";
document.getElementById("beaufort scale h9").textContent = wind_BF_value_h9;
  })
  .catch(error => console.error(error));

