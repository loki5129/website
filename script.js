
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

    // Function to fetch JSON data
    async function fetchJsonData(url) {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Failed to fetch JSON: ${response.statusText}`);
      }
      return response.json();
    }
    
    
    
    // Fetch JSON data
    fetchJsonData(jsonUrl)
      .then(variableArray => {
        // Create an object to hold variables
        const variablesObject = {};
    
        // Populate the variables object
        variableArray.forEach(variable => {
          variablesObject[variable.key] = variable.value;
    let celsius_value_c = variablesObject.celsius_value_c;
    //console.log(`Value of celsius_value_c: ${celsius_value_c}`);
    let wind_d_value_c = variablesObject.wind_d_value_c;
    //console.log(`Value of celsius_value_c: ${wind_d_value_c}`);
    let wind_b_mps_value_c = variablesObject.wind_b_value_c;
    //console.log(`Value of celsius_value_c: ${wind_b_mps_value_c}`);
    let wind_b_k_value_c = variablesObject.wind_b_k_value_c;
    //console.log(`Value of celsius_value_c: ${wind_b_k_value_c}`);
    let wind_g_mps_value_c = variablesObject.wind_g_value_c;
    //console.log(`Value of celsius_value_c: ${wind_g_mps_value_c}`);
    let wind_g_k_value_c = variablesObject.wind_g_k_value_c;
    //console.log(`Value of celsius_value_c: ${wind_g_k_value_c}`);
    let wind_bf_value_c = variablesObject.wind_bf_value_c;
    //console.log(`Value of celsius_value_c: ${wind_bf_value_c}`);
    // hour 1
   let celsius_value_h1 =variablesObject.celsius_value_h1;
   //console.log(`Value of celsius_value_h1: ${celsius_value_h1}`);
   let wind_d_value_h1 = variablesObject.wind_d_value_h1;
   //console.log(`Value of celsius_value_h1: ${wind_d_value_h1}`);
   let wind_b_mps_value_h1 = variablesObject.wind_b_value_h1;
   //console.log(`Value of celsius_value_h1: ${wind_b_mps_value_h1}`);
   let wind_b_k_value_h1 = variablesObject.wind_b_k_value_h1;
   //console.log(`Value of celsius_value_h1: ${wind_b_k_value_h1}`);
   let wind_g_mps_value_h1 = variablesObject.wind_g_value_h1;
   //console.log(`Value of celsius_value_h1: ${wind_g_mps_value_h1}`);
   let wind_g_k_value_h1 = variablesObject.wind_g_k_value_h1;
   //console.log(`Value of celsius_value_h1: ${wind_g_k_value_h1}`);
   let wind_bf_value_h1 = variablesObject.wind_bf_value_h1;
   //console.log(`Value of celsius_value_h1: ${wind_bf_value_h1}`);

   let celsius_value_h2 = variablesObject.celsius_value_h2;
   //console.log(`Value of celsius_value_h2: ${celsius_value_h2}`);
   let wind_d_value_h2 = variablesObject.wind_d_value_h2;
   //console.log(`Value of celsius_value_h2: ${wind_d_value_h2}`);
   let wind_b_mps_value_h2 = variablesObject.wind_b_value_h2;
   //console.log(`Value of celsius_value_h2: ${wind_b_mps_value_h2}`);
   let wind_b_k_value_h2 = variablesObject.wind_b_k_value_h2;
   //console.log(`Value of celsius_value_h2: ${wind_b_k_value_h2}`);
   let wind_g_mps_value_h2 = variablesObject.wind_g_value_h2;
   //console.log(`Value of celsius_value_h2: ${wind_g_mps_value_h2}`);
   let wind_g_k_value_h2 = variablesObject.wind_g_k_value_h2;
   //console.log(`Value of celsius_value_h2: ${wind_g_k_value_h2}`);
   let wind_bf_value_h2 = variablesObject.wind_bf_value_h2;
   //console.log(`Value of celsius_value_h2: ${wind_bf_value_h2}`);

// Repeat the pattern for _h3 to _h10
   let celsius_value_h3 = variablesObject.celsius_value_h3;
   //console.log(`Value of celsius_value_h3: ${celsius_value_h3}`);
   let wind_d_value_h3 = variablesObject.wind_d_value_h3;
   //console.log(`Value of celsius_value_h3: ${wind_d_value_h3}`);
   let wind_b_mps_value_h3 = variablesObject.wind_b_value_h3;
   //console.log(`Value of celsius_value_h3: ${wind_b_mps_value_h3}`);
   let wind_b_k_value_h3 = variablesObject.wind_b_k_value_h3;
   //console.log(`Value of celsius_value_h3: ${wind_b_k_value_h3}`);
   let wind_g_mps_value_h3 = variablesObject.wind_g_value_h3;
   //console.log(`Value of celsius_value_h3: ${wind_g_mps_value_h3}`);
   let wind_g_k_value_h3 = variablesObject.wind_g_k_value_h3;
   //console.log(`Value of celsius_value_h3: ${wind_g_k_value_h3}`);
   let wind_bf_value_h3 = variablesObject.wind_bf_value_h3;
   //console.log(`Value of celsius_value_h3: ${wind_bf_value_h3}`);
   let celsius_value_h4 = variablesObject.celsius_value_h4;
   //console.log(`Value of celsius_value_c: ${celsius_value_h4}`);
   let wind_d_value_h4 = variablesObject.wind_d_value_h4;
   //console.log(`Value of celsius_value_h4: ${wind_d_value_h4}`);
   let wind_b_mps_value_h4 = variablesObject.wind_b_value_h4;
   //console.log(`Value of celsius_value_h4: ${wind_b_mps_value_h4}`);
   let wind_b_k_value_h4 = variablesObject.wind_b_k_value_h4;
   //console.log(`Value of celsius_value_h4: ${wind_b_k_value_h4}`);
   let wind_g_mps_value_h4 = variablesObject.wind_g_value_h4;
   //console.log(`Value of celsius_value_h4: ${wind_g_mps_value_h4}`);
   let wind_g_k_value_h4 = variablesObject.wind_g_k_value_h4;
   //console.log(`Value of celsius_value_h4: ${wind_g_k_value_h4}`);
   let wind_bf_value_h4 = variablesObject.wind_bf_value_h4;
   //console.log(`Value of celsius_value_h4: ${wind_bf_value_h4}`);

   // Repeat the pattern for _h5 to _h13
   let celsius_value_h5 = variablesObject.celsius_value_h5;
   //console.log(`Value of celsius_value_c: ${celsius_value_h5}`);
   let wind_d_value_h5 = variablesObject.wind_d_value_h5;
   //console.log(`Value of celsius_value_h5: ${wind_d_value_h5}`);
   let wind_b_mps_value_h5 = variablesObject.wind_b_value_h5;
   //console.log(`Value of celsius_value_h5: ${wind_b_mps_value_h5}`);
   let wind_b_k_value_h5 = variablesObject.wind_b_k_value_h5;
   //console.log(`Value of celsius_value_h5: ${wind_b_k_value_h5}`); 
   let wind_g_mps_value_h5 = variablesObject.wind_g_value_h5;
   //console.log(`Value of celsius_value_h5: ${wind_g_mps_value_h5}`);
   let wind_g_k_value_h5 = variablesObject.wind_g_k_value_h5;
   //console.log(`Value of celsius_value_h5: ${wind_g_k_value_h5}`);
   let wind_bf_value_h5 = variablesObject.wind_bf_value_h5;
   //console.log(`Value of celsius_value_h5: ${wind_bf_value_h5}`);
   let celsius_value_h6 = variablesObject.celsius_value_h6;
   //console.log(`Value of celsius_value_c: ${celsius_value_h6}`);
   let wind_d_value_h6 = variablesObject.wind_d_value_h6;
   //console.log(`Value of celsius_value_h6: ${wind_d_value_h6}`);
   let wind_b_mps_value_h6 = variablesObject.wind_b_value_h6;
   //console.log(`Value of celsius_value_h6: ${wind_b_mps_value_h6}`);
   let wind_b_k_value_h6 = variablesObject.wind_b_k_value_h6;
   //console.log(`Value of celsius_value_h6: ${wind_b_k_value_h6}`);
   let wind_g_mps_value_h6 = variablesObject.wind_g_value_h6;
   //console.log(`Value of celsius_value_h6: ${wind_g_mps_value_h6}`);
   let wind_g_k_value_h6 = variablesObject.wind_g_k_value_h6;
   //console.log(`Value of celsius_value_h6: ${wind_g_k_value_h6}`);
   let wind_bf_value_h6 = variablesObject.wind_bf_value_h6;
   //console.log(`Value of celsius_value_h6: ${wind_bf_value_h6}`);
   
   let celsius_value_h7 = variablesObject.celsius_value_h7;
   //console.log(`Value of celsius_value_c: ${celsius_value_h7}`);
   let wind_d_value_h7 = variablesObject.wind_d_value_h7;
   //console.log(`Value of celsius_value_h7: ${wind_d_value_h7}`);
   let wind_b_mps_value_h7 = variablesObject.wind_b_value_h7;
   //console.log(`Value of celsius_value_h7: ${wind_b_mps_value_h7}`);
   let wind_b_k_value_h7 = variablesObject.wind_b_k_value_h7;
   //console.log(`Value of celsius_value_h7: ${wind_b_k_value_h7}`);
   let wind_g_mps_value_h7 = variablesObject.wind_g_value_h7;
   //console.log(`Value of celsius_value_h7: ${wind_g_mps_value_h7}`);
   let wind_g_k_value_h7 = variablesObject.wind_g_k_value_h7;
   //console.log(`Value of celsius_value_h7: ${wind_g_k_value_h7}`);
   let wind_bf_value_h7 = variablesObject.wind_bf_value_h7;
   //console.log(`Value of celsius_value_h7: ${wind_bf_value_h7}`);
   
   let celsius_value_h8 = variablesObject.celsius_value_h8;
   //console.log(`Value of celsius_value_c: ${celsius_value_h8}`);
   let wind_d_value_h8 = variablesObject.wind_d_value_h8;
   //console.log(`Value of celsius_value_h8: ${wind_d_value_h8}`);
   let wind_b_mps_value_h8 = variablesObject.wind_b_value_h8;
   //console.log(`Value of celsius_value_h8: ${wind_b_mps_value_h8}`);
   let wind_b_k_value_h8 = variablesObject.wind_b_k_value_h8;
   //console.log(`Value of celsius_value_h8: ${wind_b_k_value_h8}`);
   let wind_g_mps_value_h8 = variablesObject.wind_g_value_h8;
   //console.log(`Value of celsius_value_h8: ${wind_g_mps_value_h8}`);
   let wind_g_k_value_h8 = variablesObject.wind_g_k_value_h8;
   //console.log(`Value of celsius_value_h8: ${wind_g_k_value_h8}`);
   let wind_bf_value_h8 = variablesObject.wind_bf_value_h8;
   //console.log(`Value of celsius_value_h8: ${wind_bf_value_h8}`);
   
   let celsius_value_h9 = variablesObject.celsius_value_h9;
   //console.log(`Value of celsius_value_c: ${celsius_value_h9}`);
   let wind_d_value_h9 = variablesObject.wind_d_value_h9;
   //console.log(`Value of celsius_value_h9: ${wind_d_value_h9}`);
   let wind_b_mps_value_h9 = variablesObject.wind_b_value_h9;
   //console.log(`Value of celsius_value_h9: ${wind_b_mps_value_h9}`);
   let wind_b_k_value_h9 = variablesObject.wind_b_k_value_h9;
   //console.log(`Value of celsius_value_h9: ${wind_b_k_value_h9}`);
   let wind_g_mps_value_h9 = variablesObject.wind_g_value_h9;
   //console.log(`Value of celsius_value_h9: ${wind_g_mps_value_h9}`);
   let wind_g_k_value_h9 = variablesObject.wind_g_k_value_h9;
   //console.log(`Value of celsius_value_h9: ${wind_g_k_value_h9}`);
   let wind_bf_value_h9 = variablesObject.wind_bf_value_h9;
   //console.log(`Value of celsius_value_h9: ${wind_bf_value_h9}`);
   
   let celsius_value_h10 = variablesObject.celsius_value_h10;
   //console.log(`Value of celsius_value_c: ${celsius_value_h10}`);
   let wind_d_value_h10 = variablesObject.wind_d_value_h10;
   //console.log(`Value of celsius_value_h10: ${wind_d_value_h10}`);
   let wind_b_mps_value_h10 = variablesObject.wind_b_value_h10;
   //console.log(`Value of celsius_value_h10: ${wind_b_mps_value_h10}`);
   let wind_b_k_value_h10 = variablesObject.wind_b_k_value_h10;
   //console.log(`Value of celsius_value_h10: ${wind_b_k_value_h10}`);
   let wind_g_mps_value_h10 = variablesObject.wind_g_value_h10;
   //console.log(`Value of celsius_value_h10: ${wind_g_mps_value_h10}`);
   let wind_g_k_value_h10 = variablesObject.wind_g_k_value_h10;
   //console.log(`Value of celsius_value_h10: ${wind_g_k_value_h10}`);
   let wind_bf_value_h10 = variablesObject.wind_bf_value_h10;
   //console.log(`Value of celsius_value_h10: ${wind_bf_value_h10}`);
   
   let celsius_value_h11 = variablesObject.celsius_value_h11;
   //console.log(`Value of celsius_value_c: ${celsius_value_h11}`);
   let wind_d_value_h11 = variablesObject.wind_d_value_h11;
   //console.log(`Value of celsius_value_h11: ${wind_d_value_h11}`);
   let wind_b_mps_value_h11 = variablesObject.wind_b_value_h11;
   //console.log(`Value of celsius_value_h11: ${wind_b_mps_value_h11}`);
   let wind_b_k_value_h11 = variablesObject.wind_b_k_value_h11;
   //console.log(`Value of celsius_value_h11: ${wind_b_k_value_h11}`);
   let wind_g_mps_value_h11 = variablesObject.wind_g_value_h11;
   //console.log(`Value of celsius_value_h11: ${wind_g_mps_value_h11}`);
   let wind_g_k_value_h11 = variablesObject.wind_g_k_value_h11;
   //console.log(`Value of celsius_value_h11: ${wind_g_k_value_h11}`);
   let wind_bf_value_h11 = variablesObject.wind_bf_value_h11;
   //console.log(`Value of celsius_value_h11: ${wind_bf_value_h11}`);
   
   let celsius_value_h12 = variablesObject.celsius_value_h12;
   //console.log(`Value of celsius_value_c: ${celsius_value_h12}`);
   let wind_d_value_h12 = variablesObject.wind_d_value_h12;
   //console.log(`Value of celsius_value_h12: ${wind_d_value_h12}`);
   let wind_b_mps_value_h12 = variablesObject.wind_b_value_h12;
   //console.log(`Value of celsius_value_h12: ${wind_b_mps_value_h12}`);
   let wind_b_k_value_h12 = variablesObject.wind_b_k_value_h12;
   //console.log(`Value of celsius_value_h12: ${wind_b_k_value_h12}`);
   let wind_g_mps_value_h12 = variablesObject.wind_g_value_h12;
   //console.log(`Value of celsius_value_h12: ${wind_g_mps_value_h12}`);
   let wind_g_k_value_h12 = variablesObject.wind_g_k_value_h12;
   //console.log(`Value of celsius_value_h12: ${wind_g_k_value_h12}`);
   let wind_bf_value_h12 = variablesObject.wind_bf_value_h12;
   //console.log(`Value of celsius_value_h12: ${wind_bf_value_h12}`);
    
   let celsius_value_h13 = variablesObject.celsius_value_h13;
   //console.log(`Value of celsius_value_c: ${celsius_value_h13}`);
   let wind_d_value_h13 = variablesObject.wind_d_value_h13;
   //console.log(`Value of celsius_value_h13: ${wind_d_value_h13}`);
   let wind_b_mps_value_h13 = variablesObject.wind_b_value_h13;
   //console.log(`Value of celsius_value_h13: ${wind_b_mps_value_h13}`);
   let wind_b_k_value_h13 = variablesObject.wind_b_k_value_h13;
   //console.log(`Value of celsius_value_h13: ${wind_b_k_value_h13}`);
   let wind_g_mps_value_h13 = variablesObject.wind_g_value_h13;
   //console.log(`Value of celsius_value_h13: ${wind_g_mps_value_h13}`);
   let wind_g_k_value_h13 = variablesObject.wind_g_k_value_h13;
   //console.log(`Value of celsius_value_h13: ${wind_g_k_value_h13}`);
   let wind_bf_value_h13 = variablesObject.wind_bf_value_h13;
   //console.log(`Value of celsius_value_h13: ${wind_bf_value_h13}`);
   

    // day 2 
    let celsius_value_d2_h1 = variablesObject.celsius_value_d2_h1;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h1}`);
    let wind_d_value_d2_h1 = variablesObject.wind_d_value_d2_h1;
    //console.log(`Value of celsius_value_h1: ${wind_d_value_d2_h1}`);
    let wind_b_mps_value_d2_h1 = variablesObject.wind_b_value_d2_h1;
    //console.log(`Value of celsius_value_h1: ${wind_b_mps_value_d2_h1}`);
    let wind_b_k_value_d2_h1 = variablesObject.wind_b_k_value_d2_h1;
    //console.log(`Value of celsius_value_h1: ${wind_b_k_value_d2_h1}`);
    let wind_g_mps_value_d2_h1 = variablesObject.wind_g_value_d2_h1;
    //console.log(`Value of celsius_value_h1: ${wind_g_mps_value_d2_h1}`);
    let wind_g_k_value_d2_h1 = variablesObject.wind_g_k_value_d2_h1;
    //console.log(`Value of celsius_value_h1: ${wind_g_k_value_d2_h1}`);
    let wind_bf_value_d2_h1 = variablesObject.wind_bf_value_d2_h1;
    //console.log(`Value of celsius_value_h1: ${wind_bf_value_d2_h1}`);
    
    let celsius_value_d2_h2 = variablesObject.celsius_value_d2_h2;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h2}`);
    let wind_d_value_d2_h2 = variablesObject.wind_d_value_d2_h2;
    //console.log(`Value of celsius_value_h2: ${wind_d_value_d2_h2}`);
    let wind_b_mps_value_d2_h2 = variablesObject.wind_b_value_d2_h2;
    //console.log(`Value of celsius_value_h2: ${wind_b_mps_value_d2_h2}`);
    let wind_b_k_value_d2_h2 = variablesObject.wind_b_k_value_d2_h2;
    //console.log(`Value of celsius_value_h2: ${wind_b_k_value_d2_h2}`);
    let wind_g_mps_value_d2_h2 = variablesObject.wind_g_value_d2_h2;
    //console.log(`Value of celsius_value_h2: ${wind_g_mps_value_d2_h2}`);
    let wind_g_k_value_d2_h2 = variablesObject.wind_g_k_value_d2_h2;
    //console.log(`Value of celsius_value_h2: ${wind_g_k_value_d2_h2}`);
    let wind_bf_value_d2_h2 = variablesObject.wind_bf_value_d2_h2;
    //console.log(`Value of celsius_value_h2: ${wind_bf_value_d2_h2}`);
    
    let celsius_value_d2_h3 = variablesObject.celsius_value_d2_h3;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h3}`);
    let wind_d_value_d2_h3 = variablesObject.wind_d_value_d2_h3;
    //console.log(`Value of celsius_value_h3: ${wind_d_value_d2_h3}`);
    let wind_b_mps_value_d2_h3 = variablesObject.wind_b_value_d2_h3;
    //console.log(`Value of celsius_value_h3: ${wind_b_mps_value_d2_h3}`);
    let wind_b_k_value_d2_h3 = variablesObject.wind_b_k_value_d2_h3;
    //console.log(`Value of celsius_value_h3: ${wind_b_k_value_d2_h3}`);
    let wind_g_mps_value_d2_h3 = variablesObject.wind_g_value_d2_h3;
    //console.log(`Value of celsius_value_h3: ${wind_g_mps_value_d2_h3}`);
    let wind_g_k_value_d2_h3 = variablesObject.wind_g_k_value_d2_h3;
    //console.log(`Value of celsius_value_h3: ${wind_g_k_value_d2_h3}`);
    let wind_bf_value_d2_h3 = variablesObject.wind_bf_value_d2_h3;
    //console.log(`Value of celsius_value_h3: ${wind_bf_value_d2_h3}`);
    
    let celsius_value_d2_h4 = variablesObject.celsius_value_d2_h4;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h4}`);
    let wind_d_value_d2_h4 = variablesObject.wind_d_value_d2_h4;
    //console.log(`Value of celsius_value_h4: ${wind_d_value_d2_h4}`);
    let wind_b_mps_value_d2_h4 = variablesObject.wind_b_value_d2_h4;
    //console.log(`Value of celsius_value_h4: ${wind_b_mps_value_d2_h4}`);
    let wind_b_k_value_d2_h4 = variablesObject.wind_b_k_value_d2_h4;
    //console.log(`Value of celsius_value_h4: ${wind_b_k_value_d2_h4}`);
    let wind_g_mps_value_d2_h4 = variablesObject.wind_g_value_d2_h4;
    //console.log(`Value of celsius_value_h4: ${wind_g_mps_value_d2_h4}`);
    let wind_g_k_value_d2_h4 = variablesObject.wind_g_k_value_d2_h4;
    //console.log(`Value of celsius_value_h4: ${wind_g_k_value_d2_h4}`);
    let wind_bf_value_d2_h4 = variablesObject.wind_bf_value_d2_h4;
    //console.log(`Value of celsius_value_h4: ${wind_bf_value_d2_h4}`);
    
    let celsius_value_d2_h5 = variablesObject.celsius_value_d2_h5;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h5}`);
    let wind_d_value_d2_h5 = variablesObject.wind_d_value_d2_h5;
    //console.log(`Value of celsius_value_h5: ${wind_d_value_d2_h5}`);
    let wind_b_mps_value_d2_h5 = variablesObject.wind_b_value_d2_h5;
    //console.log(`Value of celsius_value_h5: ${wind_b_mps_value_d2_h5}`);
    let wind_b_k_value_d2_h5 = variablesObject.wind_b_k_value_d2_h5;
    //console.log(`Value of celsius_value_h5: ${wind_b_k_value_d2_h5}`);
    let wind_g_mps_value_d2_h5 = variablesObject.wind_g_value_d2_h5;
    //console.log(`Value of celsius_value_h5: ${wind_g_mps_value_d2_h5}`);
    let wind_g_k_value_d2_h5 = variablesObject.wind_g_k_value_d2_h5;
    //console.log(`Value of celsius_value_h5: ${wind_g_k_value_d2_h5}`);
    let wind_bf_value_d2_h5 = variablesObject.wind_bf_value_d2_h5;
    //console.log(`Value of celsius_value_h5: ${wind_bf_value_d2_h5}`);
    
    let celsius_value_d2_h6 = variablesObject.celsius_value_d2_h6;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h6}`);
    let wind_d_value_d2_h6 = variablesObject.wind_d_value_d2_h6;
    //console.log(`Value of celsius_value_h6: ${wind_d_value_d2_h6}`);
    let wind_b_mps_value_d2_h6 = variablesObject.wind_b_value_d2_h6;
    //console.log(`Value of celsius_value_h6: ${wind_b_mps_value_d2_h6}`);
    let wind_b_k_value_d2_h6 = variablesObject.wind_b_k_value_d2_h6;
    //console.log(`Value of celsius_value_h6: ${wind_b_k_value_d2_h6}`);
    let wind_g_mps_value_d2_h6 = variablesObject.wind_g_value_d2_h6;
    //console.log(`Value of celsius_value_h6: ${wind_g_mps_value_d2_h6}`);
    let wind_g_k_value_d2_h6 = variablesObject.wind_g_k_value_d2_h6;
    //console.log(`Value of celsius_value_h6: ${wind_g_k_value_d2_h6}`);
    let wind_bf_value_d2_h6 = variablesObject.wind_bf_value_d2_h6;
    //console.log(`Value of celsius_value_h6: ${wind_bf_value_d2_h6}`);
     

    let celsius_value_d2_h7 = variablesObject.celsius_value_d2_h7;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h7}`);
    let wind_d_value_d2_h7 = variablesObject.wind_d_value_d2_h7;
    //console.log(`Value of celsius_value_h7: ${wind_d_value_d2_h7}`);
    let wind_b_mps_value_d2_h7 = variablesObject.wind_b_value_d2_h7;
    //console.log(`Value of celsius_value_h7: ${wind_b_mps_value_d2_h7}`);
    let wind_b_k_value_d2_h7 = variablesObject.wind_b_k_value_d2_h7;
    //console.log(`Value of celsius_value_h7: ${wind_b_k_value_d2_h7}`);
    let wind_g_mps_value_d2_h7 = variablesObject.wind_g_value_d2_h7;
    //console.log(`Value of celsius_value_h7: ${wind_g_mps_value_d2_h7}`);
    let wind_g_k_value_d2_h7 = variablesObject.wind_g_k_value_d2_h7;
    //console.log(`Value of celsius_value_h7: ${wind_g_k_value_d2_h7}`);
    let wind_bf_value_d2_h7 = variablesObject.wind_bf_value_d2_h7;
    //console.log(`Value of celsius_value_h7: ${wind_bf_value_d2_h7}`);
    
    let celsius_value_d2_h8 = variablesObject.celsius_value_d2_h8;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h8}`);
    let wind_d_value_d2_h8 = variablesObject.wind_d_value_d2_h8;
    //console.log(`Value of celsius_value_h8: ${wind_d_value_d2_h8}`);
    let wind_b_mps_value_d2_h8 = variablesObject.wind_b_value_d2_h8;
    //console.log(`Value of celsius_value_h8: ${wind_b_mps_value_d2_h8}`);
    let wind_b_k_value_d2_h8 = variablesObject.wind_b_k_value_d2_h8;
    //console.log(`Value of celsius_value_h8: ${wind_b_k_value_d2_h8}`);
    let wind_g_mps_value_d2_h8 = variablesObject.wind_g_value_d2_h8;
    //console.log(`Value of celsius_value_h8: ${wind_g_mps_value_d2_h8}`);
    let wind_g_k_value_d2_h8 = variablesObject.wind_g_k_value_d2_h8;
    //console.log(`Value of celsius_value_h8: ${wind_g_k_value_d2_h8}`);
    let wind_bf_value_d2_h8 = variablesObject.wind_bf_value_d2_h8;
    //console.log(`Value of celsius_value_h8: ${wind_bf_value_d2_h8}`);
    
    let celsius_value_d2_h9 = variablesObject.celsius_value_d2_h9;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h9}`);
    let wind_d_value_d2_h9 = variablesObject.wind_d_value_d2_h9;
    //console.log(`Value of celsius_value_h9: ${wind_d_value_d2_h9}`);
    let wind_b_mps_value_d2_h9 = variablesObject.wind_b_value_d2_h9;
    //console.log(`Value of celsius_value_h9: ${wind_b_mps_value_d2_h9}`);
    let wind_b_k_value_d2_h9 = variablesObject.wind_b_k_value_d2_h9;
    //console.log(`Value of celsius_value_h9: ${wind_b_k_value_d2_h9}`);
    let wind_g_mps_value_d2_h9 = variablesObject.wind_g_value_d2_h9;
    //console.log(`Value of celsius_value_h9: ${wind_g_mps_value_d2_h9}`);
    let wind_g_k_value_d2_h9 = variablesObject.wind_g_k_value_d2_h9;
    //console.log(`Value of celsius_value_h9: ${wind_g_k_value_d2_h9}`);
    let wind_bf_value_d2_h9 = variablesObject.wind_bf_value_d2_h9;
    //console.log(`Value of celsius_value_h9: ${wind_bf_value_d2_h9}`);
    
    let celsius_value_d2_h10 = variablesObject.celsius_value_d2_h10;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h10}`);
    let wind_d_value_d2_h10 = variablesObject.wind_d_value_d2_h10;
    //console.log(`Value of celsius_value_h10: ${wind_d_value_d2_h10}`);
    let wind_b_mps_value_d2_h10 = variablesObject.wind_b_value_d2_h10;
    //console.log(`Value of celsius_value_h10: ${wind_b_mps_value_d2_h10}`);
    let wind_b_k_value_d2_h10 = variablesObject.wind_b_k_value_d2_h10;
    //console.log(`Value of celsius_value_h10: ${wind_b_k_value_d2_h10}`);
    let wind_g_mps_value_d2_h10 = variablesObject.wind_g_value_d2_h10;
    //console.log(`Value of celsius_value_h10: ${wind_g_mps_value_d2_h10}`);
    let wind_g_k_value_d2_h10 = variablesObject.wind_g_k_value_d2_h10;
    //console.log(`Value of celsius_value_h10: ${wind_g_k_value_d2_h10}`);
    let wind_bf_value_d2_h10 = variablesObject.wind_bf_value_d2_h10;
    //console.log(`Value of celsius_value_h10: ${wind_bf_value_d2_h10}`);
    
    let celsius_value_d2_h11 = variablesObject.celsius_value_d2_h11;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h11}`);
    let wind_d_value_d2_h11 = variablesObject.wind_d_value_d2_h11;
    //console.log(`Value of celsius_value_h11: ${wind_d_value_d2_h11}`);
    let wind_b_mps_value_d2_h11 = variablesObject.wind_b_value_d2_h11;
    //console.log(`Value of celsius_value_h11: ${wind_b_mps_value_d2_h11}`);
    let wind_b_k_value_d2_h11 = variablesObject.wind_b_k_value_d2_h11;
    //console.log(`Value of celsius_value_h11: ${wind_b_k_value_d2_h11}`);
    let wind_g_mps_value_d2_h11 = variablesObject.wind_g_value_d2_h11;
    //console.log(`Value of celsius_value_h11: ${wind_g_mps_value_d2_h11}`);
    let wind_g_k_value_d2_h11 = variablesObject.wind_g_k_value_d2_h11;
    //console.log(`Value of celsius_value_h11: ${wind_g_k_value_d2_h11}`);
    let wind_bf_value_d2_h11 = variablesObject.wind_bf_value_d2_h11;
    //console.log(`Value of celsius_value_h11: ${wind_bf_value_d2_h11}`);
    
    let celsius_value_d2_h12 = variablesObject.celsius_value_d2_h12;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h12}`);
    let wind_d_value_d2_h12 = variablesObject.wind_d_value_d2_h12;
    //console.log(`Value of celsius_value_h12: ${wind_d_value_d2_h12}`);
    let wind_b_mps_value_d2_h12 = variablesObject.wind_b_value_d2_h12;
    //console.log(`Value of celsius_value_h12: ${wind_b_mps_value_d2_h12}`);
    let wind_b_k_value_d2_h12 = variablesObject.wind_b_k_value_d2_h12;
    //console.log(`Value of celsius_value_h12: ${wind_b_k_value_d2_h12}`);
    let wind_g_mps_value_d2_h12 = variablesObject.wind_g_value_d2_h12;
    //console.log(`Value of celsius_value_h12: ${wind_g_mps_value_d2_h12}`);
    let wind_g_k_value_d2_h12 = variablesObject.wind_g_k_value_d2_h12;
    //console.log(`Value of celsius_value_h12: ${wind_g_k_value_d2_h12}`);
    let wind_bf_value_d2_h12 = variablesObject.wind_bf_value_d2_h12;
    //console.log(`Value of celsius_value_h12: ${wind_bf_value_d2_h12}`);
    
    let celsius_value_d2_h13 = variablesObject.celsius_value_d2_h13;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h13}`);
    let wind_d_value_d2_h13 = variablesObject.wind_d_value_d2_h13;
    //console.log(`Value of celsius_value_h13: ${wind_d_value_d2_h13}`);
    let wind_b_mps_value_d2_h13 = variablesObject.wind_b_value_d2_h13;
    //console.log(`Value of celsius_value_h13: ${wind_b_mps_value_d2_h13}`);
    let wind_b_k_value_d2_h13 = variablesObject.wind_b_k_value_d2_h13;
    //console.log(`Value of celsius_value_h13: ${wind_b_k_value_d2_h13}`);
    let wind_g_mps_value_d2_h13 = variablesObject.wind_g_value_d2_h13;
    //console.log(`Value of celsius_value_h13: ${wind_g_mps_value_d2_h13}`);
    let wind_g_k_value_d2_h13 = variablesObject.wind_g_k_value_d2_h13;
    //console.log(`Value of celsius_value_h13: ${wind_g_k_value_d2_h13}`);
    let wind_bf_value_d2_h13 = variablesObject.wind_bf_value_d2_h13;
    //console.log(`Value of celsius_value_h13: ${wind_bf_value_d2_h13}`);
    
    let celsius_value_d2_h14 = variablesObject.celsius_value_d2_h14;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h14}`);
    let wind_d_value_d2_h14 = variablesObject.wind_d_value_d2_h14;
    //console.log(`Value of celsius_value_h14: ${wind_d_value_d2_h14}`);
    let wind_b_mps_value_d2_h14 = variablesObject.wind_b_value_d2_h14;
    //console.log(`Value of celsius_value_h14: ${wind_b_mps_value_d2_h14}`);
    let wind_b_k_value_d2_h14 = variablesObject.wind_b_k_value_d2_h14;
    //console.log(`Value of celsius_value_h14: ${wind_b_k_value_d2_h14}`);
    let wind_g_mps_value_d2_h14 = variablesObject.wind_g_value_d2_h14;
    //console.log(`Value of celsius_value_h14: ${wind_g_mps_value_d2_h14}`);
    let wind_g_k_value_d2_h14 = variablesObject.wind_g_k_value_d2_h14;
    //console.log(`Value of celsius_value_h14: ${wind_g_k_value_d2_h14}`);
    let wind_bf_value_d2_h14 = variablesObject.wind_bf_value_d2_h14;
    //console.log(`Value of celsius_value_h14: ${wind_bf_value_d2_h14}`);
    
    let celsius_value_d2_h15 = variablesObject.celsius_value_d2_h15;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h15}`);
    let wind_d_value_d2_h15 = variablesObject.wind_d_value_d2_h15;
    //console.log(`Value of celsius_value_h15: ${wind_d_value_d2_h15}`);
    let wind_b_mps_value_d2_h15 = variablesObject.wind_b_value_d2_h15;
    //console.log(`Value of celsius_value_h15: ${wind_b_mps_value_d2_h15}`);
    let wind_b_k_value_d2_h15 = variablesObject.wind_b_k_value_d2_h15;
    //console.log(`Value of celsius_value_h15: ${wind_b_k_value_d2_h15}`);
    let wind_g_mps_value_d2_h15 = variablesObject.wind_g_value_d2_h15;
    //console.log(`Value of celsius_value_h15: ${wind_g_mps_value_d2_h15}`);
    let wind_g_k_value_d2_h15 = variablesObject.wind_g_k_value_d2_h15;
    //console.log(`Value of celsius_value_h15: ${wind_g_k_value_d2_h15}`);
    let wind_bf_value_d2_h15 = variablesObject.wind_bf_value_d2_h15;
    //console.log(`Value of celsius_value_h15: ${wind_bf_value_d2_h15}`);
    
    let celsius_value_d2_h16 = variablesObject.celsius_value_d2_h16;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h16}`);
    let wind_d_value_d2_h16 = variablesObject.wind_d_value_d2_h16;
    //console.log(`Value of celsius_value_h16: ${wind_d_value_d2_h16}`);
    let wind_b_mps_value_d2_h16 = variablesObject.wind_b_value_d2_h16;
    //console.log(`Value of celsius_value_h16: ${wind_b_mps_value_d2_h16}`);
    let wind_b_k_value_d2_h16 = variablesObject.wind_b_k_value_d2_h16;
    //console.log(`Value of celsius_value_h16: ${wind_b_k_value_d2_h16}`);
    let wind_g_mps_value_d2_h16 = variablesObject.wind_g_value_d2_h16;
    //console.log(`Value of celsius_value_h16: ${wind_g_mps_value_d2_h16}`);
    let wind_g_k_value_d2_h16 = variablesObject.wind_g_k_value_d2_h16;
    //console.log(`Value of celsius_value_h16: ${wind_g_k_value_d2_h16}`);
    let wind_bf_value_d2_h16 = variablesObject.wind_bf_value_d2_h16;
    //console.log(`Value of celsius_value_h16: ${wind_bf_value_d2_h16}`);
    
    let celsius_value_d2_h17 = variablesObject.celsius_value_d2_h17;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h17}`);
    let wind_d_value_d2_h17 = variablesObject.wind_d_value_d2_h17;
    //console.log(`Value of celsius_value_h17: ${wind_d_value_d2_h17}`);
    let wind_b_mps_value_d2_h17 = variablesObject.wind_b_value_d2_h17;
    //console.log(`Value of celsius_value_h17: ${wind_b_mps_value_d2_h17}`);
    let wind_b_k_value_d2_h17 = variablesObject.wind_b_k_value_d2_h17;
    //console.log(`Value of celsius_value_h17: ${wind_b_k_value_d2_h17}`);
    let wind_g_mps_value_d2_h17 = variablesObject.wind_g_value_d2_h17;
    //console.log(`Value of celsius_value_h17: ${wind_g_mps_value_d2_h17}`);
    let wind_g_k_value_d2_h17 = variablesObject.wind_g_k_value_d2_h17;
    //console.log(`Value of celsius_value_h17: ${wind_g_k_value_d2_h17}`);
    let wind_bf_value_d2_h17 = variablesObject.wind_bf_value_d2_h17;
    //console.log(`Value of celsius_value_h17: ${wind_bf_value_d2_h17}`);
    
    let celsius_value_d2_h18 = variablesObject.celsius_value_d2_h18;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h18}`);
    let wind_d_value_d2_h18 = variablesObject.wind_d_value_d2_h18;
    //console.log(`Value of celsius_value_h18: ${wind_d_value_d2_h18}`);
    let wind_b_mps_value_d2_h18 = variablesObject.wind_b_value_d2_h18;
    //console.log(`Value of celsius_value_h18: ${wind_b_mps_value_d2_h18}`);
    let wind_b_k_value_d2_h18 = variablesObject.wind_b_k_value_d2_h18;
    //console.log(`Value of celsius_value_h18: ${wind_b_k_value_d2_h18}`);
    let wind_g_mps_value_d2_h18 = variablesObject.wind_g_value_d2_h18;
    //console.log(`Value of celsius_value_h18: ${wind_g_mps_value_d2_h18}`);
    let wind_g_k_value_d2_h18 = variablesObject.wind_g_k_value_d2_h18;
    //console.log(`Value of celsius_value_h18: ${wind_g_k_value_d2_h18}`);
    let wind_bf_value_d2_h18 = variablesObject.wind_bf_value_d2_h18;
    //console.log(`Value of celsius_value_h18: ${wind_bf_value_d2_h18}`);
    
    let celsius_value_d2_h19 = variablesObject.celsius_value_d2_h19;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h19}`);
    let wind_d_value_d2_h19 = variablesObject.wind_d_value_d2_h19;
    //console.log(`Value of celsius_value_h19: ${wind_d_value_d2_h19}`);
    let wind_b_mps_value_d2_h19 = variablesObject.wind_b_value_d2_h19;
    //console.log(`Value of celsius_value_h19: ${wind_b_mps_value_d2_h19}`);
    let wind_b_k_value_d2_h19 = variablesObject.wind_b_k_value_d2_h19;
    //console.log(`Value of celsius_value_h19: ${wind_b_k_value_d2_h19}`);
    let wind_g_mps_value_d2_h19 = variablesObject.wind_g_value_d2_h19;
    //console.log(`Value of celsius_value_h19: ${wind_g_mps_value_d2_h19}`);
    let wind_g_k_value_d2_h19 = variablesObject.wind_g_k_value_d2_h19;
    //console.log(`Value of celsius_value_h19: ${wind_g_k_value_d2_h19}`);
    let wind_bf_value_d2_h19 = variablesObject.wind_bf_value_d2_h19;
    //console.log(`Value of celsius_value_h19: ${wind_bf_value_d2_h19}`);
    
    let celsius_value_d2_h20 = variablesObject.celsius_value_d2_h20;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h20}`);
    let wind_d_value_d2_h20 = variablesObject.wind_d_value_d2_h20;
    //console.log(`Value of celsius_value_h20: ${wind_d_value_d2_h20}`);
    let wind_b_mps_value_d2_h20 = variablesObject.wind_b_value_d2_h20;
    //console.log(`Value of celsius_value_h20: ${wind_b_mps_value_d2_h20}`);
    let wind_b_k_value_d2_h20 = variablesObject.wind_b_k_value_d2_h20;
    //console.log(`Value of celsius_value_h20: ${wind_b_k_value_d2_h20}`);
    let wind_g_mps_value_d2_h20 = variablesObject.wind_g_value_d2_h20;
    //console.log(`Value of celsius_value_h20: ${wind_g_mps_value_d2_h20}`);
    let wind_g_k_value_d2_h20 = variablesObject.wind_g_k_value_d2_h20;
    //console.log(`Value of celsius_value_h20: ${wind_g_k_value_d2_h20}`);
    let wind_bf_value_d2_h20 = variablesObject.wind_bf_value_d2_h20;
    //console.log(`Value of celsius_value_h20: ${wind_bf_value_d2_h20}`);
    
    let celsius_value_d2_h21 = variablesObject.celsius_value_d2_h21;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h21}`);
    let wind_d_value_d2_h21 = variablesObject.wind_d_value_d2_h21;
    //console.log(`Value of celsius_value_h21: ${wind_d_value_d2_h21}`);
    let wind_b_mps_value_d2_h21 = variablesObject.wind_b_value_d2_h21;
    //console.log(`Value of celsius_value_h21: ${wind_b_mps_value_d2_h21}`);
    let wind_b_k_value_d2_h21 = variablesObject.wind_b_k_value_d2_h21;
    //console.log(`Value of celsius_value_h21: ${wind_b_k_value_d2_h21}`);
    let wind_g_mps_value_d2_h21 = variablesObject.wind_g_value_d2_h21;
    //console.log(`Value of celsius_value_h21: ${wind_g_mps_value_d2_h21}`);
    let wind_g_k_value_d2_h21 = variablesObject.wind_g_k_value_d2_h21;
    //console.log(`Value of celsius_value_h21: ${wind_g_k_value_d2_h21}`);
    let wind_bf_value_d2_h21 = variablesObject.wind_bf_value_d2_h21;
    //console.log(`Value of celsius_value_h21: ${wind_bf_value_d2_h21}`);
    
    let celsius_value_d2_h22 = variablesObject.celsius_value_d2_h22;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h22}`);
    let wind_d_value_d2_h22 = variablesObject.wind_d_value_d2_h22;
    //console.log(`Value of celsius_value_h22: ${wind_d_value_d2_h22}`);
    let wind_b_mps_value_d2_h22 = variablesObject.wind_b_value_d2_h22;
    //console.log(`Value of celsius_value_h22: ${wind_b_mps_value_d2_h22}`);
    let wind_b_k_value_d2_h22 = variablesObject.wind_b_k_value_d2_h22;
    //console.log(`Value of celsius_value_h22: ${wind_b_k_value_d2_h22}`);
    let wind_g_mps_value_d2_h22 = variablesObject.wind_g_value_d2_h22;
    //console.log(`Value of celsius_value_h22: ${wind_g_mps_value_d2_h22}`);
    let wind_g_k_value_d2_h22 = variablesObject.wind_g_k_value_d2_h22;
    //console.log(`Value of celsius_value_h22: ${wind_g_k_value_d2_h22}`);
    let wind_bf_value_d2_h22 = variablesObject.wind_bf_value_d2_h22;
    //console.log(`Value of celsius_value_h22: ${wind_bf_value_d2_h22}`);
    
    let celsius_value_d2_h23 = variablesObject.celsius_value_d2_h23;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h23}`);
    let wind_d_value_d2_h23 = variablesObject.wind_d_value_d2_h23;
    //console.log(`Value of celsius_value_h23: ${wind_d_value_d2_h23}`);
    let wind_b_mps_value_d2_h23 = variablesObject.wind_b_value_d2_h23;
    //console.log(`Value of celsius_value_h23: ${wind_b_mps_value_d2_h23}`);
    let wind_b_k_value_d2_h23 = variablesObject.wind_b_k_value_d2_h23;
    //console.log(`Value of celsius_value_h23: ${wind_b_k_value_d2_h23}`);
    let wind_g_mps_value_d2_h23 = variablesObject.wind_g_value_d2_h23;
    //console.log(`Value of celsius_value_h23: ${wind_g_mps_value_d2_h23}`);
    let wind_g_k_value_d2_h23 = variablesObject.wind_g_k_value_d2_h23;
    //console.log(`Value of celsius_value_h23: ${wind_g_k_value_d2_h23}`);
    let wind_bf_value_d2_h23 = variablesObject.wind_bf_value_d2_h23;
    //console.log(`Value of celsius_value_h23: ${wind_bf_value_d2_h23}`);
    
    let celsius_value_d2_h24 = variablesObject.celsius_value_d2_h24;
    //console.log(`Value of celsius_value_c: ${celsius_value_d2_h24}`);
    let wind_d_value_d2_h24 = variablesObject.wind_d_value_d2_h24;
    //console.log(`Value of celsius_value_h24: ${wind_d_value_d2_h24}`);
    let wind_b_mps_value_d2_h24 = variablesObject.wind_b_value_d2_h24;
    //console.log(`Value of celsius_value_h24: ${wind_b_mps_value_d2_h24}`);
    let wind_b_k_value_d2_h24 = variablesObject.wind_b_k_value_d2_h24;
    //console.log(`Value of celsius_value_h24: ${wind_b_k_value_d2_h24}`);
    let wind_g_mps_value_d2_h24 = variablesObject.wind_g_value_d2_h24;
    //console.log(`Value of celsius_value_h24: ${wind_g_mps_value_d2_h24}`);
    let wind_g_k_value_d2_h24 = variablesObject.wind_g_k_value_d2_h24;
    //console.log(`Value of celsius_value_h24: ${wind_g_k_value_d2_h24}`);
    let wind_bf_value_d2_h24 = variablesObject.wind_bf_value_d2_h24;
    //console.log(`Value of celsius_value_h24: ${wind_bf_value_d2_h24}`);
    // day 3 
     let celsius_value_d3_h1 = variablesObject.celsius_value_d3_h1;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h1}`);
let wind_d_value_d3_h1 = variablesObject.wind_d_value_d3_h1;
//console.log(`Value of celsius_value_h1: ${wind_d_value_d3_h1}`);
let wind_b_mps_value_d3_h1 = variablesObject.wind_b_value_d3_h1;
//console.log(`Value of celsius_value_h1: ${wind_b_mps_value_d3_h1}`);
let wind_b_k_value_d3_h1 = variablesObject.wind_b_k_value_d3_h1;
//console.log(`Value of celsius_value_h1: ${wind_b_k_value_d3_h1}`);
let wind_g_mps_value_d3_h1 = variablesObject.wind_g_value_d3_h1;
//console.log(`Value of celsius_value_h1: ${wind_g_mps_value_d3_h1}`);
let wind_g_k_value_d3_h1 = variablesObject.wind_g_k_value_d3_h1;
//console.log(`Value of celsius_value_h1: ${wind_g_k_value_d3_h1}`);
let wind_bf_value_d3_h1 = variablesObject.wind_bf_value_d3_h1;
//console.log(`Value of celsius_value_h1: ${wind_bf_value_d3_h1}`);

let celsius_value_d3_h2 = variablesObject.celsius_value_d3_h2;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h2}`);
let wind_d_value_d3_h2 = variablesObject.wind_d_value_d3_h2;
//console.log(`Value of celsius_value_h2: ${wind_d_value_d3_h2}`);
let wind_b_mps_value_d3_h2 = variablesObject.wind_b_value_d3_h2;
//console.log(`Value of celsius_value_h2: ${wind_b_mps_value_d3_h2}`);
let wind_b_k_value_d3_h2 = variablesObject.wind_b_k_value_d3_h2;
//console.log(`Value of celsius_value_h2: ${wind_b_k_value_d3_h2}`);
let wind_g_mps_value_d3_h2 = variablesObject.wind_g_value_d3_h2;
//console.log(`Value of celsius_value_h2: ${wind_g_mps_value_d3_h2}`);
let wind_g_k_value_d3_h2 = variablesObject.wind_g_k_value_d3_h2;
//console.log(`Value of celsius_value_h2: ${wind_g_k_value_d3_h2}`);
let wind_bf_value_d3_h2 = variablesObject.wind_bf_value_d3_h2;
//console.log(`Value of celsius_value_h2: ${wind_bf_value_d3_h2}`);

