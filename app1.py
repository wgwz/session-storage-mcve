import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        '1.html',
    iframe_server='https://qtbrvovhpj.localtunnel.me'
    )