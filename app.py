from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "hello world"
