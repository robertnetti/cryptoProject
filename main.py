from flask import Flask, request, render_template, redirect, url_for
from affine import *
from rsa import *
from substitution import *

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
    m = int(request.form["multKeyAffine"])
    a = int(request.form["addKeyAffine"])
    key = [m, a]
    sending = encrypt(text, key)
    return render_template("affine.html", encrypted=sending)

@app.route('/affineDecrypt', methods=['POST'])
def affineDecrypt():
    text = request.form["affine-decrypt"]
    m = int(request.form["multKeyAffineDec"])
    a = int(request.form["addKeyAffineDec"])
    key = [m, a]
    sending = decrypt(text, key)
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
    plaintext = request.form["rsa-encrypt"]
    e = int(request.form["eEncrypt"])
    N = int(request.form["nEncrypt"])
    sending = rsaencrypt(e, N, plaintext)
    return render_template("rsa.html", encrypted=sending)

@app.route('/rsaDecrypt', methods=['POST'])
def rsaDecrypt():
    ciphertext = request.form["rsa-decrypt"]
    e = int(request.form["eDec"])
    p = int(request.form["pDec"])
    q = int(request.form["qDec"])
    phiN = (p-1)*(q-1)
    N = p*q
    d = modinv(e, phiN)
    sending = rsadecrypt(d, N, ciphertext)
    return render_template("rsa.html", decrypted=sending)


@app.route("/substitution")
def substitution():
    return render_template("substitution.html")

@app.route('/substitutionEncrypt', methods=['POST'])
def substitutionEncrypt():
    plain_text = request.form["substitution-encrypt"]
    key = int(request.form["subKeyEnc"])
    sending = sub_encrypt(key, plain_text)
    return render_template("substitution.html", encrypted=sending)

@app.route('/substitutionDecrypt', methods=['POST'])
def substitutionDecrypt():
    cipher_text = request.form["substitution-decrypt"]
    key = int(request.form["subKeyDec"])
    sending = sub_decrypt(key, cipher_text)
    return render_template("substitution.html", decrypted=sending)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