let celsius_value_d3_h3 = variablesObject.celsius_value_d3_h3;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h3}`);
let wind_d_value_d3_h3 = variablesObject.wind_d_value_d3_h3;
//console.log(`Value of celsius_value_h3: ${wind_d_value_d3_h3}`);
let wind_b_mps_value_d3_h3 = variablesObject.wind_b_value_d3_h3;
//console.log(`Value of celsius_value_h3: ${wind_b_mps_value_d3_h3}`);
let wind_b_k_value_d3_h3 = variablesObject.wind_b_k_value_d3_h3;
//console.log(`Value of celsius_value_h3: ${wind_b_k_value_d3_h3}`);
let wind_g_mps_value_d3_h3 = variablesObject.wind_g_value_d3_h3;
//console.log(`Value of celsius_value_h3: ${wind_g_mps_value_d3_h3}`);
let wind_g_k_value_d3_h3 = variablesObject.wind_g_k_value_d3_h3;
//console.log(`Value of celsius_value_h3: ${wind_g_k_value_d3_h3}`);
let wind_bf_value_d3_h3 = variablesObject.wind_bf_value_d3_h3;
//console.log(`Value of celsius_value_h3: ${wind_bf_value_d3_h3}`);

let celsius_value_d3_h4 = variablesObject.celsius_value_d3_h4;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h4}`);
let wind_d_value_d3_h4 = variablesObject.wind_d_value_d3_h4;
//console.log(`Value of celsius_value_h4: ${wind_d_value_d3_h4}`);
let wind_b_mps_value_d3_h4 = variablesObject.wind_b_value_d3_h4;
//console.log(`Value of celsius_value_h4: ${wind_b_mps_value_d3_h4}`);
let wind_b_k_value_d3_h4 = variablesObject.wind_b_k_value_d3_h4;
//console.log(`Value of celsius_value_h4: ${wind_b_k_value_d3_h4}`);
let wind_g_mps_value_d3_h4 = variablesObject.wind_g_value_d3_h4;
//console.log(`Value of celsius_value_h4: ${wind_g_mps_value_d3_h4}`);
let wind_g_k_value_d3_h4 = variablesObject.wind_g_k_value_d3_h4;
//console.log(`Value of celsius_value_h4: ${wind_g_k_value_d3_h4}`);
let wind_bf_value_d3_h4 = variablesObject.wind_bf_value_d3_h4;
//console.log(`Value of celsius_value_h4: ${wind_bf_value_d3_h4}`);

