from flask import Blueprint

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return "Hello World! Server Flask is working!"
