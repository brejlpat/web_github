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


@app.route("/formulare")
def formulare():
    return render_template("download.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
