"""
Routes and views for the flask application.
"""

from datetime import datetime
from random import random
from flask import Flask, jsonify, json, abort,request
from FlaskWebProject import app

with open('coffee.json', 'rb') as f:
     coffees = json.loads(f.read())  # produces single string

@app.route('/api/v1.0/coffees', methods=['GET'])
def get_coffees():
    query = request.args.get('query')
    if query is None:
        return jsonify(coffees)
    
    query = query.lower()
    c = [coffee for coffee in coffees if match(coffee, query)]
    return jsonify(c)

def match(coffee,query):
    return query in coffee['title'].lower() or query in coffee['description'].lower()