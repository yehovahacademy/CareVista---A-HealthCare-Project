<div class="Navbar">
<img src="/logo.png" alt=carevista/>
<h1>Care<em>Vista</em></h1>
  <a href="/">Home</a>
	<a href="/dashboard">Health Meter</a>
  <a href="/register">Register</a>
  <a href="/contactus">Contact Us</a>
</div>

<br><br>



<slot />


<br><br><br><br>
<footer class="Footer">
  <div class="Footer__brand">
    <img src="/logo.png" alt="carevista" />
    <h2>Care<em>Vista</em></h2>
    <p>Compassionate care, closer to you.</p>
  </div>

  <div class="Footer__links">
    <h3>Navigation</h3>
    <a href="/">Home</a>
    <a href="/register">Register</a>
    <a href="/contactus">Contact Us</a>
  </div>

  <div class="Footer__links">
    <h3>Company</h3>
    <a href="/careers">Careers</a>
    <a href="/privacy">Privacy Policy</a>
  </div>

  <div class="Footer__contact">
    <h3>Get in Touch</h3>
    <p>📧 hello@carevista.com</p>
    <p>📞 +1 (800) 123-4567</p>
    <p>📍 Mumbai, Maharashtra</p>
  </div>
</footer>

<div class="Footer__bottom">
  <p>© 2026 CareVista. All rights reserved.</p>
</div>


<style>
.Navbar {
    display: flex;
    align-items: center;
    gap: 2rem;
    padding: 1rem 2.5rem;
    background: #ffffff;
    border-bottom: 1px solid #e8edf2;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
    font-family: 'Georgia', serif;
  }

  .Navbar img {
    width: 55px;
    height: 55px;
    border-radius: 50%;
    object-fit: cover;
  }

  .Navbar h1 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1a2e3b;
    margin: 0;
    margin-right: auto; /* pushes nav links to the right */
    letter-spacing: -0.02em;
  }

  .Navbar h1 em {
    font-style: italic;
    color: #2a9d8f;
  }

  .Navbar a {
    text-decoration: none;
    color: #4a5568;
    font-size: 0.95rem;
    font-weight: 500;
    letter-spacing: 0.01em;
    padding: 0.4rem 0.75rem;
    border-radius: 6px;
    transition: color 0.2s ease, background 0.2s ease;
  }

  .Navbar a:hover {
    color: #2a9d8f;
    background: #f0faf9;
  }

  .Navbar a:last-child {
    background: #2a9d8f;
    color: #ffffff;
    padding: 0.4rem 1rem;
  }

  .Navbar a:last-child:hover {
    background: #21867a;
    color: #ffffff;
  }

	.Footer {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1.5fr;
    gap: 2.5rem;
    padding: 3rem 2.5rem 2rem;
    background: #1a2e3b;
    color: #cbd5e0;
    font-family: 'Georgia', serif;
		
  }

  /* Brand column */
  .Footer__brand img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 0.5rem;
  }

  .Footer__brand h2 {
    font-size: 1.3rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 0.5rem;
    letter-spacing: -0.02em;
  }

  .Footer__brand h2 em {
    font-style: italic;
    color: #2a9d8f;
  }

  .Footer__brand p {
    font-size: 0.875rem;
    color: #94a3b8;
    margin: 0;
    line-height: 1.6;
  }

  /* Link columns */
  .Footer__links {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
  }

  .Footer__links h3,
  .Footer__contact h3 {
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #2a9d8f;
    margin: 0 0 0.5rem;
  }

  .Footer__links a {
    text-decoration: none;
    color: #94a3b8;
    font-size: 0.9rem;
    transition: color 0.2s ease;
  }

  .Footer__links a:hover {
    color: #ffffff;
  }

  /* Contact column */
  .Footer__contact {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .Footer__contact p {
    font-size: 0.875rem;
    color: #94a3b8;
    margin: 0;
  }

  /* Bottom bar */
  .Footer__bottom {
    background: #111e27;
    padding: 1rem 2.5rem;
    font-family: 'Georgia', serif;
		
  }

  .Footer__bottom p {
    font-size: 0.8rem;
    color: #64748b;
    margin: 0;
    text-align: center;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .Footer {
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
    }

    .Footer__brand {
      grid-column: 1 / -1;
    }
  }

  @media (max-width: 480px) {
    .Footer {
      grid-template-columns: 1fr;
    }
  }

</style>
