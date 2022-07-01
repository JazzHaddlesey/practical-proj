from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    chars = requests.get('http://rand-name-gen:5000/get_name').text
    nums = requests.get('http://rand-num-gen:5000/get_num').text
    prize = requests.post('http://race-gen:5000/race', json = dict(chars = chars, nums = nums))
    return render_template('home.html', prize = prize.text)