let celsius_value_d3_h5 = variablesObject.celsius_value_d3_h5;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h5}`);
let wind_d_value_d3_h5 = variablesObject.wind_d_value_d3_h5;
//console.log(`Value of celsius_value_h5: ${wind_d_value_d3_h5}`);
let wind_b_mps_value_d3_h5 = variablesObject.wind_b_value_d3_h5;
//console.log(`Value of celsius_value_h5: ${wind_b_mps_value_d3_h5}`);
let wind_b_k_value_d3_h5 = variablesObject.wind_b_k_value_d3_h5;
//console.log(`Value of celsius_value_h5: ${wind_b_k_value_d3_h5}`);
let wind_g_mps_value_d3_h5 = variablesObject.wind_g_value_d3_h5;
//console.log(`Value of celsius_value_h5: ${wind_g_mps_value_d3_h5}`);
let wind_g_k_value_d3_h5 = variablesObject.wind_g_k_value_d3_h5;
//console.log(`Value of celsius_value_h5: ${wind_g_k_value_d3_h5}`);
let wind_bf_value_d3_h5 = variablesObject.wind_bf_value_d3_h5;
//console.log(`Value of celsius_value_h5: ${wind_bf_value_d3_h5}`);

let celsius_value_d3_h6 = variablesObject.celsius_value_d3_h6;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h6}`);
let wind_d_value_d3_h6 = variablesObject.wind_d_value_d3_h6;
//console.log(`Value of celsius_value_h6: ${wind_d_value_d3_h6}`);
let wind_b_mps_value_d3_h6 = variablesObject.wind_b_value_d3_h6;
//console.log(`Value of celsius_value_h6: ${wind_b_mps_value_d3_h6}`);
let wind_b_k_value_d3_h6 = variablesObject.wind_b_k_value_d3_h6;
//console.log(`Value of celsius_value_h6: ${wind_b_k_value_d3_h6}`);
let wind_g_mps_value_d3_h6 = variablesObject.wind_g_value_d3_h6;
//console.log(`Value of celsius_value_h6: ${wind_g_mps_value_d3_h6}`);
let wind_g_k_value_d3_h6 = variablesObject.wind_g_k_value_d3_h6;
//console.log(`Value of celsius_value_h6: ${wind_g_k_value_d3_h6}`);
let wind_bf_value_d3_h6 = variablesObject.wind_bf_value_d3_h6;
//console.log(`Value of celsius_value_h6: ${wind_bf_value_d3_h6}`);

