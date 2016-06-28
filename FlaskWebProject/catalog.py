
from flask import json

class Catalog(object):
    with open('FlaskWebProject/coffee.json', 'rb') as f:
        coffees = json.loads(f.read())  # produces single string

    def search(self, query):
        if len(query)== 0: 
            return self.coffees
        return [coffee for coffee in self.coffees if self.match(coffee, query)]

    def decrement(self, id, quantity):
        c = [coffee for coffee in  self.coffees if coffee['id'] == id]
        if len(c) != 0:
            c[0]['availability'] = c[0]['availability'] - quantity;
        return; 

    def match(self, coffee,query):
        return query in  coffee['id'].lower() or query in coffee['title'].lower() or query in coffee['description'].lower() 
