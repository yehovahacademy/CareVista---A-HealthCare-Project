<script>
 let weight = $state('')
    let height = $state('')


 let bmi = $derived(() => weight / (height * height))
    let status = $state('')

    async function calculateBMI() {

        const response = await fetch(
            `carevista-a-healthcare-project-production.up.railway.app?weight=${weight}&height=${height}`
        )

        const data = await response.json()

        bmi = data.bmi
        status = data.status
    }


    //For hydration



  let water = $state('')
  let goal = $state('')
  let percentage = $state('')
  let hydrationStatus = $state('')

 async function checkHydration() {
    try {
        const res = await fetch(
            `http://127.0.0.1:8000/hydration?water=${water}&goal=${goal}`
        )

        if (!res.ok) {
            hydrationStatus = `Error: ${res.status} ${res.statusText}`
            return
        }

        const data = await res.json()

        hydrationStatus = data.status   // ✅
        percentage = data.ratio         // ✅
    } catch (error) {
        console.error('Error fetching hydration data:', error)
        hydrationStatus = 'Error fetching data'
    }
}




</script>



<section class="bmi-calculator">
<h1>BMI Calculator</h1>
<div class="intro-para">
  <h2>Introduction to BMI</h2>
  <p>The BMI Calculator helps users better understand their overall health and wellness by providing an estimate of body mass based on height and weight measurements. This feature offers a quick and simple way to monitor fitness levels, maintain healthy lifestyle awareness, and support informed healthcare decisions through an easy-to-use and interactive health tracking experience.
</p>
</div>

<div class="bmi-model">
<h2>Your Height:</h2>
  <input type = "number" placeholder="Enter your height" bind:value={height}>
<h2>Your Weight:</h2>
  <input type="number" placeholder="Enter your weight" bind:value={weight}>  
  <button onclick={calculateBMI}>Get your BMI</button>
</div>
<div class="result">
  <h1>Your BMI is: {status}</h1>
</div>
</section>

<br><br>
<section>
<div class="hydration-calculator">
  <h1>Hydration Calculator</h1>
  <div class="intro-para-2">
    <p>The Hydration Calculator is a simple yet effective health tool designed to help users track their daily water intake and maintain proper hydration levels. Staying hydrated is essential for overall health, energy, focus, and body function, but many people often fail to meet their daily water requirements.

This application allows users to input their water consumption and compare it with their recommended daily intake. Based on the data, it calculates hydration percentage and provides a clear status such as Dehydrated, Normal, or Well Hydrated.

The goal of this project is to promote healthy habits through an easy-to-use interface while demonstrating practical implementation of reactive UI design and real-time calculations in a modern web application.</p>
  </div>

  <div class="hydration-model">
    <h2>Enter your water intake of today:</h2>
    <input type="number" placeholder="enter your water intake in L"bind:value={water}>
    <h2>Enter your Goal</h2>
    <input type="number" placeholder="enter your water intake goal"bind:value={goal}>
    <button onclick={checkHydration}>Get your result</button>
  </div>
  <div class="result">
    Your hydration Level is: {hydrationStatus  || "Not calculated yet"}
  </div>
</div>



</section>













<style>
/* BMI Calculator - Corporate Style */
.bmi-calculator {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08), 0 2px 4px rgba(0, 0, 0, 0.02);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Intro Section */
.intro-para {
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid #e9ecef;
}

.intro-para h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a3a5c;
  margin-bottom: 1rem;
  letter-spacing: -0.3px;
}

.intro-para p {
  font-size: 0.95rem;
  line-height: 1.6;
  color: #4a5568;
  margin: 0;
}

/* BMI Model Section */
.bmi-model {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.bmi-model h2 {
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #2d5f8b;
  margin-bottom: 0.5rem;
  margin-top: 1rem;
}

.bmi-model h2:first-of-type {
  margin-top: 0;
}

/* Input Fields */
.bmi-model input {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  font-family: inherit;
  color: #1a202c;
  background: #ffffff;
  border: 1.5px solid #e2e8f0;
  border-radius: 6px;
  transition: all 0.2s ease;
  box-sizing: border-box;
}

.bmi-model input:focus {
  outline: none;
  border-color: #2d5f8b;
  box-shadow: 0 0 0 3px rgba(45, 95, 139, 0.1);
}

.bmi-model input::placeholder {
  color: #a0aec0;
  font-size: 0.875rem;
}

.bmi-model input:hover:not(:focus) {
  border-color: #cbd5e0;
}

/* Button */
.bmi-model button {
  width: 100%;
  margin-top: 1.5rem;
  padding: 0.875rem 1.5rem;
  font-size: 0.95rem;
  font-weight: 500;
  font-family: inherit;
  color: white;
  background: linear-gradient(135deg, #2d5f8b 0%, #1a3a5c 100%);
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  letter-spacing: 0.3px;
}

.bmi-model button:hover {
  background: linear-gradient(135deg, #1a4a6e 0%, #0f2a42 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(45, 95, 139, 0.2);
}

.bmi-model button:active {
  transform: translateY(0);
  box-shadow: 0 2px 6px rgba(45, 95, 139, 0.15);
}

/* Optional: Add responsive design */
@media (max-width: 640px) {
  .bmi-calculator {
    margin: 1rem;
    padding: 1.5rem;
  }
  
  .bmi-model {
    padding: 1rem;
  }
  
  .intro-para h2 {
    font-size: 1.25rem;
  }
}

/* Optional: Add subtle animations */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.bmi-calculator {
  animation: fadeIn 0.3s ease-out;
}

/* For Svelte transitions (optional) */
:global(body) {
  background-color: #f7fafc;
}
.hydration-calculator {
  max-width: 650px;
  margin: 0 auto;
  padding: 2rem;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
  background: linear-gradient(135deg, white 0%, black 100%);
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.hydration-calculator h1 {
  text-align: center;
  color: white;
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  font-weight: 700;
}

.intro-para-2 {
  background: rgba(255, 255, 255, 0.95);
  padding: 1.5rem;
  border-radius: 15px;
  margin-bottom: 2rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.intro-para-2 p {
  color: #333;
  line-height: 1.6;
  margin: 0;
  font-size: 1rem;
}

.hydration-model {
  background: rgba(255, 255, 255, 0.95);
  padding: 2rem;
  border-radius: 15px;
  margin-bottom: 2rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.hydration-model h2 {
  color: #667eea;
  font-size: 1.2rem;
  margin-bottom: 0.75rem;
  font-weight: 600;
}

.hydration-model input {
  width: 100%;
  padding: 12px 16px;
  margin-bottom: 1.5rem;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s ease;
  box-sizing: border-box;
}

.hydration-model input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.hydration-model input::placeholder {
  color: #999;
  font-size: 0.9rem;
}

.hydration-model button {
  width: 100%;
  padding: 14px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.hydration-model button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}

.hydration-model button:active {
  transform: translateY(0);
}

.result {
  background: rgba(255, 255, 255, 0.95);
  padding: 1.5rem;
  border-radius: 15px;
  text-align: center;
  font-size: 1.3rem;
  font-weight: 600;
  color: #667eea;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hydration-calculator {
    padding: 1rem;
    margin: 1rem;
  }
  
  .hydration-calculator h1 {
    font-size: 1.8rem;
  }
  
  .hydration-model {
    padding: 1.5rem;
  }
  
  .result {
    font-size: 1.1rem;
  }
}

/* Animation for result updates */
.result {
  animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

</style>