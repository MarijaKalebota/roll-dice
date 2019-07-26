from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Welcome to the dice rolling app!<br><br>"
    greeting+= "Options:<br>"
    greeting+= "\"/roll/<i>die_size</i>\" - Rolls a die of size <i>die_size</i>"

    return greeting

@app.route('/roll/<die_size>')
def roll_size(die_size):
    return str(random.randint(1, int(die_size)))
