from flask import Flask, render_template, request, jsonify
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

cartlist = []
@app.route('/shop', methods=['GET','POST'])
def shop():
    if request.method == 'POST':
        cartlist.append((request.form).to_dict())
    return render_template('shop.html')

@app.route('/cart')
def cart():
    total = 0
    for item in cartlist:
        total = total + int(item["Price"])

    return render_template('cart.html', total=total, cartlist=cartlist)

@app.route('/checkout')
def checkout():
    total = 0
    for item in cartlist:
        total = total + int(item["Price"])

    url = "http://localhost:8080/payments"

    payload = {
        "amt": total,
        "cpn": "Company S.A.C.",
        "cpp": "933740123"
    }

    r = requests.post(url, json=payload)

    return render_template('checkout.html', total=total, jwt=r.text)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
