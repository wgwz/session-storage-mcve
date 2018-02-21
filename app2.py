from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('2.html')

@app.route('/get')
def get():
    return 'bleh'