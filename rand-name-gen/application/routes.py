from application import app
from flask import render_template
import requests
import names

@app.route('/')
def index():
    full_name = names.get_full_name()
    return full_name