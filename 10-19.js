
// Function to fetch JSON data
async function fetchJsonData(url) {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Failed to fetch JSON: ${response.statusText}`);
    }
    return response.json();
  }
  const d = new Date();
let hour = d.getHours() +11;
console.log(hour)
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









const celsius_value_h10 = variablesObject.celsius_value_h13;
const wind_D_value_h10 = variablesObject.wind_d_value_h10;
const wind_B_value_h10 = variablesObject.wind_b_value_h10;
const wind_bk_value_h10 = variablesObject.wind_b_k_value_h10;
const wind_G_value_h10 = variablesObject.wind_g_value_h10;
const wind_GK_value_h10 = variablesObject.wind_g_k_value_h10;
const wind_BF_value_h10 = variablesObject.wind_bf_value_h10;
document.getElementById("temperature h10").textContent = celsius_value_h10 + "C";
document.getElementById("wind direction h10").textContent = wind_D_value_h10;
document.getElementById("wind speed in mps h10").textContent = wind_B_value_h10 + "mps";
document.getElementById("wind speed in kts h10").textContent = wind_bk_value_h10 + "kts";
document.getElementById("wind gust in mps h10").textContent = wind_G_value_h10 + "mps";
document.getElementById("wind gust in kts h10").textContent = wind_GK_value_h10 + "kts";
document.getElementById("beaufort scale h10").textContent = wind_BF_value_h10; 

const celsius_value_h11 = variablesObject.celsius_value_h11;
const wind_D_value_h11 = variablesObject.wind_d_value_h11;
const wind_B_value_h11 = variablesObject.wind_b_value_h11;
const wind_bk_value_h11 = variablesObject.wind_b_k_value_h11;
const wind_G_value_h11 = variablesObject.wind_g_value_h11;
const wind_GK_value_h11 = variablesObject.wind_g_k_value_h11;
const wind_BF_value_h11 = variablesObject.wind_bf_value_h11;
document.getElementById("temperature h11").textContent = celsius_value_h11 + "C";
document.getElementById("wind direction h11").textContent = wind_D_value_h11;
document.getElementById("wind speed in mps h11").textContent = wind_B_value_h11 + "mps";
document.getElementById("wind speed in kts h11").textContent = wind_bk_value_h11 + "kts";
document.getElementById("wind gust in mps h11").textContent = wind_G_value_h11 + "mps";
document.getElementById("wind gust in kts h11").textContent = wind_GK_value_h11 + "kts";
document.getElementById("beaufort scale h11").textContent = wind_BF_value_h11; 
const celsius_value_h12 = variablesObject.celsius_value_h12;
const wind_D_value_h12 = variablesObject.wind_d_value_h12;
const wind_B_value_h12 = variablesObject.wind_b_value_h12;
const wind_bk_value_h12 = variablesObject.wind_b_k_value_h12;
const wind_G_value_h12 = variablesObject.wind_g_value_h12;
const wind_GK_value_h12 = variablesObject.wind_g_k_value_h12;
const wind_BF_value_h12 = variablesObject.wind_bf_value_h12;
document.getElementById("temperature h12").textContent = celsius_value_h12 + "C";
document.getElementById("wind direction h12").textContent = wind_D_value_h12;
document.getElementById("wind speed in mps h12").textContent = wind_B_value_h12 + "mps";
document.getElementById("wind speed in kts h12").textContent = wind_bk_value_h12 + "kts";
document.getElementById("wind gust in mps h12").textContent = wind_G_value_h12 + "mps";
document.getElementById("wind gust in kts h12").textContent = wind_GK_value_h12 + "kts";
document.getElementById("beaufort scale h12").textContent = wind_BF_value_h12; 

const celsius_value_h13 = variablesObject.celsius_value_h13;
const wind_D_value_h13 = variablesObject.wind_d_value_h13;
const wind_B_value_h13 = variablesObject.wind_b_value_h13;
const wind_bk_value_h13 = variablesObject.wind_b_k_value_h13;
const wind_G_value_h13 = variablesObject.wind_g_value_h13;
const wind_GK_value_h13 = variablesObject.wind_g_k_value_h13;
const wind_BF_value_h13 = variablesObject.wind_bf_value_h13;
document.getElementById("temperature h13").textContent = celsius_value_h13 + "C";
document.getElementById("wind direction h13").textContent = wind_D_value_h13;
document.getElementById("wind speed in mps h13").textContent = wind_B_value_h13 + "mps";
document.getElementById("wind speed in kts h13").textContent = wind_bk_value_h13 + "kts";
document.getElementById("wind gust in mps h13").textContent = wind_G_value_h13 + "mps";
document.getElementById("wind gust in kts h13").textContent = wind_GK_value_h13 + "kts";
document.getElementById("beaufort scale h13").textContent = wind_BF_value_h13; 

const celsius_value_d2_h1 = variablesObject.celsius_value_d2_h1;
const wind_D_value_d2_h1 = variablesObject.wind_d_value_d2_h1;
const wind_B_value_d2_h1 = variablesObject.wind_b_value_d2_h1;
const wind_BK_value_d2_h1 = variablesObject.wind_b_k_value_d2_h1;
const wind_G_value_d2_h1 = variablesObject.wind_g_value_d2_h1;
const wind_GK_value_d2_h1 = variablesObject.wind_g_k_value_d2_h1;
const wind_BF_value_d2_h1 = variablesObject.wind_bf_value_d2_h1;
document.getElementById("temperature h14").textContent = celsius_value_d2_h1 + "C";
document.getElementById("wind direction h14").textContent = wind_D_value_d2_h1;
document.getElementById("wind speed in mps h14").textContent = wind_B_value_d2_h1 + "mps";
document.getElementById("wind speed in kts h14").textContent = wind_BK_value_d2_h1 + "kts";
document.getElementById("wind gust in mps h14").textContent = wind_G_value_d2_h1 + "mps";
document.getElementById("wind gust in kts h14").textContent = wind_GK_value_d2_h1 + "kts";
document.getElementById("beaufort scale h14").textContent = wind_BF_value_d2_h1; 


const celsius_value_d2_h2 = variablesObject.celsius_value_d2_h2;
const wind_D_value_d2_h2 = variablesObject.wind_d_value_d2_h2;
const wind_B_value_d2_h2 = variablesObject.wind_b_value_d2_h2;
const wind_BK_value_d2_h2 = variablesObject.wind_b_k_value_d2_h2;
const wind_G_value_d2_h2 = variablesObject.wind_g_value_d2_h2;
const wind_GK_value_d2_h2 = variablesObject.wind_g_k_value_d2_h2;
const wind_BF_value_d2_h2 = variablesObject.wind_bf_value_d2_h2;

document.getElementById("temperature h15").textContent = celsius_value_d2_h2 + "C";
document.getElementById("wind direction h15").textContent = wind_D_value_d2_h2;
document.getElementById("wind speed in mps h15").textContent = wind_B_value_d2_h2 + "mps";
document.getElementById("wind speed in kts h15").textContent = wind_BK_value_d2_h2 + "kts";
document.getElementById("wind gust in mps h15").textContent = wind_G_value_d2_h2 + "mps";
document.getElementById("wind gust in kts h15").textContent = wind_GK_value_d2_h2 + "kts";
document.getElementById("beaufort scale h15").textContent = wind_BF_value_d2_h2; 

const celsius_value_d2_h3 = variablesObject.celsius_value_d2_h3;
const wind_D_value_d2_h3 = variablesObject.wind_d_value_d2_h3;
const wind_B_value_d2_h3 = variablesObject.wind_b_value_d2_h3;
const wind_BK_value_d2_h3 = variablesObject.wind_b_k_value_d2_h3;
const wind_G_value_d2_h3 = variablesObject.wind_g_value_d2_h3;
const wind_GK_value_d2_h3 = variablesObject.wind_g_k_value_d2_h3;
const wind_BF_value_d2_h3 = variablesObject.wind_bf_value_d2_h3;

document.getElementById("temperature h16").textContent = celsius_value_d2_h3 + "C";
document.getElementById("wind direction h16").textContent = wind_D_value_d2_h3;
document.getElementById("wind speed in mps h16").textContent = wind_B_value_d2_h3 + "mps";
document.getElementById("wind speed in kts h16").textContent = wind_BK_value_d2_h3 + "kts";
document.getElementById("wind gust in mps h16").textContent = wind_G_value_d2_h3 + "mps";
document.getElementById("wind gust in kts h16").textContent = wind_GK_value_d2_h3 + "kts";
document.getElementById("beaufort scale h16").textContent = wind_BF_value_d2_h3; 

const celsius_value_d2_h4 = variablesObject.celsius_value_d2_h4;
const wind_D_value_d2_h4 = variablesObject.wind_d_value_d2_h4;
const wind_B_value_d2_h4 = variablesObject.wind_b_value_d2_h4;
const wind_BK_value_d2_h4 = variablesObject.wind_b_k_value_d2_h4;
const wind_G_value_d2_h4 = variablesObject.wind_g_value_d2_h4;
const wind_GK_value_d2_h4 = variablesObject.wind_g_k_value_d2_h4;
const wind_BF_value_d2_h4 = variablesObject.wind_bf_value_d2_h4;

document.getElementById("temperature h17").textContent = celsius_value_d2_h4 + "C";
document.getElementById("wind direction h17").textContent = wind_D_value_d2_h4;
document.getElementById("wind speed in mps h17").textContent = wind_B_value_d2_h4 + "mps";
document.getElementById("wind speed in kts h17").textContent = wind_BK_value_d2_h4 + "kts";
document.getElementById("wind gust in mps h17").textContent = wind_G_value_d2_h4 + "mps";
document.getElementById("wind gust in kts h17").textContent = wind_GK_value_d2_h4 + "kts";
document.getElementById("beaufort scale h17").textContent = wind_BF_value_d2_h4; 

const celsius_value_d2_h5 = variablesObject.celsius_value_d2_h5;
const wind_D_value_d2_h5 = variablesObject.wind_d_value_d2_h5;
const wind_B_value_d2_h5 = variablesObject.wind_b_value_d2_h5;
const wind_BK_value_d2_h5 = variablesObject.wind_b_k_value_d2_h5;
const wind_G_value_d2_h5 = variablesObject.wind_g_value_d2_h5;
const wind_GK_value_d2_h5 = variablesObject.wind_g_k_value_d2_h5;
const wind_BF_value_d2_h5 = variablesObject.wind_bf_value_d2_h5;

document.getElementById("temperature h18").textContent = celsius_value_d2_h5 + "C";
document.getElementById("wind direction h18").textContent = wind_D_value_d2_h5;
document.getElementById("wind speed in mps h18").textContent = wind_B_value_d2_h5 + "mps";
document.getElementById("wind speed in kts h18").textContent = wind_BK_value_d2_h5 + "kts";
document.getElementById("wind gust in mps h18").textContent = wind_G_value_d2_h5 + "mps";
document.getElementById("wind gust in kts h18").textContent = wind_GK_value_d2_h5 + "kts";
document.getElementById("beaufort scale h18").textContent = wind_BF_value_d2_h5; 


const celsius_value_d2_h6 = variablesObject.celsius_value_d2_h6;
const wind_D_value_d2_h6 = variablesObject.wind_d_value_d2_h6;
const wind_B_value_d2_h6 = variablesObject.wind_b_value_d2_h6;
const wind_BK_value_d2_h6 = variablesObject.wind_b_k_value_d2_h6;
const wind_G_value_d2_h6 = variablesObject.wind_g_value_d2_h6;
const wind_GK_value_d2_h6 = variablesObject.wind_g_k_value_d2_h6;
const wind_BF_value_d2_h6 = variablesObject.wind_bf_value_d2_h6;

document.getElementById("temperature h19").textContent = celsius_value_d2_h6 + "C";
document.getElementById("wind direction h19").textContent = wind_D_value_d2_h6;
document.getElementById("wind speed in mps h19").textContent = wind_B_value_d2_h6 + "mps";
document.getElementById("wind speed in kts h19").textContent = wind_BK_value_d2_h6 + "kts";
document.getElementById("wind gust in mps h19").textContent = wind_G_value_d2_h6 + "mps";
document.getElementById("wind gust in kts h19").textContent = wind_GK_value_d2_h6 + "kts";
document.getElementById("beaufort scale h19").textContent = wind_BF_value_d2_h6; 

    console.log('Variables displayed successfully!');
  })
  .catch(error => console.error(error));

