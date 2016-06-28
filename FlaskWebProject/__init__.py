from flask import Flask
app = Flask(__name__)

from FlaskWebProject.catalog import Catalog
cat = Catalog()

import FlaskWebProject.views
import FlaskWebProject.coffeeapi
import FlaskWebProject.orderapi
import FlaskWebProject.reservationapi