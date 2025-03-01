from flask import Flask, render_template, request
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)
@app.route('/', methods=['GET', 'POST'])
def createUserAccount():
    data = request.data

    return True
