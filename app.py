from flask import Flask, request, render_template, redirect, url_for
from affine import encrypt, decrypt
from rsa import rsaencrypt, rsadecrypt, modinv
from substitution import generate_key, sub_encrypt, sub_decrypt
from shift import shift_encrypt, shift_decrypt
from columnar import columnar_encrypt, columnar_decrypt

app = Flask(__name__)
affineHTML = "affine.html"
rsaHTML = "rsa.html"
subsHTML = "substitution.html"
shiftHTML = "shift.html"
columnarHTML = "columnar.html"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/affine")
def affine():
    return render_template(affineHTML)

@app.route('/affineEncrypt', methods=['POST'])
def affineEncrypt():
    text = request.form["affine-encrypt"]
    m = int(request.form["multKeyAffine"])
    a = int(request.form["addKeyAffine"])
    key = [m, a]
    sending = encrypt(text, key)
    return render_template(affineHTML, encrypted=sending)

@app.route('/affineDecrypt', methods=['POST'])
def affineDecrypt():
    text = request.form["affine-decrypt"]
    m = int(request.form["multKeyAffineDec"])
    a = int(request.form["addKeyAffineDec"])
    key = [m, a]
    sending = decrypt(text, key)
    return render_template(affineHTML, decrypted=sending)

@app.route("/shift")
def shift():
    return render_template(shiftHTML)

@app.route('/shiftEncrypt', methods=['POST'])
def shiftEncrypt():
    plain_text = request.form["shift-encrypt"]
    key = int(request.form["shiftEncKey"])
    sending = shift_encrypt(key, plain_text)
    return render_template(shiftHTML, encrypted=sending)

@app.route('/shiftDecrypt', methods=['POST'])
def shiftDecrypt():
    cipher_text = request.form["shift-decrypt"]
    key = int(request.form["shiftDecKey"])
    sending = shift_decrypt(key, cipher_text)
    return render_template(shiftHTML, decrypted=sending)

@app.route("/rsa")
def rsa():
    return render_template(rsaHTML)

@app.route('/rsaEncrypt', methods=['POST'])
def rsaEncrypt():
    plaintext = request.form["rsa-encrypt"]
    e = int(request.form["eEncrypt"])
    N = int(request.form["nEncrypt"])
    sending = rsaencrypt(e, N, plaintext)
    return render_template(rsaHTML, encrypted=sending)

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
    return render_template(rsaHTML, decrypted=sending)


@app.route("/substitution")
def substitution():
    return render_template(subsHTML)

@app.route('/substitutionEncrypt', methods=['POST'])
def substitutionEncrypt():
    plaintext = request.form["substitution-encrypt"]
    key = generate_key()
    sending = sub_encrypt(key, plaintext)
    return render_template(subsHTML, encrypted=sending, encryptedKey=key)

@app.route('/substitutionDecrypt', methods=['POST'])
def substitutionDecrypt():
    cipher_text = request.form["substitution-decrypt"]
    key = request.form["subKeyDec"]
    sending = sub_decrypt(key, cipher_text)
    return render_template(subsHTML, decrypted=sending)

@app.route("/columnar")
def columnar():
    return render_template(columnarHTML)

@app.route('/columnarEncrypt', methods=['POST'])
def columnarEncrypt():
    plain_text = request.form["columnar-encrypt"]
    key = request.form["columnar-encrypt-key"]
    sending = columnar_encrypt(plain_text, key)
    return render_template(columnarHTML, encrypted=sending)

@app.route('/columnarDecrypt', methods=['POST'])
def columnarDecrypt():
    cipher_text = request.form["column-decrypt"]
    key = request.form["columnKeyDec"]
    sending = columnar_decrypt(cipher_text, key)
    return render_template(columnarHTML, decrypted=sending)


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
