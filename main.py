from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/affine")
def affine():
    return render_template("affine.html")

@app.route('/affineEncrypt', methods=['POST'])
def affineEncrypt():
    text = request.form["affine-encrypt"]
    sending = text + " ENCRYPTED"
    return render_template("affine.html", encrypted=sending)

@app.route('/affineDecrypt', methods=['POST'])
def affineDecrypt():
    text = request.form["affine-decrypt"]
    sending = text + " DECRYPTED"
    return render_template("affine.html", decrypted=sending)

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