let celsius_value_d3_h7 = variablesObject.celsius_value_d3_h7;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h7}`);
let wind_d_value_d3_h7 = variablesObject.wind_d_value_d3_h7;
//console.log(`Value of celsius_value_h7: ${wind_d_value_d3_h7}`);
let wind_b_mps_value_d3_h7 = variablesObject.wind_b_value_d3_h7;
//console.log(`Value of celsius_value_h7: ${wind_b_mps_value_d3_h7}`);
let wind_b_k_value_d3_h7 = variablesObject.wind_b_k_value_d3_h7;
//console.log(`Value of celsius_value_h7: ${wind_b_k_value_d3_h7}`);
let wind_g_mps_value_d3_h7 = variablesObject.wind_g_value_d3_h7;
//console.log(`Value of celsius_value_h7: ${wind_g_mps_value_d3_h7}`);
let wind_g_k_value_d3_h7 = variablesObject.wind_g_k_value_d3_h7;
//console.log(`Value of celsius_value_h7: ${wind_g_k_value_d3_h7}`);
let wind_bf_value_d3_h7 = variablesObject.wind_bf_value_d3_h7;
//console.log(`Value of celsius_value_h7: ${wind_bf_value_d3_h7}`);

let celsius_value_d3_h8 = variablesObject.celsius_value_d3_h8;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h8}`);
let wind_d_value_d3_h8 = variablesObject.wind_d_value_d3_h8;
//console.log(`Value of celsius_value_h8: ${wind_d_value_d3_h8}`);
let wind_b_mps_value_d3_h8 = variablesObject.wind_b_value_d3_h8;
//console.log(`Value of celsius_value_h8: ${wind_b_mps_value_d3_h8}`);
let wind_b_k_value_d3_h8 = variablesObject.wind_b_k_value_d3_h8;
//console.log(`Value of celsius_value_h8: ${wind_b_k_value_d3_h8}`);
let wind_g_mps_value_d3_h8 = variablesObject.wind_g_value_d3_h8;
//console.log(`Value of celsius_value_h8: ${wind_g_mps_value_d3_h8}`);
let wind_g_k_value_d3_h8 = variablesObject.wind_g_k_value_d3_h8;
//console.log(`Value of celsius_value_h8: ${wind_g_k_value_d3_h8}`);
let wind_bf_value_d3_h8 = variablesObject.wind_bf_value_d3_h8;
//console.log(`Value of celsius_value_h8: ${wind_bf_value_d3_h8}`);

