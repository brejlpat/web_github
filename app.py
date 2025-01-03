from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Nastavení e-mailu pro Seznam
SMTP_SERVER = "smtp.seznam.cz"  # SMTP server Seznam.cz
SMTP_PORT = 587  # SMTP port (pro TLS)
EMAIL_ADDRESS = "webtest.mail@seznam.cz"  # Nahraď svým e-mailem na Seznam.cz
EMAIL_PASSWORD = "Web_test123"  # Nahraď svým heslem (nebo použij heslo aplikace)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        phone = request.form["phone"]
        print(f"Jméno: {name}\nE-mail: {email}\nTelefon: {phone}\nZpráva: {message}")

        # Obsah e-mailu
        subject = f"Nová zpráva z webu od {name}"
        body = f"""
        Jméno: {name}\n
        E-mail: {email}\n
        Telefon: {phone}\n
        {message}
        """

        try:
            # Vytvoření připojení k SMTP serveru Seznam.cz
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Zabezpečené připojení
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Přihlášení

                # Sestavení e-mailu
                msg = MIMEMultipart()
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = "patrikbrejla@seznam.cz"  # Nahraď adresou příjemce
                msg["Subject"] = subject
                msg.attach(MIMEText(body, "plain"))

                # Odeslání e-mailu
                server.send_message(msg)

            print("E-mail byl úspěšně odeslán.")

        except Exception as e:
            print(f"Chyba při odesílání e-mailu: {e}")

        return redirect(url_for("home"))
    return render_template("form.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
