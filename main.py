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
    sending = text + " AFFINE ENCRYPTED"
    return render_template("affine.html", encrypted=sending)

@app.route('/affineDecrypt', methods=['POST'])
def affineDecrypt():
    text = request.form["affine-decrypt"]
    sending = text + " AFFINE DECRYPTED"
    return render_template("affine.html", decrypted=sending)

@app.route("/columnar")
def columnar():
    return render_template("columnar.html")

@app.route('/columnarEncrypt', methods=['POST'])
def columnarEncrypt():
    text = request.form["columnar-encrypt"]
    sending = text + " COLUMNAR ENCRYPTED"
    return render_template("columnar.html", encrypted=sending)

@app.route('/columnarDecrypt', methods=['POST'])
def columnarDecrypt():
    text = request.form["columnar-decrypt"]
    sending = text + " COLUMNAR DECRYPTED"
    return render_template("columnar.html", decrypted=sending)

@app.route("/rsa")
def rsa():
    return render_template("rsa.html")

@app.route('/rsaEncrypt', methods=['POST'])
def rsaEncrypt():
    text = request.form["rsa-encrypt"]
    sending = text + " RSA ENCRYPTED"
    return render_template("rsa.html", encrypted=sending)

@app.route('/rsaDecrypt', methods=['POST'])
def rsaDecrypt():
    text = request.form["rsa-decrypt"]
    sending = text + " RSA DECRYPTED"
    return render_template("rsa.html", decrypted=sending)


@app.route("/substitution")
def substitution():
    return render_template("substitution.html")

@app.route('/substitutionEncrypt', methods=['POST'])
def substitutionEncrypt():
    text = request.form["substitution-encrypt"]
    sending = text + " SUBSTITUTION ENCRYPTED"
    return render_template("substitution.html", encrypted=sending)

@app.route('/substitutionDecrypt', methods=['POST'])
def substitutionDecrypt():
    text = request.form["substitution-decrypt"]
    sending = text + " SUBSTITUTION DECRYPTED"
    return render_template("substitution.html", decrypted=sending)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