let celsius_value_d3_h9 = variablesObject.celsius_value_d3_h9;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h9}`);
let wind_d_value_d3_h9 = variablesObject.wind_d_value_d3_h9;
//console.log(`Value of celsius_value_h9: ${wind_d_value_d3_h9}`);
let wind_b_mps_value_d3_h9 = variablesObject.wind_b_value_d3_h9;
//console.log(`Value of celsius_value_h9: ${wind_b_mps_value_d3_h9}`);
let wind_b_k_value_d3_h9 = variablesObject.wind_b_k_value_d3_h9;
//console.log(`Value of celsius_value_h9: ${wind_b_k_value_d3_h9}`);
let wind_g_mps_value_d3_h9 = variablesObject.wind_g_value_d3_h9;
//console.log(`Value of celsius_value_h9: ${wind_g_mps_value_d3_h9}`);
let wind_g_k_value_d3_h9 = variablesObject.wind_g_k_value_d3_h9;
//console.log(`Value of celsius_value_h9: ${wind_g_k_value_d3_h9}`);
let wind_bf_value_d3_h9 = variablesObject.wind_bf_value_d3_h9;
//console.log(`Value of celsius_value_h9: ${wind_bf_value_d3_h9}`);

let celsius_value_d3_h10 = variablesObject.celsius_value_d3_h10;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h10}`);
let wind_d_value_d3_h10 = variablesObject.wind_d_value_d3_h10;
//console.log(`Value of celsius_value_h10: ${wind_d_value_d3_h10}`);
let wind_b_mps_value_d3_h10 = variablesObject.wind_b_value_d3_h10;
//console.log(`Value of celsius_value_h10: ${wind_b_mps_value_d3_h10}`);
let wind_b_k_value_d3_h10 = variablesObject.wind_b_k_value_d3_h10;
//console.log(`Value of celsius_value_h10: ${wind_b_k_value_d3_h10}`);
let wind_g_mps_value_d3_h10 = variablesObject.wind_g_value_d3_h10;
//console.log(`Value of celsius_value_h10: ${wind_g_mps_value_d3_h10}`);
let wind_g_k_value_d3_h10 = variablesObject.wind_g_k_value_d3_h10;
//console.log(`Value of celsius_value_h10: ${wind_g_k_value_d3_h10}`);
let wind_bf_value_d3_h10 = variablesObject.wind_bf_value_d3_h10;
//console.log(`Value of celsius_value_h10: ${wind_bf_value_d3_h10}`);

