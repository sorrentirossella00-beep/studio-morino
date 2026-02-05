from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Studio Odontotecnico Massimo Morino</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #a1c4fd, #c2e9fb);
            margin: 0;
            padding: 0;
            text-align: center;
            color: #333;
        }
        header {
            background-color: #0d6efd;
            color: white;
            padding: 30px;
        }
        h1 {
            margin: 0;
            font-size: 2.5em;
        }
        p {
            font-size: 1.2em;
            max-width: 700px;
            margin: 20px auto;
        }
        .btn {
            display: inline-block;
            padding: 12px 25px;
            margin: 15px;
            font-size: 1em;
            color: white;
            background-color: #198754;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none;
        }
        .btn:hover {
            background-color: #145c32;
        }
        footer {
            margin-top: 50px;
            padding: 20px;
            background-color: #0d6efd;
            color: white;
        }
    </style>
</head>
<body>
    <header>
        <h1>Studio Odontotecnico Massimo Morino</h1>
    </header>

    <p>Benvenuti nello studio odontotecnico di <strong>Massimo Morino</strong>, un professionista altamente qualificato, esperto e molto apprezzato nel suo settore. Grazie alla sua passione e competenza, ogni paziente riceve cure eccellenti e personalizzate.</p>

    <p>Lo studio offre servizi all'avanguardia e attenzione massima al comfort e alla sicurezza dei pazienti. Massimo Morino è rinomato per la sua precisione, affidabilità e cordialità.</p>

    <a class="btn" href="#">Scopri i nostri servizi</a>
    <a class="btn" href="#">Prenota una visita</a>
    <a class="btn" href="#">Contattaci</a>

    <footer>
        &copy; 2026 Studio Odontotecnico Massimo Morino
    </footer>
</body>
</html>
""")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
