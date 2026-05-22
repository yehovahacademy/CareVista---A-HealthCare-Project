<script>
  let fname = $state('')
let lname = $state('')
let email = $state('')
let contact = $state('')
let password = $state('')
let terms = $state(false)
let toast = $state(null)

async function registerUser() {
  try {
    // Added https:// to the URL
    const response = await fetch("https://carevista-a-healthcare-project-production.up.railway.app/auth/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        fname,
        lname,
        email,
        contact,
        password
      })
    })

    if (!response.ok) {
      toast = { type: 'error', message: `Registration failed: ${response.status}` }
      return
    }

    const data = await response.json()
    toast = { type: 'success', message: data.message || 'Registration successful!' }
    
  } catch (error) {
    console.error('Registration error:', error)
    toast = { type: 'error', message: 'Could not connect to server' }
  }
}

			body: JSON.stringify({
				fname,
				lname,
				email,
				password,
				contact
			})
		});

		const data = await response.json();

		console.log(data);

		alert(data.message);
  }


  //For Toast Message

  function showToast(message, type = 'success') {
  toast = { message, type };
  setTimeout(() => {
    toast = null;
  }, 3000);
}

function handleSubmit() {
  if (!terms) {
    showToast('Please agree to the Terms of Service.', 'error');
    return;
  }
  if (!fname || !email || !password) {
    showToast('Please fill in all required fields.', 'error');
    return;
  }
  showToast('Account created successfully!', 'success');
}


</script>

<div class="reg-root">
  <p class="reg-eyebrow">Welcome aboard</p>
  <h1 class="reg-title">Create your account</h1>
  <p class="reg-sub">Start your journey — it only takes a minute.</p>

  <div class="row">
    <div class="field">
      <label for="fname">First name</label>
      <input id="fname" type="text" placeholder="Ada" bind:value={fname} autocomplete="given-name" />
    </div>
    <div class="field">
      <label for="lname">Last name</label>
      <input id="lname" type="text" placeholder="Lovelace" bind:value={lname} autocomplete="family-name" />
    </div>
  </div>

  <div class="field">
    <label for="email">Email address</label>
    <div class="input-icon">
      <i class="ti ti-mail"></i>
      <input id="email" type="email" placeholder="ada@example.com" bind:value={email} autocomplete="email" />
    </div>
  </div>

  <div class="field">
    <label for="phone">Phone number</label>
    <div class="input-icon">
      <i class="ti ti-phone"></i>
      <input id="phone" type="tel" placeholder="+91 98765 43210" bind:value={contact} autocomplete="tel" />
    </div>
  </div>

  <div class="field">
    <label for="password">Password</label>
    <div class="pass-wrap">
      <i class="ti ti-lock"></i>
      <input id="password" type="password" placeholder="Min. 8 characters" bind:value={password} autocomplete="new-password" />
    </div>
  </div>

  <div class="checkbox-row">
    <input type="checkbox" id="terms" bind:checked={terms} />
    <span>I agree to the <a href="/terms">Terms of Service</a> and <a href="/privacy">Privacy Policy</a></span>
  </div>

  <button class="btn-submit" type="submit" onclick={registerUser}>Create account</button>

  <p class="sign-in">Already have an account? <a href="/login">Sign in</a></p>
</div>
{#if toast}
  <div class="toast toast--{toast.type}">
    {#if toast.type === 'success'}
      <svg />  <!-- checkmark icon -->
    {:else}
      <svg />  <!-- x icon -->
    {/if}
    <span>{toast.message}</span>
  </div>
{/if}

<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500&display=swap');

  .reg-root { font-family: 'DM Sans', sans-serif; max-width: 480px; margin: 0 auto; padding: 2rem 1rem; }
  .reg-eyebrow { font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: #aaa; margin-bottom: 0.5rem; }
  .reg-title { font-family: 'DM Serif Display', serif; font-size: 32px; font-weight: 400; margin: 0 0 0.25rem; }
  .reg-sub { font-size: 14px; color: #666; margin: 0 0 2rem; }

  .row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }

  .field { margin-bottom: 1.25rem; }
  .field label { display: block; font-size: 13px; font-weight: 500; color: #555; margin-bottom: 6px; }
  .field input { width: 100%; box-sizing: border-box; height: 42px; border-radius: 8px; border: 0.5px solid #ccc; font-size: 14px; padding: 0 12px; outline: none; }
  .field input:focus { border: 1.5px solid #7F77DD; box-shadow: 0 0 0 3px rgba(127,119,221,0.12); }

  .input-icon { position: relative; }
  .input-icon input { padding-left: 38px; }
  .input-icon i { position: absolute; left: 11px; top: 50%; transform: translateY(-50%); font-size: 16px; color: #aaa; pointer-events: none; }

  .pass-wrap { position: relative; }
  .pass-wrap input { padding-left: 38px; width: 100%; box-sizing: border-box; height: 42px; border-radius: 8px; border: 0.5px solid #ccc; font-size: 14px; outline: none; }
  .pass-wrap i { position: absolute; left: 11px; top: 50%; transform: translateY(-50%); font-size: 16px; color: #aaa; pointer-events: none; }

  .checkbox-row { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 1.5rem; }
  .checkbox-row input { margin-top: 2px; accent-color: #7F77DD; width: 15px; height: 15px; flex-shrink: 0; }
  .checkbox-row span { font-size: 13px; color: #555; line-height: 1.5; }
  .checkbox-row a { color: #534AB7; text-decoration: none; }

  .btn-submit { width: 100%; height: 46px; border-radius: 8px; background: #534AB7; color: #fff; font-size: 15px; font-weight: 500; border: none; cursor: pointer; }
  .btn-submit:hover { background: #3C3489; }

  .sign-in { text-align: center; font-size: 13px; color: #666; margin-top: 1.25rem; }
  .sign-in a { color: #534AB7; font-weight: 500; text-decoration: none; }




  .toast {
  position: fixed;
  bottom: 1.5rem;
  right: 1.5rem;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  animation: slide-in 0.2s ease;
}

.toast--success { background: #f0fdf4; color: #166534; border: 0.5px solid #bbf7d0; }
.toast--error   { background: #fef2f2; color: #991b1b; border: 0.5px solid #fecaca; }

@keyframes slide-in {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}
</style>