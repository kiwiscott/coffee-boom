"""
Routes and views for the flask application.
"""
from datetime import datetime
from random import random
from flask import Flask, jsonify, json, abort,request
from FlaskWebProject import app, cat

@app.route('/api/v1.0/coffees', methods=['GET'])
def get_coffees():
    query = request.args.get('query')
    if query is None:
         return jsonify(cat.coffees)

    query = query.lower()
    c = cat.search(query)
    return jsonify(c)