let celsius_value_d3_h11 = variablesObject.celsius_value_d3_h11;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h11}`);
let wind_d_value_d3_h11 = variablesObject.wind_d_value_d3_h11;
//console.log(`Value of celsius_value_h11: ${wind_d_value_d3_h11}`);
let wind_b_mps_value_d3_h11 = variablesObject.wind_b_value_d3_h11;
//console.log(`Value of celsius_value_h11: ${wind_b_mps_value_d3_h11}`);
let wind_b_k_value_d3_h11 = variablesObject.wind_b_k_value_d3_h11;
//console.log(`Value of celsius_value_h11: ${wind_b_k_value_d3_h11}`);
let wind_g_mps_value_d3_h11 = variablesObject.wind_g_value_d3_h11;
//console.log(`Value of celsius_value_h11: ${wind_g_mps_value_d3_h11}`);
let wind_g_k_value_d3_h11 = variablesObject.wind_g_k_value_d3_h11;
//console.log(`Value of celsius_value_h11: ${wind_g_k_value_d3_h11}`);
let wind_bf_value_d3_h11 = variablesObject.wind_bf_value_d3_h11;
//console.log(`Value of celsius_value_h11: ${wind_bf_value_d3_h11}`);

let celsius_value_d3_h12 = variablesObject.celsius_value_d3_h12;
//console.log(`Value of celsius_value_c: ${celsius_value_d3_h12}`);
let wind_d_value_d3_h12 = variablesObject.wind_d_value_d3_h12;
//console.log(`Value of celsius_value_h12: ${wind_d_value_d3_h12}`);
let wind_b_mps_value_d3_h12 = variablesObject.wind_b_value_d3_h12;
//console.log(`Value of celsius_value_h12: ${wind_b_mps_value_d3_h12}`);
let wind_b_k_value_d3_h12 = variablesObject.wind_b_k_value_d3_h12;
//console.log(`Value of celsius_value_h12: ${wind_b_k_value_d3_h12}`);
let wind_g_mps_value_d3_h12 = variablesObject.wind_g_value_d3_h12;
//console.log(`Value of celsius_value_h12: ${wind_g_mps_value_d3_h12}`);
let wind_g_k_value_d3_h12 = variablesObject.wind_g_k_value_d3_h12;
//console.log(`Value of celsius_value_h12: ${wind_g_k_value_d3_h12}`);
let wind_bf_value_d3_h12 = variablesObject.wind_bf_value_d3_h12;
//console.log(`Value of celsius_value_h12: ${wind_bf_value_d3_h12}`);

document.getElementById('temperature').textContent = celsius_value_c + '°C';
document.getElementById('wind speed in mps').textContent = wind_b_mps_value_c + "mps";
document.getElementById('wind speed in kts').textContent = wind_b_k_value_c + ' kts';
document.getElementById('wind gusting in mps').textContent =wind_g_mps_value_c + 'mps';
document.getElementById('wind gusting in kts').textContent = wind_b_k_value_c + ' kts';
document.getElementById('beaufort scale').textContent = wind_bf_value_c;
    //console.log('Variables displayed successfully!');
  })
  .catch(error => console.error(error));})


   
