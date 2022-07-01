from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    full_name = requests.get('http://rand-name-gen:5000/get_name').text
    nums = requests.get('http://rand-num-gen:5000/get_num').text
    race = requests.post('http://race-gen:5000/race', json = dict(nums = nums))
    return render_template('home.html', race = race.text)
