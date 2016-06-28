"""
Routes and views for the flask application.
"""

from datetime import datetime
from random import random
from flask import Flask, jsonify, json, abort,request
from FlaskWebProject import app, cat

@app.route('/api/v1.0/reservations', methods=['POST'])
def reserve():
    if not request.json:
        abort(400)

    for item in request.json:
        cat.decrement(item['id'],item['qty'])

    return jsonify(None)


