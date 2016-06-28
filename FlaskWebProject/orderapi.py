from datetime import datetime, timedelta
from random import random
from flask import Flask, jsonify, json, abort,request
from FlaskWebProject import app

orders=[]

@app.route('/api/v1.0/orders', methods=['POST'])
def order_something():
    if not request.json or not 'customer' in request.json:
        abort(400)

    number = len(orders)+1
    eta = datetime.utcnow() + timedelta(hours=24)
    o = {
        'id': len(orders) + 1,
        'endcustomer': request.json['customer'],
        'eta': eta,
        'shipped': False
    }
    orders.append(o)
    return jsonify(o), 201

@app.route('/api/v1.0/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    c = [order for order in orders if order['id'] == order_id]
    if len(c) == 0:
        abort(404)
    return jsonify(c[0])
