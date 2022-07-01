from application import app
from flask import render_template
import requests
import names

@app.route('/get_name', methods = ['GET'])
def name_gen():
    full_name = names.get_full_name()
    return full_name
