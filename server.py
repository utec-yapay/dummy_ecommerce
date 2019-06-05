from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///minishop.db"

db = SQLAlchemy(app)

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProductName = db.Column(db.String(50))
    Price = db.Column(db.Integer)

# class Cart(db.Model):
#     __tablename__ = 'cart'
#     id = db.Column(db.Integer, db.Sequence("boleta_id_sequence"), primary_key=True)
#     numeroboleta = db.Column(db.Integer)
#     ProductId = db.Column(db.Integer, db.ForeignKey('products.id'))
#     ProductPrice = db.Column(db.Integer)

db.create_all()


if (Products.query.all() == []):
    db.session.add(Products(id=0, ProductName="Nike Free RN 2019 iD 0", Price=120))
    db.session.add(Products(id=1, ProductName="Nike Free RN 2019 iD 1", Price=80))
    db.session.add(Products(id=2, ProductName="Nike Free RN 2019 iD 2", Price=120))
    db.session.add(Products(id=3, ProductName="Nike Free RN 2019 iD 3", Price=120))
    db.session.add(Products(id=4, ProductName="Nike Free RN 2019 iD 4", Price=120))
    db.session.add(Products(id=5, ProductName="Nike Free RN 2019 iD 5", Price=80))
    db.session.add(Products(id=6, ProductName="Nike Free RN 2019 iD 6", Price=120))
    db.session.add(Products(id=7, ProductName="Nike Free RN 2019 iD 7", Price=120))

    db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

cartlist = []
@app.route('/shop', methods=['GET','POST'])
def shop():
    if request.method == 'POST':
        cartlist.append((request.form).to_dict())
        print(cartlist)
    return render_template('shop.html')

@app.route('/cart')
def cart():
    total = 0
    for dict in cartlist:
        total = total + int(dict["Price"])
    return render_template('cart.html', total=total)

@app.route('/checkout')
def checkout():
    total = 0
    for dict in cartlist:
        total = total + int(dict["Price"])
    return render_template('checkout.html', total=total)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


if __name__ == '__main__':
    app.run(debug=True)