from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/formulare")
def formulare():
    return render_template("download.html")


if __name__ == "__main__":
    #app.run()
    app.run(debug=True, port=5000, host="0.0.0.0")
