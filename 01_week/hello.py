from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/goodbye')
def goodbye():
    return 'Thank you for coming, see you back soon!'