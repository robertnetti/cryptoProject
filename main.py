from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/affine")
def affine():
    return render_template("affine.html")

@app.route("/columnar")
def columnar():
    return render_template("columnar.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/rsa")
def rsa():
    return render_template("rsa.html")


@app.route("/substitution")
def substitution():
    return render_template("substitution.html")

if __name__ == "__main__":
    app.run(debug=True)
