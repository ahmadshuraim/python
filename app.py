from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello(name="World"):
    return "Hello %s!" % name
