from flask import Flask, render_template, request
from flask_cors import CORS
import json
import item as Item

app = Flask(__name__)

CORS(app)
@app.route('/', methods=['GET', 'POST'])
def createUserAccount():
    data = request.data

    return True

@app.route('/hackathonmarketplace/src/svelte', methods=['GET', 'POST'])
def createListing():
    form = request.form
    newListing = Item(form.name, form.image, form.price)