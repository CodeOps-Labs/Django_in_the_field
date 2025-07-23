from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse("Welcome home\n this is hammad \n <h1> Hammad </h1>  <span> Django </span > ")

from django.http import HttpResponse

def returntxt(request):
    txt = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Hammad | Software Engineer</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
      color: #f4f4f4;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }

    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 2rem;
      background-color: rgba(0, 0, 0, 0.3);
      box-shadow: 0 2px 4px rgba(0,0,0,0.4);
    }

    .profile-info {
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }

    .profile-info img {
      width: 100px;
      height: 100px;
      object-fit: cover;
      border-radius: 50%;
      border: 3px solid #1de9b6;
      transition: transform 0.4s ease;
    }

    .profile-info img:hover {
      transform: scale(1.05);
    }

    .profile-text h1 {
      font-size: 2.2rem;
      font-weight: bold;
    }

    .profile-text p {
      font-size: 1.1rem;
      opacity: 0.85;
    }

    .social-links {
      display: flex;
      gap: 1rem;
    }

    .social-links a {
      font-size: 1.6rem;
      color: #f4f4f4;
      transition: transform 0.3s, color 0.3s;
    }

    .social-links a:hover {
      transform: scale(1.2);
      color: #1de9b6;
    }

    .hero {
      flex-grow: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 4rem 2rem;
      text-align: center;
      animation: fadeIn 1.5s ease-in-out;
    }

    .hero h2 {
      font-size: 2.5rem;
      margin-bottom: 1rem;
    }

    .hero p {
      font-size: 1.2rem;
      max-width: 700px;
      margin: 0 auto;
      opacity: 0.9;
    }

    .projects-banner {
      background-color: #1de9b6;
      color: #111;
      padding: 1.5rem;
      text-align: center;
      font-size: 1.5rem;
      font-weight: bold;
      letter-spacing: 1px;
      margin-top: 2rem;
    }

    footer {
      text-align: center;
      padding: 1rem;
      font-size: 0.9rem;
      opacity: 0.7;
      background-color: rgba(0, 0, 0, 0.2);
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 600px) {
      header {
        flex-direction: column;
        gap: 1rem;
      }

      .hero h2 {
        font-size: 1.8rem;
      }

      .profile-info img {
        width: 80px;
        height: 80px;
      }
    }
  </style>
</head>
<body>

  <header>
    <div class="profile-info">
      <img src="hammad.jpg" />
      <div class="profile-text">
        <h1>Hammad</h1>
        <p>Software Engineer | Python Backend Developer</p>
      </div>
    </div>
    <div class="social-links">
      <a href="https://www.linkedin.com/in/YOUR-LINKEDIN" target="_blank" aria-label="LinkedIn">
        <i class="fab fa-linkedin"></i>
      </a>
      <a href="https://www.instagram.com/YOUR-INSTA" target="_blank" aria-label="Instagram">
        <i class="fab fa-instagram"></i>
      </a>
      <a href="https://twitter.com/YOUR-X-ACCOUNT" target="_blank" aria-label="X">
        <i class="fab fa-x-twitter"></i>
      </a>
    </div>
  </header>

  <main class="hero">
    <div>
      <h2>Welcome to Hammad’s Portfolio</h2>
      <p>
        Crafting clean code, designing backend architecture, and delivering scalable solutions with Python & Django.
      </p>
    </div>
  </main>

  <section class="projects-banner">
    Explore My Projects & Contributions!
  </section>

  <footer>
    &copy; 2025 Hammad Ibrahim. All rights reserved.
  </footer>

</body>
</html>

    """

    return HttpResponse(txt)

