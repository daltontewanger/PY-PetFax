# Config                    
from flask import Flask
app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return 'Hello, this is not hello world!'
@app.route('/pets')
def pets(): 
    return 'These are our pets available for adoption!'
